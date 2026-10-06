#!/usr/bin/env java
// Java URL parser using OkHttp HttpUrl
//
// Parses URLs using OkHttp library and outputs JSON.

import okhttp3.HttpUrl;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.HashMap;
import java.util.Map;

public class OkHttpParser {
    
    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();
        
        try {
            HttpUrl url = HttpUrl.parse(urlStr);
            
            if (url == null) {
                result.put("error", "Failed to parse URL");
                result.put("raw_url", urlStr);
                return result;
            }
            
            result.put("scheme", url.scheme() != null && !url.scheme().isEmpty() ? url.scheme() : null);
            result.put("authority", "EXCLUDE");
            result.put("userinfo", "EXCLUDE");
            result.put("username", url.username() != null && !url.username().isEmpty() ? url.username() : null);
            result.put("password", url.password() != null && !url.password().isEmpty() ? url.password() : null);
            result.put("host", url.host() != null && !url.host().isEmpty() ? url.host() : null);
            result.put("port", url.port() != 80 && url.port() != 443 ? String.valueOf(url.port()) : null);
            result.put("path", url.encodedPath() != null && !url.encodedPath().isEmpty() ? url.encodedPath() : null);
            result.put("query", url.encodedQuery() != null && !url.encodedQuery().isEmpty() ? url.encodedQuery() : null);
            result.put("query_dict", "EXCLUDE"); // Exclude these because the client API allows you to extract values as a list or as individual parameters
            result.put("fragment", url.encodedFragment() != null && !url.encodedFragment().isEmpty() ? url.encodedFragment() : null);
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
