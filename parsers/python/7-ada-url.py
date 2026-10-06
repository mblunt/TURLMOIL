#!/usr/bin/env python3
import sys
import json
from ada_url import parse_url as _ada_parse_url
from ada_url import parse_search_params


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
        parsed = _ada_parse_url(url)
        
        result = {
            "scheme": parsed.get("protocol") or None,
            "authority": "EXCLUDE",
            "userinfo": "EXCLUDE",  # urllib.parse does not provide userinfo directly
            "username": parsed.get("username") or None,
            "password": parsed.get("password") or None,
            "host": parsed.get("host") or None,
            "port": str(parsed.get("port")) if parsed.get("port") is not None else None,
            "path": parsed.get("pathname") or None,
            "query": parsed.get("search") or None,
            "query_dict": parse_search_params(parsed.get("search")) if parsed.get("search") else None,
            "fragment": parsed.get("hash") or None,
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
