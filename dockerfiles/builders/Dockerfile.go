FROM golang:1.21-alpine

RUN apk add --no-cache jq python3 py3-pip

WORKDIR /parsers/go

# Copy parsers.json, utils, and Go parser files
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/go/*.go /parsers/go/

# Make utils executable
RUN chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# Build each parser binary
RUN for f in /parsers/go/*.go; do \
        name=$(basename "$f" .go); \
        echo "Building $name"; \
        mkdir -p /build/$name && \
        tail -n +2 "$f" > /build/$name/main.go && \
        cd /build/$name && \
        go mod init $name && \
        go build -o /parsers/go/$name . && \
        chmod +x /parsers/go/$name && \
        cd /parsers/go; \
    done

# Save the enabled libs to a file for the worker to read at startup
RUN /parsers/libs.sh go > /parsers/worker_parsers.json

# Set up the Celery worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]
