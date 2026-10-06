#!/usr/bin/env python3
"""Python URL parser using furl.

Parses URLs using furl and outputs JSON.
"""

import sys
import json
from furl import furl

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
    try:
        parsed = furl(url)
        
        result = {
            "scheme": str(parsed.scheme) if parsed.scheme else None,
            "authority": str(parsed.netloc) if parsed.netloc else None,
            "userinfo": "EXCLUDE",  # furl does not provide userinfo directly
            "username": str(parsed.username) if parsed.username else None,
            "password": str(parsed.password) if parsed.password else None,
            "host": str(parsed.host) if parsed.host else None,
            "port": str(parsed.port) if parsed.port is not None else None,
            "path": str(parsed.pathstr) if parsed.pathstr else None,
            "query": str(parsed.querystr) if parsed.querystr else None,
            "query_dict": dict(parsed.args) if parsed.args else None,
            "fragment": str(parsed.fragment) if parsed.fragment else None,
            "raw_url": url,
        }
        
        return result
        
    except Exception as e:
        return {
            "error": str(e),
            "raw_url": url,
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
