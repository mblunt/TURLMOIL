#!/usr/bin/env java
// Java URL parser using galimatias (WHATWG URL Standard)
//
// Parses URLs using the galimatias library and outputs JSON.
// galimatias implements the WHATWG URL Standard - it normalizes malformed
// input that RFC-strict parsers reject (e.g. http:host -> http://host).

import io.mola.galimatias.URL;
import io.mola.galimatias.GalimatiasParseException;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.HashMap;
import java.util.Map;

public class GalimatiasParser {

    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();

        try {
            URL url = URL.parse(urlStr);

            result.put("scheme", url.scheme() != null && !url.scheme().isEmpty() ? url.scheme() : null);
            result.put("authority", "EXCLUDE");
            result.put("userinfo", "EXCLUDE");
            result.put("username", url.username() != null && !url.username().isEmpty() ? url.username() : null);
            result.put("password", url.password() != null && !url.password().isEmpty() ? url.password() : null);
            result.put("host", url.host() != null ? url.host().toString() : null);
            result.put("port", url.port() != -1 ? String.valueOf(url.port()) : null);
            result.put("path", url.path() != null && !url.path().isEmpty() ? url.path() : null);
            result.put("query", url.query() != null && !url.query().isEmpty() ? url.query() : null);
            result.put("query_dict", "EXCLUDE");
            result.put("fragment", url.fragment() != null && !url.fragment().isEmpty() ? url.fragment() : null);
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
