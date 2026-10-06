#!/usr/bin/env python3
"""TCP client for Elixir parser servers."""
import socket
import sys
import json


def main():
    port = int(sys.argv[1])
    url = sys.argv[2]
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=10) as s:
            s.sendall(url.encode() + b"\n")
            data = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
                if b"\n" in data:
                    break
            print(data.decode().strip())
    except Exception as e:
        print(json.dumps({"error": str(e), "raw_url": url}))


main()
