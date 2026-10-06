#!/usr/bin/env java
// Java URL parser using java.net.URI
//
// Parses URLs using Java's standard library and outputs JSON.

import java.net.URI;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.HashMap;
import java.util.Map;

public class JavaNetURIParser {
    
    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();
        
        try {
            URI uri = new URI(urlStr);
            
            result.put("scheme", uri.getScheme() != null && !uri.getScheme().isEmpty() ? uri.getScheme() : null);
            result.put("authority", "EXCLUDE");
            result.put("userinfo", uri.getUserInfo() != null && !uri.getUserInfo().isEmpty() ? uri.getUserInfo() : null);
            result.put("username", "EXCLUDE");
            result.put("password", "EXCLUDE");
            result.put("host", uri.getHost() != null && !uri.getHost().isEmpty() ? uri.getHost() : null);
            result.put("port", uri.getPort() != -1 ? String.valueOf(uri.getPort()) : null);
            result.put("path", uri.getPath() != null && !uri.getPath().isEmpty() ? uri.getPath() : null);
            result.put("query", uri.getQuery() != null && !uri.getQuery().isEmpty() ? uri.getQuery() : null);
            result.put("query_dict", "EXCLUDE");
            result.put("fragment", uri.getFragment() != null && !uri.getFragment().isEmpty() ? uri.getFragment() : null);
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
