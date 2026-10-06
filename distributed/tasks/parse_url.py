"""URL parsing Celery task."""

from typing import Dict, Any, Optional
from datetime import datetime, timezone
import json
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update

from tasks.celery_app import app
from core.database import get_session
from core.models import Library, ParseJob, ParseResult, JobStatus
from registry.parser import ParserRunner

@app.task(bind=True, name="tasks.parse_url.parse_single")
def parse_single(self, job_id: int, library_id: int) -> Dict[str, Any]:
    """Parse a URL with a specific library.
    
    This task is idempotent - if a result already exists for this job+library,
    it will not create a duplicate.
    
    Args:
        job_id: The ParseJob ID
        library_id: The Library ID to use
        
    Returns:
        Dict with parse result summary
    """
    with get_session() as session:
        # Check if result already exists (idempotency)
        existing_result = session.query(ParseResult).filter(
            ParseResult.job_id == job_id,
            ParseResult.library_id == library_id
        ).first()
        
        if existing_result:
            return {
                "job_id": job_id,
                "library_id": library_id,
                "success": existing_result.success,
                "note": "Result already exists (idempotent skip)"
            }
        
        # Get job and library
        job = session.query(ParseJob).filter(ParseJob.id == job_id).first()
        library = session.query(Library).filter(Library.id == library_id).first()
        
        if not job:
            return {"error": f"Job {job_id} not found"}
        if not library:
            return {"error": f"Library {library_id} not found"}
        
        # Capture data we need before session closes
        library_name = library.name
        url = job.url.replace("\\x00", "\x00")  # restore NUL bytes stripped for DB storage

        # Run parser
        output = ParserRunner.run(library, url)
        
        # Create result record
        result = ParseResult(
            job_id=job_id,
            library_id=library_id,
            success=output.success,
            error_message=output.error,
            parse_time_ms=output.parse_time_ms,
            raw_output=output.data,
        )
        
        # Extract parsed fields if successful
        if output.success:
            # Helper to convert values to strings (handles dicts, lists, etc.)
            def to_text(value):
                if value is None:
                    return None
                if isinstance(value, (dict, list)):
                    return json.dumps(value)
                return str(value)
            
            result.scheme = to_text(output.data.get("scheme"))
            result.authority = to_text(output.data.get("authority"))
            result.userinfo = to_text(output.data.get("userinfo"))
            result.username = to_text(output.data.get("username"))
            result.password = to_text(output.data.get("password"))
            result.host = to_text(output.data.get("host"))
            result.port = to_text(output.data.get("port"))
            result.path = to_text(output.data.get("path"))
            result.query = to_text(output.data.get("query"))
            result.query_dict = output.data.get("query_dict")
            result.fragment = to_text(output.data.get("fragment"))
        
        session.add(result)
        
        try:
            # Flush to get IDs and detect constraint violations before context manager commits
            session.flush()
        except IntegrityError:
            # Result already exists (race condition with another worker)
            session.rollback()
            return {
                "job_id": job_id,
                "library_id": library_id,
                "library_name": library_name,
                "success": True,
                "note": "Result already exists (duplicate task skipped)"
            }
        
        # Update job progress atomically and check for completion in one transaction
        # First, increment the counter atomically
        session.execute(
            update(ParseJob)
            .where(ParseJob.id == job_id)
            .values(libraries_completed=ParseJob.libraries_completed + 1)
        )
        row = session.execute(
            select(ParseJob.libraries_completed, ParseJob.libraries_total)
            .where(ParseJob.id == job_id)
        ).fetchone()
        
        # Check if this was the last library to complete
        job_complete = row and row[0] >= row[1]  # libraries_completed >= libraries_total
        if job_complete:
            session.execute(
                update(ParseJob)
                .where(ParseJob.id == job_id)
                .values(
                    status=JobStatus.COMPLETED.value,
                    completed_at=datetime.now(timezone.utc)
                )
            )

    if job_complete:
        pass  # differential analysis disabled

    return {
        "job_id": job_id,
        "library_id": library_id,
        "library_name": library_name,
        "success": output.success,
        "error": output.error,
        "parse_time_ms": output.parse_time_ms,
    }


@app.task(bind=True, name="tasks.parse_url.parse_all")
def parse_all(self, job_id: int) -> Dict[str, Any]:
    """Parse a URL with all enabled libraries.
    
    Args:
        job_id: The ParseJob ID
        
    Returns:
        Dict with task IDs for each library parse
    """
    with get_session() as session:
        job = session.query(ParseJob).filter(ParseJob.id == job_id).first()
        if not job:
            return {"error": f"Job {job_id} not found"}
        
        # Get all enabled libraries - query directly to avoid detachment issues
        libraries = session.query(Library).filter(Library.enabled == True).all()

        # Extract IDs while session is active to avoid detachment
        library_data = [(lib.id, lib.name, lib.language) for lib in libraries]

        if not library_data:
            return {"error": "No enabled libraries found"}

        # Update job
        job.status = JobStatus.IN_PROGRESS.value
        job.started_at = datetime.now(timezone.utc)
        job.libraries_total = len(library_data)
        # Flush will be done by context manager

    # Dispatch parse tasks for each library (outside session context)
    task_ids = {}
    for lib_id, lib_name, lang in library_data:
        task = parse_single.apply_async(args=[job_id, lib_id], queue=lang)
        task_ids[lib_name] = task.id
    
    return {
        "job_id": job_id,
        "libraries_count": len(library_data),
        "task_ids": task_ids,
    }


@app.task(bind=True, name="tasks.parse_url.parse_url")
def parse_url(self, url: str) -> Dict[str, Any]:
    """Create a job and parse URL with all libraries.
    
    This is a convenience wrapper that creates a job and dispatches parsing.
    Returns immediately without waiting for completion.
    
    Args:
        url: The URL to parse
        
    Returns:
        Dict with job info and parse_all task ID
    """
    with get_session() as session:
        # Create job
        job = ParseJob(url=url, status=JobStatus.PENDING.value)
        session.add(job)
        session.flush()
        job_id = job.id
    
    # Dispatch to all libraries (async, don't wait)
    task = parse_all.delay(job_id)
    
    return {
        "job_id": job_id,
        "url": url,
        "parse_task_id": task.id
    }
