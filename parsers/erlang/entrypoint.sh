#!/bin/sh
set -e

mkdir -p /tmp/erlang-logs

# Start each Erlang parser as a long-lived TCP server.
# Ports: numeric prefix + 6000 (1-uri-string -> 6001, 2-hackney-url -> 6002, …)
for f in /parsers/erlang/*.erl; do
  name=$(basename "$f" .erl)
  num=$(echo "$name" | grep -o '^[0-9]*')
  [ -z "$num" ] && continue
  port=$((6000 + num))
  escript "$f" --server "$port" >"/tmp/erlang-logs/${name}.log" 2>&1 &
  echo "Started Erlang server ${name} on port ${port} (pid $!)"
done

# Wait for each server to accept connections (absorbs BEAM startup ~1-2s)
for f in /parsers/erlang/*.erl; do
  name=$(basename "$f" .erl)
  num=$(echo "$name" | grep -o '^[0-9]*')
  [ -z "$num" ] && continue
  port=$((6000 + num))
  i=0
  while ! python3 -c "import socket; socket.create_connection(('127.0.0.1', ${port}), 0.5).close()" 2>/dev/null; do
    i=$((i + 1))
    if [ "$i" -ge 60 ]; then
      echo "ERROR: Erlang server ${name} on port ${port} failed to start" >&2
      cat "/tmp/erlang-logs/${name}.log" >&2
      exit 1
    fi
    sleep 0.5
  done
  echo "Erlang server ${name} ready on port ${port}"
done

exec python3 /app/worker.py
