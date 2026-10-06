#!/usr/bin/env java
// Java URL parser using Netty QueryStringDecoder
//
// Parses path and query using Netty's HTTP request URI decoder and outputs JSON.
// QueryStringDecoder is designed for request-line URIs, so scheme/host/port/fragment
// are excluded - only path and query parsing behavior is captured.

import io.netty.handler.codec.http.QueryStringDecoder;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NettyParser {

    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();

        try {
            // QueryStringDecoder expects a request-line URI (/path?query), not a full URL.
            // Extract the raw path+query portion via java.net.URI first.
            URI javaUri = new URI(urlStr);
            String pathAndQuery = javaUri.getRawPath() != null ? javaUri.getRawPath() : "";
            if (javaUri.getRawQuery() != null) {
                pathAndQuery += "?" + javaUri.getRawQuery();
            }

            QueryStringDecoder decoder = new QueryStringDecoder(pathAndQuery);

            result.put("scheme", "EXCLUDE");
            result.put("authority", "EXCLUDE");
            result.put("userinfo", "EXCLUDE");
            result.put("username", "EXCLUDE");
            result.put("password", "EXCLUDE");
            result.put("host", "EXCLUDE");
            result.put("port", "EXCLUDE");
            result.put("path", !decoder.rawPath().isEmpty() ? decoder.rawPath() : null);
            result.put("query", javaUri.getRawQuery() != null && !javaUri.getRawQuery().isEmpty() ? javaUri.getRawQuery() : null);

            Map<String, List<String>> params = decoder.parameters();
            result.put("query_dict", params.isEmpty() ? null : new HashMap<>(params));

            result.put("fragment", "EXCLUDE");
            result.put("raw_url", urlStr);

        } catch (Exception e) {
            result.put("error", e.getMessage());
            result.put("raw_url", urlStr);
        }

        return result;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            Map<String, Object> error = new HashMap<>();
            error.put("error", "No URL provided");
            Gson gson = new GsonBuilder().serializeNulls().create();
            System.out.println(gson.toJson(error));
            System.exit(1);
        }

        String url = args[0];
        Map<String, Object> result = parseUrl(url);
        Gson gson = new GsonBuilder().serializeNulls().create();
        System.out.println(gson.toJson(result));
    }
}
