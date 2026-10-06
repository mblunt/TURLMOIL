FROM ubuntu:24.04

WORKDIR /parsers/ada

RUN apt-get update && apt-get install -y \
    gnat-14 gprbuild jq python3 python3-pip curl unzip git \
    libssl-dev zlib1g-dev make \
    && rm -rf /var/lib/apt/lists/*

# Symlink every versioned GNAT binary (bare and target-prefixed) so gprbuild/gprbind
# can find gnatbind, x86_64-linux-gnu-gnatbind, etc. by unversioned name.
RUN find /usr/bin \( -name 'gnat*-14' -o -name '*-gnat*-14' -o -name '*-gcc-14' \) \
        -exec sh -c 'ln -sf "$1" "/usr/local/bin/$(basename "${1%-14}")"' _ {} \;

# Install Alire v2.0.1
RUN curl -fsSL https://github.com/alire-project/alire/releases/download/v2.0.1/alr-2.0.1-bin-x86_64-linux.zip \
        -o /tmp/alr.zip && \
    unzip /tmp/alr.zip -d /tmp/alr && \
    mv /tmp/alr/bin/alr /usr/local/bin/ && \
    rm -rf /tmp/alr /tmp/alr.zip

# Configure Alire: disable interactive toolchain assistant so it uses the
# system GNAT detected via PATH without prompting
ENV ALIRE_NONINTERACTIVE=true
RUN alr settings --global --set toolchain.assistant false

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/ada/*.adb /parsers/ada/

RUN chmod +x /parsers/extractor.sh /parsers/libs.sh

# Build each Ada parser as its own Alire binary crate.
# File naming convention: N-lib-name.adb → crate ada_lib_name → procedure Ada_Lib_Name.
# The auto-generated main stub from `alr init` is overwritten with our source.
RUN set -e; \
    for f in /parsers/ada/*.adb; do \
        stem=$(basename "$f" .adb); \
        lib_suffix=$(echo "$stem" | cut -d'-' -f2-); \
        id_key="ada-$lib_suffix"; \
        library=$(sh /parsers/extractor.sh "$id_key" library); \
        proj_name="ada_$(echo "$lib_suffix" | tr '-' '_')"; \
        \
        echo "=== Building $stem ($library) ==="; \
        rm -rf "/build/$proj_name"; \
        mkdir -p /build && cd /build && \
        alr --non-interactive init --bin "$proj_name" && \
        cp "$f" "/build/$proj_name/src/$proj_name.adb" && \
        cd "/build/$proj_name" && \
        alr --non-interactive with "$library" && \
        alr --non-interactive build -- -j0 && \
        cp "bin/$proj_name" "/parsers/ada/$stem" && \
        chmod +x "/parsers/ada/$stem" && \
        rm -rf "/build/$proj_name"; \
    done

RUN /parsers/libs.sh ada > /parsers/worker_parsers.json

WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]
