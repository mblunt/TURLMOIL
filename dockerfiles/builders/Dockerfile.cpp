FROM ubuntu:24.04 AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential cmake git ca-certificates curl pkg-config jq \
        libboost-all-dev \
        libcurl4-openssl-dev \
        liburiparser-dev \
        libglib2.0-dev \
        libjsoncpp-dev \
        qt6-base-dev \
    && rm -rf /var/lib/apt/lists/*

COPY parsers/parsers.json /parsers/
COPY parsers/utils/extractor.sh /parsers/
COPY parsers/cpp/ /parsers/cpp/

# Download single-header / single-file dependencies
RUN chmod +x /parsers/extractor.sh \
    \
    && ADA_VERSION=$(sh /parsers/extractor.sh "cpp-ada-url" version) \
    && curl -fsSL "https://github.com/ada-url/ada/releases/download/v${ADA_VERSION}/ada.cpp" \
            -o /parsers/cpp/ada.cpp \
    && curl -fsSL "https://github.com/ada-url/ada/releases/download/v${ADA_VERSION}/ada.h" \
            -o /parsers/cpp/ada.h \
    \
    && HTTP_PARSER_VERSION=$(sh /parsers/extractor.sh "cpp-http-parser" version) \
    && curl -fsSL "https://raw.githubusercontent.com/nodejs/http-parser/v${HTTP_PARSER_VERSION}/http_parser.h" \
            -o /parsers/cpp/http_parser.h \
    && curl -fsSL "https://raw.githubusercontent.com/nodejs/http-parser/v${HTTP_PARSER_VERSION}/http_parser.c" \
            -o /parsers/cpp/http_parser.c \
    \
    && URL_C_COMMIT=$(sh /parsers/extractor.sh "cpp-url-c-rfc" version) \
    && curl -fsSL "https://raw.githubusercontent.com/cozis/url.c/${URL_C_COMMIT}/url.c" \
            -o /parsers/cpp/url.c \
    && curl -fsSL "https://raw.githubusercontent.com/cozis/url.c/${URL_C_COMMIT}/url.h" \
            -o /parsers/cpp/url.h

# Build Poco from source (takes longest — own layer for cache)
RUN POCO_VERSION=$(sh /parsers/extractor.sh "cpp-poco-uri" version) \
    && curl -fsSL "https://github.com/pocoproject/poco/archive/refs/tags/poco-${POCO_VERSION}-release.tar.gz" \
            | tar -xz -C /tmp \
    && cmake -S "/tmp/poco-poco-${POCO_VERSION}-release" -B /tmp/poco-build \
             -DCMAKE_BUILD_TYPE=Release \
             -DENABLE_TESTS=OFF -DENABLE_SAMPLES=OFF \
             -DENABLE_FOUNDATION=ON -DENABLE_NET=ON -DENABLE_UTIL=OFF \
             -DENABLE_XML=OFF -DENABLE_JSON=OFF -DENABLE_MONGODB=OFF \
             -DENABLE_DATA=OFF -DENABLE_CRYPTO=OFF -DENABLE_NETSSL=OFF \
    && cmake --build /tmp/poco-build --parallel "$(nproc)" \
    && cmake --install /tmp/poco-build --prefix /usr/local \
    && ldconfig \
    && rm -rf /tmp/poco-build "/tmp/poco-poco-${POCO_VERSION}-release"

# Compile all parsers
RUN g++ -O2 -std=c++17 /parsers/cpp/1-boost-url.cpp \
           -lboost_url -lboost_json \
           -o /parsers/cpp/1-boost-url \
    && g++ -O2 -std=c++20 /parsers/cpp/2-ada-url.cpp \
           -lboost_json \
           -o /parsers/cpp/2-ada-url \
    && g++ -O2 -std=c++17 /parsers/cpp/3-poco-uri.cpp \
           -lPocoFoundation -lPocoNet \
           $(pkg-config --cflags --libs jsoncpp) \
           -o /parsers/cpp/3-poco-uri \
    && g++ -O2 -std=c++17 /parsers/cpp/4-libcurl.cpp \
           $(pkg-config --cflags --libs libcurl jsoncpp) \
           -o /parsers/cpp/4-libcurl \
    && g++ -O2 -std=c++17 /parsers/cpp/5-http-parser.cpp /parsers/cpp/http_parser.c \
           $(pkg-config --cflags --libs jsoncpp) \
           -o /parsers/cpp/5-http-parser \
    && g++ -O2 -std=c++17 /parsers/cpp/6-uriparser.cpp \
           $(pkg-config --cflags --libs liburiparser jsoncpp) \
           -o /parsers/cpp/6-uriparser \
    && gcc -O2 -c /parsers/cpp/url.c -o /parsers/cpp/url.o \
    && g++ -O2 -std=c++17 /parsers/cpp/7-url-c-rfc.cpp /parsers/cpp/url.o \
           $(pkg-config --cflags --libs jsoncpp) \
           -o /parsers/cpp/7-url-c-rfc \
    && g++ -O2 -std=c++17 /parsers/cpp/8-url-c-whatwg.cpp /parsers/cpp/url.o \
           $(pkg-config --cflags --libs jsoncpp) \
           -o /parsers/cpp/8-url-c-whatwg \
    && g++ -O2 -std=c++17 /parsers/cpp/9-qurl-tolerant.cpp \
           $(pkg-config --cflags --libs Qt6Core jsoncpp) -fPIC \
           -o /parsers/cpp/9-qurl-tolerant \
    && g++ -O2 -std=c++17 /parsers/cpp/10-qurl-strict.cpp \
           $(pkg-config --cflags --libs Qt6Core jsoncpp) -fPIC \
           -o /parsers/cpp/10-qurl-strict \
    && g++ -O2 -std=c++17 /parsers/cpp/11-guri.cpp \
           $(pkg-config --cflags --libs glib-2.0 jsoncpp) \
           -o /parsers/cpp/11-guri


# ── Runtime image ────────────────────────────────────────────────────────────
FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        jq python3 python3-pip \
        libboost-url1.83.0 libboost-json1.83.0 \
        libcurl4t64 \
        liburiparser1 \
        libglib2.0-0 \
        libjsoncpp25 \
        libqt6core6 \
    && rm -rf /var/lib/apt/lists/*

# Copy Poco runtime libs from builder (not in Ubuntu repos at the right version)
COPY --from=builder /usr/local/lib/libPoco*.so* /usr/local/lib/
RUN ldconfig

COPY --from=builder /parsers/cpp/1-boost-url \
                    /parsers/cpp/2-ada-url \
                    /parsers/cpp/3-poco-uri \
                    /parsers/cpp/4-libcurl \
                    /parsers/cpp/5-http-parser \
                    /parsers/cpp/6-uriparser \
                    /parsers/cpp/7-url-c-rfc \
                    /parsers/cpp/8-url-c-whatwg \
                    /parsers/cpp/9-qurl-tolerant \
                    /parsers/cpp/10-qurl-strict \
                    /parsers/cpp/11-guri \
                    /parsers/cpp/

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/

COPY distributed/requirements.txt /app/
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

RUN chmod +x /parsers/extractor.sh /parsers/libs.sh \
    && /parsers/libs.sh cpp > /parsers/worker_parsers.json \
    && pip3 install -r /app/requirements.txt --break-system-packages \
    && rm -rf /root/.cache/pip

WORKDIR /app
CMD ["python3", "worker.py"]
