#!/usr/bin/env python3
"""Python URL parser using furl.

Parses URLs using furl and outputs JSON.
"""

import sys
import json
from httpx import URL

#  1. scheme
#  2. authority
#     2a. userinfo
#         2aa. username
#         2ab. password
#     2b. host
#     2c. port
# 3. path
# 4. query
#     4a. query_dict
# 5. fragment

def parse_url(url: str) -> dict:
    """Parse a URL and return components as a dictionary."""
    def safe_str(val):
        if isinstance(val, bytes):
            try:
                return val.decode('utf-8', errors='replace')
            except Exception:
                return str(val)
        return val

    try:
        parsed = URL(url)
        return {
            "scheme": safe_str(parsed.scheme) if parsed.scheme is not None else None,
            "authority": safe_str(parsed.netloc) if parsed.netloc is not None else None,
            "userinfo": safe_str(parsed.userinfo) if parsed.userinfo is not None else None,
            "username": safe_str(parsed.username) if parsed.username is not None else None,
            "password": safe_str(parsed.password) if parsed.password is not None else None,
            "host": safe_str(parsed.host) if parsed.host is not None else None,
            "port": parsed.port,
            "path": safe_str(parsed.path) if parsed.path is not None else None,
            "query": safe_str(parsed.query) if parsed.query is not None else None,
            "query_dict": dict(parsed.params) if parsed.params else None,
            "fragment": safe_str(parsed.fragment) if parsed.fragment is not None else None,
            "raw_url": url,
        }
    except Exception as e:
        return {
            "raw_url": url,
            "error": str(e),
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        sys.exit(1)
    
    url = sys.argv[1]
    result = parse_url(url)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
