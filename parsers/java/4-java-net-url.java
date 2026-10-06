#!/usr/bin/env java
// Java URL parser using java.net.URL
//
// Parses URLs using Java's legacy URL class and outputs JSON.
// java.net.URL is protocol-aware and looser than java.net.URI -
// accepts inputs URI rejects, e.g. unencoded characters and relative paths.

import java.net.URL;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.HashMap;
import java.util.Map;

public class JavaNetURLParser {

    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();

        try {
            @SuppressWarnings("deprecation")
            URL url = new URL(urlStr);

            result.put("scheme", url.getProtocol() != null && !url.getProtocol().isEmpty() ? url.getProtocol() : null);
            result.put("authority", "EXCLUDE");
            result.put("userinfo", url.getUserInfo() != null && !url.getUserInfo().isEmpty() ? url.getUserInfo() : null);
            result.put("username", "EXCLUDE");
            result.put("password", "EXCLUDE");
            result.put("host", url.getHost() != null && !url.getHost().isEmpty() ? url.getHost() : null);
            result.put("port", url.getPort() != -1 ? String.valueOf(url.getPort()) : null);
            result.put("path", url.getPath() != null && !url.getPath().isEmpty() ? url.getPath() : null);
            result.put("query", url.getQuery() != null && !url.getQuery().isEmpty() ? url.getQuery() : null);
            result.put("query_dict", "EXCLUDE");
            result.put("fragment", url.getRef() != null && !url.getRef().isEmpty() ? url.getRef() : null);
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
