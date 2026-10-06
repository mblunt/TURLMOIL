FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jdk maven jq python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /parsers/java

COPY parsers/parsers.json /parsers/
COPY parsers/utils/* /parsers/
COPY parsers/java/*.java /parsers/java/
COPY parsers/java/client.py /parsers/java/
COPY parsers/java/entrypoint.sh /parsers/java/

RUN chmod +x /parsers/extractor.sh /parsers/libs.sh /parsers/java/entrypoint.sh

# Download all JAR dependencies via Maven
RUN OKHTTP_VERSION=$(sh /parsers/extractor.sh "java-okhttp" version) && \
    HC_VERSION=$(sh /parsers/extractor.sh "java-apache-httpclient" version) && \
    SPRING_VERSION=$(sh /parsers/extractor.sh "java-spring-web" version) && \
    GALIMATIAS_VERSION=$(sh /parsers/extractor.sh "java-galimatias" version) && \
    NETTY_VERSION=$(sh /parsers/extractor.sh "java-netty" version) && \
    mkdir -p /parsers/java/lib /tmp/mvn-deps && \
    printf '<project><modelVersion>4.0.0</modelVersion><groupId>p</groupId><artifactId>p</artifactId><version>1</version><dependencies>\
<dependency><groupId>com.squareup.okhttp3</groupId><artifactId>okhttp</artifactId><version>%s</version></dependency>\
<dependency><groupId>org.apache.httpcomponents</groupId><artifactId>httpclient</artifactId><version>%s</version></dependency>\
<dependency><groupId>com.google.code.gson</groupId><artifactId>gson</artifactId><version>2.10.1</version></dependency>\
<dependency><groupId>org.springframework</groupId><artifactId>spring-web</artifactId><version>%s</version></dependency>\
<dependency><groupId>io.mola.galimatias</groupId><artifactId>galimatias</artifactId><version>%s</version></dependency>\
<dependency><groupId>io.netty</groupId><artifactId>netty-codec-http</artifactId><version>%s</version></dependency>\
</dependencies></project>' \
        "$OKHTTP_VERSION" "$HC_VERSION" "$SPRING_VERSION" "$GALIMATIAS_VERSION" "$NETTY_VERSION" \
        > /tmp/mvn-deps/pom.xml && \
    mvn --batch-mode -f /tmp/mvn-deps/pom.xml dependency:copy-dependencies \
        -DoutputDirectory=/parsers/java/lib && \
    rm -rf /tmp/mvn-deps ~/.m2

# Compile all parsers + Server together (strip #! shebang lines first)
RUN mkdir -p /parsers/java/classes /tmp/java-src && \
    for f in /parsers/java/*.java; do \
        classname=$(grep -oP 'public class \K\w+' "$f"); \
        # Server.java has no shebang — copy as-is; parser files strip the first line
        if [ "$classname" = "Server" ]; then \
            cp "$f" /tmp/java-src/Server.java; \
        else \
            tail -n +2 "$f" > /tmp/java-src/${classname}.java; \
        fi; \
    done && \
    javac -encoding UTF-8 -cp '/parsers/java/lib/*' \
          -d /parsers/java/classes /tmp/java-src/*.java && \
    rm -rf /tmp/java-src

# Generate shell wrappers: each calls client.py with the assigned port
RUN for f in /parsers/java/*.java; do \
        name=$(basename "$f" .java); \
        num=$(echo "$name" | grep -o '^[0-9]*'); \
        [ -z "$num" ] && continue; \
        port=$((5000 + num)); \
        printf '%s\n' "#!/bin/sh" \
            "exec python3 /parsers/java/client.py ${port} \"\$1\"" \
            > /parsers/java/$name; \
        chmod +x /parsers/java/$name; \
    done

RUN /parsers/libs.sh java > /parsers/worker_parsers.json

WORKDIR /app
COPY distributed/requirements.txt /app/
RUN pip3 install -r requirements.txt --break-system-packages
COPY distributed/core/ /app/core/
COPY distributed/registry/ /app/registry/
COPY distributed/tasks/ /app/tasks/
COPY distributed/worker.py /app/

CMD ["/parsers/java/entrypoint.sh"]
