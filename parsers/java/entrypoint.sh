#!/bin/sh
set -e

mkdir -p /tmp/java-logs

# Start each Java parser as a long-lived TCP server.
# Ports: numeric prefix + 5000 (1-okhttp -> 5001, 2-apache -> 5002, …)
for f in /parsers/java/*.java; do
  name=$(basename "$f" .java)
  num=$(echo "$name" | grep -o '^[0-9]*')
  [ -z "$num" ] && continue
  port=$((5000 + num))
  java -cp '/parsers/java/lib/*:/parsers/java/classes' Server "$port" "$num" \
    >"/tmp/java-logs/${name}.log" 2>&1 &
  echo "Started Java parser ${name} on port ${port} (pid $!)"
done

# Wait for each server to accept connections (absorbs JVM startup)
for f in /parsers/java/*.java; do
  name=$(basename "$f" .java)
  num=$(echo "$name" | grep -o '^[0-9]*')
  [ -z "$num" ] && continue
  port=$((5000 + num))
  i=0
  while ! python3 -c "import socket; socket.create_connection(('127.0.0.1', ${port}), 0.5).close()" 2>/dev/null; do
    i=$((i + 1))
    if [ "$i" -ge 120 ]; then
      echo "ERROR: Java parser ${name} on port ${port} failed to start" >&2
      cat "/tmp/java-logs/${name}.log" >&2
      exit 1
    fi
    sleep 0.5
  done
  echo "Java parser ${name} ready on port ${port}"
done

exec python3 /app/worker.py
