FROM ubuntu:24.04 AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq python3-pip r-base build-essential \
    libcurl4-openssl-dev libssl-dev libxml2-dev libfontconfig1-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /parsers/r

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/r/*.r /parsers/r/

RUN chmod +x /parsers/extractor.sh /parsers/libs.sh

ENV R_LIBS_USER=/usr/local/lib/R/site-library

RUN Rscript -e "install.packages(c('remotes', 'jsonlite'), repos = 'https://cloud.r-project.org', lib = '/usr/local/lib/R/site-library')"
RUN for f in /parsers/r/*.r; do \
        library=$(basename "$f" .r | cut -d'-' -f2-); \
        version=$(sh /parsers/extractor.sh "r-$library" version); \
        echo "=== Installing $library==$version ==="; \
        if [ -n "$library" ] && [ -n "$version" ] && [ "$version" != "null" ]; then \
            Rscript -e " \
                tryCatch( \
                    remotes::install_version('$library', version='$version', repos='https://cloud.r-project.org', lib='/usr/local/lib/R/site-library', upgrade='never'), \
                    error=function(e) { cat('FAILED: ', conditionMessage(e), '\n'); quit(status=1) } \
                )" || exit 1; \
        fi; \
    done

RUN chmod +x /parsers/r/*.r && \
    for f in /parsers/r/*.r; do \
        name=$(basename "$f" .r); \
        printf '%s\n' "#!/bin/sh" "cd /app/parsers/r 2>/dev/null || cd /parsers/r" "exec Rscript \"$name.r\" \"\$@\"" > /parsers/r/$name; \
        chmod +x /parsers/r/$name; \
    done

RUN /parsers/libs.sh r > /parsers/worker_parsers.json


FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq python3-pip r-base libcurl4 libssl3 libxml2 && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
           /usr/share/info /usr/share/locale

# Copy installed R packages from builder (both site-library paths), then strip artifacts
COPY --from=builder /usr/local/lib/R/site-library/ /usr/local/lib/R/site-library/
COPY --from=builder /usr/lib/R/site-library/ /usr/lib/R/site-library/
RUN find /usr/local/lib/R/site-library -type d -name 'tests' -exec rm -rf {} + 2>/dev/null || true && \
    find /usr/local/lib/R/site-library -type d -name 'doc'   -exec rm -rf {} + 2>/dev/null || true && \
    find /usr/local/lib/R/site-library -name '*.o' -delete 2>/dev/null || true

COPY --from=builder /parsers/r/ /parsers/r/
COPY --from=builder /parsers/worker_parsers.json /parsers/
COPY --from=builder /parsers/extractor.sh /parsers/
COPY --from=builder /parsers/libs.sh /parsers/

WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages && \
    rm -rf /root/.cache/pip
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/


CMD ["python3", "worker.py"]
