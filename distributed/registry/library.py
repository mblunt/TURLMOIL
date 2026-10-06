"""Library registry for managing parser implementations."""

from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session

from core.models import Library
from core.database import get_session


class LibraryRegistry:
    """Registry for parser library management."""
    
    @staticmethod
    def register(
        name: str,
        language: str,
        version: Optional[str] = None,
        description: Optional[str] = None,
        binary_path: Optional[str] = None,
        command: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
        session: Optional[Session] = None
    ) -> Library:
        """Register a new parser library.
        
        Args:
            name: Unique name for this library
            language: Implementation language
            version: Library version string
            description: Human-readable description
            binary_path: Path to compiled binary (for Go/Rust/etc)
            command: Custom command template (use {url} placeholder)
            config: Additional configuration dict
            session: Optional existing session
            
        Returns:
            The created Library object
        """
        def _register(sess: Session) -> Library:
            # Check if already exists
            existing = sess.query(Library).filter(Library.name == name).first()
            if existing:
                raise ValueError(f"Library '{name}' already registered")
            
            library = Library(
                name=name,
                language=language,
                version=version,
                description=description,
                binary_path=binary_path,
                command=command,
                config=config or {},
                enabled=True
            )
            sess.add(library)
            sess.flush()  # populates library.id

            # Seed a zero-count matrix row for every existing (other) library
            return library
        
        if session:
            return _register(session)
        else:
            with get_session() as sess:
                return _register(sess)
    
    @staticmethod
    def update(
        name: str,
        session: Optional[Session] = None,
        **kwargs
    ) -> Library:
        """Update an existing library's configuration."""
        def _update(sess: Session) -> Library:
            library = sess.query(Library).filter(Library.name == name).first()
            if not library:
                raise ValueError(f"Library '{name}' not found")
            
            for key, value in kwargs.items():
                if hasattr(library, key):
                    setattr(library, key, value)
            
            sess.flush()
            return library
        
        if session:
            return _update(session)
        else:
            with get_session() as sess:
                return _update(sess)
    
    @staticmethod
    def get(name: str, session: Optional[Session] = None) -> Optional[Library]:
        """Get a library by name."""
        def _get(sess: Session) -> Optional[Library]:
            return sess.query(Library).filter(Library.name == name).first()
        
        if session:
            return _get(session)
        else:
            with get_session() as sess:
                return _get(sess)
    
    @staticmethod
    def get_by_id(library_id: int, session: Optional[Session] = None) -> Optional[Library]:
        """Get a library by ID."""
        def _get(sess: Session) -> Optional[Library]:
            return sess.query(Library).filter(Library.id == library_id).first()
        
        if session:
            return _get(session)
        else:
            with get_session() as sess:
                return _get(sess)
    
    @staticmethod
    def list_all(
        enabled_only: bool = True,
        language: Optional[str] = None,
        session: Optional[Session] = None
    ) -> List[Library]:
        """List all registered libraries."""
        def _list(sess: Session) -> List[Library]:
            query = sess.query(Library)
            if enabled_only:
                query = query.filter(Library.enabled == True)
            if language:
                query = query.filter(Library.language == language)
            return query.order_by(Library.name).all()
        
        if session:
            return _list(session)
        else:
            with get_session() as sess:
                return _list(sess)
    
    @staticmethod
    def enable(name: str, session: Optional[Session] = None) -> Library:
        return LibraryRegistry.update(name, session=session, enabled=True)
    
    @staticmethod
    def disable(name: str, session: Optional[Session] = None) -> Library:
        return LibraryRegistry.update(name, session=session, enabled=False)
    
    @staticmethod
    def delete(name: str, session: Optional[Session] = None) -> bool:
        def _delete(sess: Session) -> bool:
            library = sess.query(Library).filter(Library.name == name).first()
            if not library:
                return False
            sess.delete(library)
            return True
        
        if session:
            return _delete(session)
        else:
            with get_session() as sess:
                return _delete(sess)
    
    @staticmethod
    def count(enabled_only: bool = True, session: Optional[Session] = None) -> int:
        def _count(sess: Session) -> int:
            query = sess.query(Library)
            if enabled_only:
                query = query.filter(Library.enabled == True)
            return query.count()
        
        if session:
            return _count(session)
        else:
            with get_session() as sess:
                return _count(sess)
