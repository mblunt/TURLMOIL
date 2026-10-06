FROM perl:5.42.1-slim-bookworm

# Install jq (for libs.sh), python3 (for the Celery worker), and curl + unzip (for Deno install)
RUN apt-get update && apt-get install -y jq python3 python3-pip curl unzip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /parsers/perl

# Copy parsers.json, utils, and JS parser files
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/perl/*.pl /parsers/perl/

# Make utils executable
RUN chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# Install CPAN modules
RUN cpan install JSON
RUN for f in /parsers/perl/*.pl; do \
        stem=$(basename "$f" .pl | cut -d'-' -f2-); \
        id="perl-$stem"; \
        library=$(sh /parsers/extractor.sh "$id" library); \
        version=$(sh /parsers/extractor.sh "$id" version); \
        \
        echo "Installing $library==$version"; \
        cpan install "$library-$version.tar.gz"; \
    done

# Create shell wrapper scripts without extension to run the .pl files
RUN for f in /parsers/perl/*.pl; do \
        name=$(basename "$f" .pl); \
        printf '%s\n' "#!/bin/sh" "cd /app/parsers/perl 2>/dev/null || cd /parsers/perl" "exec perl \"$name.pl\" \"\$@\"" > /parsers/perl/$name; \
        chmod +x /parsers/perl/$name; \
    done

# Save the enabled libs to a file for the worker to read at startup
RUN /parsers/libs.sh perl > /parsers/worker_parsers.json

# Set up the Celery worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]