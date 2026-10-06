FROM node:25.8.2-bookworm-slim

# Install jq (for libs.sh), python3 (for the Celery worker), and curl + unzip (for Deno install)
RUN apt-get update && apt-get install -y jq python3 python3-pip curl unzip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /parsers/javascript

# Copy parsers.json, utils, and JS parser files
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/javascript/*.js /parsers/javascript/

# Make utils executable
RUN chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# Install Deno at the version pinned in parsers.json
RUN DENO_VERSION=v$(/parsers/extractor.sh "javascript-deno" version) && \
    curl -fsSL https://deno.land/x/install/install.sh | DENO_VERSION="v${DENO_VERSION}" sh && \
    mv /root/.deno/bin/deno /usr/local/bin/deno

# Install npm dependencies for JS parsers, using the versions pinned in parsers.json
RUN for f in /parsers/javascript/*.js; do \
        stem=$(basename "$f" .js | cut -d'-' -f2-); \
        id="javascript-$stem"; \
        library=$(sh /parsers/extractor.sh "$id" library); \
        version=$(sh /parsers/extractor.sh "$id" version); \
        \
        if echo "$stem" | grep -qiE 'deno|whatwg|legacy'; then \
            continue; \
        fi; \
        \
        echo "Installing $library==$version"; \
        npm install "$library@$version"; \
    done

# Create shell wrapper scripts without extension: use `deno run` for deno parsers, `node` otherwise
RUN for f in /parsers/javascript/*.js; do \
        name=$(basename "$f" .js); \
        if echo "$name" | grep -qi deno; then \
            printf '%s\n' "#!/bin/sh" "cd /app/parsers/javascript 2>/dev/null || cd /parsers/javascript" "exec deno run --no-check --allow-read --allow-net \"$name.js\" \"\$@\"" > /parsers/javascript/$name; \
        else \
            printf '%s\n' "#!/bin/sh" "cd /app/parsers/javascript 2>/dev/null || cd /parsers/javascript" "exec node \"$name.js\" \"\$@\"" > /parsers/javascript/$name; \
        fi; \
        chmod +x /parsers/javascript/$name; \
    done

# Save the enabled libs to a file for the worker to read at startup
RUN /parsers/libs.sh javascript > /parsers/worker_parsers.json

# Set up the Celery worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]