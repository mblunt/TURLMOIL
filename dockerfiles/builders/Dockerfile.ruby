FROM ruby:4.0.2-alpine3.23

# Install jq (for libs.sh), python3 (for the Celery worker), and curl + unzip (for Deno install)
RUN apk add --no-cache jq python3 py3-pip curl unzip

WORKDIR /parsers/ruby

# Copy parsers.json, utils, and parser files
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/ruby/*.rb /parsers/ruby/

# Make utils executable
RUN chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# Dependency pinning and installation
ENV GEM_HOME=/usr/local/bundle
ENV BUNDLE_PATH=/usr/local/bundle
RUN for f in /parsers/ruby/*.rb; do \
        stem=$(basename "$f" .rb | cut -d'-' -f2-); \
        id="ruby-$stem"; \
        library=$(sh /parsers/extractor.sh "$id" library); \
        version=$(sh /parsers/extractor.sh "$id" version); \
        \
        echo "Installing $library $version"; \
        gem install "$library" -v "$version"; \
    done


# Create shell wrapper scripts without extension to run the .rb files
RUN for f in /parsers/ruby/*.rb; do \
        name=$(basename "$f" .rb); \
        printf '%s\n' "#!/bin/sh" "cd /app/parsers/ruby 2>/dev/null || cd /parsers/ruby" "exec ruby \"$name.rb\" \"\$@\"" > /parsers/ruby/$name; \
        chmod +x /parsers/ruby/$name; \
    done

# Save the enabled libs to a file for the worker to read at startup
RUN /parsers/libs.sh ruby > /parsers/worker_parsers.json

# Set up the Celery worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]