FROM debian:bookworm-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq curl xz-utils clang git ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
RUN chmod +x /parsers/extractor.sh /parsers/libs.sh

RUN ZIG_VERSION=$(sh /parsers/extractor.sh "zig-std-uri" version) && \
    curl -fsSL "https://ziglang.org/download/${ZIG_VERSION}/zig-linux-x86_64-${ZIG_VERSION}.tar.xz" | \
    tar -xJ -C /usr/local && \
    ln -sf /usr/local/zig-linux-x86_64-${ZIG_VERSION}/zig /usr/local/bin/zig

COPY parsers/zig/*.zig /parsers/zig/
COPY parsers/zig/build.sh /parsers/zig/build.sh
RUN chmod +x /parsers/zig/build.sh

WORKDIR /build
RUN /parsers/zig/build.sh

RUN /parsers/libs.sh zig > /parsers/worker_parsers.json


# Zig produces statically linked binaries — no runtime libs needed
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /parsers/zig/ /parsers/zig/
COPY --from=builder /parsers/worker_parsers.json /parsers/
COPY --from=builder /parsers/extractor.sh /parsers/
COPY --from=builder /parsers/libs.sh /parsers/

WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]
