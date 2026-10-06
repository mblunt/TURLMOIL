#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <Poco/URI.h>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);
    
    try {
        Poco::URI uri(url_str);
        
        auto set_or_null = [&](const std::string &k, const std::string &v){
            if (v.empty()) result[k] = Json::nullValue; else result[k] = v;
        };

        set_or_null("scheme", uri.getScheme());
        set_or_null("authority", uri.getAuthority());
        set_or_null("userinfo", uri.getUserInfo());
        result["username"] = "EXCLUDE";
        result["password"] = "EXCLUDE";
        set_or_null("host", uri.getHost());
        set_or_null("port", std::to_string(uri.getPort()));
        set_or_null("path", uri.getPath());
        set_or_null("query", uri.getQuery());

        // Convert QueryParameters vector to a multi-value Dictionary
        auto params = uri.getQueryParameters();
        if (params.empty()) {
            result["query_dict"] = Json::nullValue;
        } else {
            Json::Value query_dict(Json::objectValue);
            for (const auto& pair : params) {
                // Ensure every key points to an array of strings
                query_dict[pair.first].append(pair.second);
            }
            result["query_dict"] = query_dict;
        }

        set_or_null("fragment", uri.getFragment());
        result["raw_url"] = url_str;
        
    } catch (const std::exception& e) {
        result["error"] = e.what();
        result["raw_url"] = url_str;
    }
    
    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        Json::Value error(Json::objectValue);
        error["error"] = "No URL provided";
        Json::StreamWriterBuilder w;
        w["indentation"] = ""; // Compact output
        std::cout << Json::writeString(w, error) << std::endl;
        return 1;
    }
    
    std::string url = argv[1];
    Json::Value result = parse_url(url);
    Json::StreamWriterBuilder w;
    w["indentation"] = ""; 
    std::cout << Json::writeString(w, result) << std::endl;
    
    return 0;
}