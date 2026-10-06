FROM dart:3.11.5-sdk

WORKDIR /parsers/dart

# Copying stuff over
COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/dart/*.dart /parsers/dart/

# Make utils executable
RUN apt update && apt install jq python3-pip -y && \
    chmod +x /parsers/extractor.sh && \
    chmod +x /parsers/libs.sh

# # Generate pubspec.yaml from parsers.json and install dependencies
# RUN { \
#       echo "name: dart_parsers"; \
#       echo "description: URI parser implementations for differential fuzzing"; \
#       echo "version: 1.0.0"; \
#       echo "environment:"; \
#       echo "  sdk: '>=3.0.0 <4.0.0'"; \
#       echo "dependencies:"; \
#       jq -r '.parsers[] | select(.language == "dart") | select(.library | startswith("dart:") | not) | "  \(.library): \(.version)"' /parsers/parsers.json; \
#     } > /parsers/dart/pubspec.yaml && \
#     cat /parsers/dart/pubspec.yaml && \
#     cd /parsers/dart && dart pub get

# Create shell wrapper scripts without extension to run the .dart files
RUN chmod +x /parsers/dart/*.dart && \
    for f in /parsers/dart/*.dart; do \
        name=$(basename "$f" .dart); \
        printf '%s\n' "#!/bin/sh" "cd /app/parsers/dart 2>/dev/null || cd /parsers/dart" "exec dart \"$name.dart\" \"\$@\"" > /parsers/dart/$name; \
        chmod +x /parsers/dart/$name; \
    done

# Save the libs to a file for the worker to read
RUN /parsers/libs.sh dart > /parsers/worker_parsers.json

# Set up the worker
WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["python3", "worker.py"]
