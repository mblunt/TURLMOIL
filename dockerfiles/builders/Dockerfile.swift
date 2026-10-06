FROM swift:5.9 AS builder

RUN apt-get update && apt-get install -y --no-install-recommends jq && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /parsers/swift

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/swift/*.swift /parsers/swift/

RUN chmod +x /parsers/extractor.sh /parsers/libs.sh

RUN for f in /parsers/swift/*.swift; do \
        stem=$(basename "$f" .swift); \
        if [ "$stem" = "3-weburl" ]; then continue; fi; \
        echo "=== Compiling $stem ==="; \
        swiftc "$f" -o /parsers/swift/$stem; \
    done

WORKDIR /build/weburl-parser
RUN mkdir -p Sources/weburl-parser && \
    cat > Package.swift <<'EOF'
// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "weburl-parser",
    dependencies: [
        .package(url: "https://github.com/karwa/swift-url", exact: "0.4.2")
    ],
    targets: [
        .executableTarget(
            name: "weburl-parser",
            dependencies: [
                .product(name: "WebURL", package: "swift-url")
            ]
        )
    ]
)
EOF

RUN cp /parsers/swift/3-weburl.swift Sources/weburl-parser/main.swift && \
    swift build -c release && \
    cp "$(swift build -c release --show-bin-path)/weburl-parser" /parsers/swift/3-weburl

RUN /parsers/libs.sh swift > /parsers/worker_parsers.json


# swift:5.9 is Ubuntu 22.04 — use the same OS so the Swift runtime libs match
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the Swift runtime shared libraries — compiler toolchain stays behind
COPY --from=builder /usr/lib/swift/linux/ /usr/lib/swift/linux/
COPY --from=builder /usr/lib/libswift*.so* /usr/lib/
COPY --from=builder /parsers/swift/ /parsers/swift/
COPY --from=builder /parsers/worker_parsers.json /parsers/
COPY --from=builder /parsers/extractor.sh /parsers/
COPY --from=builder /parsers/libs.sh /parsers/

WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]
