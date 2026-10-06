#!/bin/sh
set -e

mkdir -p /tmp/elixir-logs

# Start each Elixir parser as a long-lived TCP server.
# Ports: numeric prefix + 4000 (1-uri -> 4001, 2-ex_url -> 4002, …)
for escript in /parsers/elixir/*.escript; do
  name=$(basename "$escript" .escript)
  num=$(echo "$name" | grep -o '^[0-9]*')
  port=$((4000 + num))
  "$escript" --server "$port" >"/tmp/elixir-logs/${name}.log" 2>&1 &
  echo "Started Elixir server ${name} on port ${port} (pid $!)"
done

# Wait for each server to accept connections (absorbs BEAM startup ~2-3s)
for escript in /parsers/elixir/*.escript; do
  name=$(basename "$escript" .escript)
  num=$(echo "$name" | grep -o '^[0-9]*')
  port=$((4000 + num))
  i=0
  while ! python3 -c "import socket; socket.create_connection(('127.0.0.1', ${port}), 0.5).close()" 2>/dev/null; do
    i=$((i + 1))
    if [ "$i" -ge 60 ]; then
      echo "ERROR: Elixir server ${name} on port ${port} failed to start" >&2
      echo "--- server log ---" >&2
      cat "/tmp/elixir-logs/${name}.log" >&2
      exit 1
    fi
    sleep 0.5
  done
  echo "Elixir server ${name} ready on port ${port}"
done

exec python3 /app/worker.py
