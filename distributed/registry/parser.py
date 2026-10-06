"""Parser execution utilities."""

import subprocess
import json
import time
from typing import Dict, Any, Optional
from dataclasses import dataclass

from core.models import Library


@dataclass
class ParseOutput:
    success: bool
    error: Optional[str]
    data: Dict[str, Any]
    parse_time_ms: float
    raw_output: str


class ParserRunner:
    """Execute parser binaries and capture output."""
    
    @staticmethod
    def run(library: Library, url: str, timeout: float = 15.0) -> ParseOutput:
        """Run a parser library against a URL.
        
        Args:
            library: The library to run
            url: URL to parse
            timeout: Maximum execution time in seconds
            
        Returns:
            ParseOutput with results
        """
        start_time = time.perf_counter()
        
        # Determine how to run this parser
        if library.command:
            # Custom command template
            args = [library.command, url]
        elif library.binary_path:
            # Direct binary invocation
            args = [library.binary_path, url]
        else:
            return ParseOutput(
                success=False,
                error="No execution method configured for library",
                data={},
                parse_time_ms=0,
                raw_output=""
            )
        
        try:
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            parse_time_ms = (time.perf_counter() - start_time) * 1000
            raw_output = result.stdout
            if result.returncode != 0 and not raw_output and result.stderr:
                return ParseOutput(
                    success=False,
                    error=result.stderr.strip(),
                    data={},
                    parse_time_ms=parse_time_ms,
                    raw_output=result.stderr
                )

            # Try to parse JSON output; fall back to ast.literal_eval for
            # parsers that emit Python-style single-quoted dicts.
            try:
                try:
                    data = json.loads(raw_output)
                except json.JSONDecodeError:
                    import ast
                    data = ast.literal_eval(raw_output.strip())
                
                # Check if output indicates an error
                if "error" in data and data["error"]:
                    return ParseOutput(
                        success=False,
                        error=data["error"],
                        data=data,
                        parse_time_ms=parse_time_ms,
                        raw_output=raw_output
                    )
                
                return ParseOutput(
                    success=True,
                    error=None,
                    data=data,
                    parse_time_ms=parse_time_ms,
                    raw_output=raw_output
                )
                
            except (json.JSONDecodeError, ValueError, SyntaxError) as e:
                return ParseOutput(
                    success=False,
                    error=f"Unparseable output: {e}",
                    data={},
                    parse_time_ms=parse_time_ms,
                    raw_output=raw_output
                )
                
        except subprocess.TimeoutExpired:
            parse_time_ms = (time.perf_counter() - start_time) * 1000
            return ParseOutput(
                success=False,
                error=f"Parser timed out after {timeout}s",
                data={},
                parse_time_ms=parse_time_ms,
                raw_output=""
            )
            
        except FileNotFoundError:
            return ParseOutput(
                success=False,
                error=f"Parser binary not found: {args[0]}",
                data={},
                parse_time_ms=0,
                raw_output=""
            )
            
        except Exception as e:
            parse_time_ms = (time.perf_counter() - start_time) * 1000
            return ParseOutput(
                success=False,
                error=f"Execution error: {str(e)}",
                data={},
                parse_time_ms=parse_time_ms,
                raw_output=""
            )
