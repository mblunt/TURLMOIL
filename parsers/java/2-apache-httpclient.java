#!/usr/bin/env java
// Java URL parser using Apache HttpClient URIBuilder
//
// Parses URLs using Apache HttpClient library and outputs JSON.

import org.apache.http.client.utils.URIBuilder;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class ApacheHttpClientParser {
    
    public static Map<String, Object> parseUrl(String urlStr) {
        Map<String, Object> result = new HashMap<>();
        
        try {
            URIBuilder builder = new URIBuilder(urlStr);
            
            result.put("scheme", builder.getScheme());
            result.put("authority", "EXCLUDE"); 
            result.put("userinfo", builder.getUserInfo());
            result.put("username", "EXCLUDE");
            result.put("password", "EXCLUDE");
            result.put("host", builder.getHost());
            result.put("port", builder.getPort() != -1 ? String.valueOf(builder.getPort()) : null);
            result.put("path", builder.getPath());
            result.put("query", (builder.getQueryParams().isEmpty()) ? null : builder.build().getRawQuery());
            
            // HANDLE DUPLICATES: Map keys to a List of values
            Map<String, List<String>> queryDict = new HashMap<>();
            for (org.apache.http.NameValuePair pair : builder.getQueryParams()) {
                queryDict.computeIfAbsent(pair.getName(), k -> new java.util.ArrayList<>())
                        .add(pair.getValue());
            }
            
            result.put("query_dict", queryDict.isEmpty() ? null : queryDict);
            result.put("fragment", builder.getFragment());
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
