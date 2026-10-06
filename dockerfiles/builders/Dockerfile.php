FROM php:8.4.19-cli-alpine

# Install jq (for libs.sh), python3 (for the Celery worker), and curl + unzip (for Deno install)
RUN apk add --no-cache jq python3 py3-pip curl unzip

WORKDIR /parsers/php

# Copy parsers.json, utils, and JS parser files
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/php/*.php /parsers/php/

# Make utils executable
RUN chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# Install unzip (required by Composer), git and CA certs then install Composer
RUN apk add --no-cache unzip git ca-certificates && \
	curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install npm dependencies for JS parsers, using the versions pinned in parsers.json
RUN composer init --no-interaction
RUN for f in /parsers/php/*.php; do \
        stem=$(basename "$f" .php | cut -d'-' -f2-); \
        id="php-$stem"; \
        library=$(sh /parsers/extractor.sh "$id" library); \
        version=$(sh /parsers/extractor.sh "$id" version); \
        \
        if echo "$stem" | grep -qiE 'parse-url'; then \
            continue; \
        fi; \
        \
        echo "Installing $library==$version"; \
        composer require "$library:$version"; \
    done

# Create shell wrapper scripts without extension to run the .pl files
RUN for f in /parsers/php/*.php; do \
        name=$(basename "$f" .php); \
        printf '%s\n' "#!/bin/sh" "cd /app/parsers/php 2>/dev/null || cd /parsers/php" "exec php \"$name.php\" \"\$@\"" > /parsers/php/$name; \
        chmod +x /parsers/php/$name; \
    done

# Save the enabled libs to a file for the worker to read at startup
RUN /parsers/libs.sh php > /parsers/worker_parsers.json

# Set up the Celery worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]