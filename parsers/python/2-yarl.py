#!/usr/bin/env python3
"""Python URL parser using yarl.

Parses URLs using yarl and outputs JSON.
"""

import sys
import json
from yarl import URL

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
    try:
        parsed = URL(url)
        
        
        result = {
            "scheme": parsed.scheme or None,
            "authority": parsed.authority or None,
            "userinfo": "EXCLUDE",  # yarl does not provide userinfo
            "username": parsed.user or None,
            "password": parsed.password or None,
            "host": parsed.host or None,
            "port": str(parsed.port) if parsed.port is not None else None,
            "path": parsed.path or None,
            "query": parsed.query_string or None,
            "query_dict": dict(parsed.query.items()) if parsed.query else None,
            "fragment": parsed.fragment or None,
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
