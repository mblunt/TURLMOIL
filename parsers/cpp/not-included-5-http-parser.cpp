#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <sstream>
#include "http_parser.h"
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);
    
    struct http_parser_url u;
    http_parser_url_init(&u);
    
    // Parse the URL
    int parse_result = http_parser_parse_url(url_str.c_str(), url_str.length(), 0, &u);
    
    if (parse_result != 0) {
        result["error"] = "Failed to parse URL";
        result["raw_url"] = url_str;
        return result;
    }
    
    auto get_field_str = [&](http_parser_url_fields field) -> std::string {
        if (u.field_set & (1 << field)) {
            return url_str.substr(u.field_data[field].off, u.field_data[field].len);
        }
        return "";
    };

    std::string scheme = get_field_str(UF_SCHEMA);
    std::string userinfo = get_field_str(UF_USERINFO);
    std::string host = get_field_str(UF_HOST);
    std::string port = (u.field_set & (1 << UF_PORT)) ? std::to_string(u.port) : "";
    std::string path = get_field_str(UF_PATH);
    std::string query = get_field_str(UF_QUERY);
    std::string fragment = get_field_str(UF_FRAGMENT);

    // Map to JSON result
    result["scheme"] = scheme.empty() ? Json::nullValue : scheme;
    result["authority"] = "EXCLUDE";
    result["userinfo"] = userinfo.empty() ? Json::nullValue : userinfo;
    result["username"] = "EXCLUDE";
    result["password"] = "EXCLUDE";
    result["host"] = host.empty() ? Json::nullValue : host;
    result["port"] = port.empty() ? Json::nullValue : port;
    result["path"] = path.empty() ? Json::nullValue : path;
    result["query"] = query.empty() ? Json::nullValue : query;
    result["query_dict"] = "EXCLUDE";
    result["fragment"] = fragment.empty() ? Json::nullValue : fragment;
    result["raw_url"] = url_str;
    
    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        Json::Value error(Json::objectValue);
        error["error"] = "No URL provided";
        Json::StreamWriterBuilder writer;
        writer["indentation"] = "";
        std::cout << Json::writeString(writer, error) << std::endl;
        return 1;
    }
    
    std::string url = argv[1];
    Json::Value result = parse_url(url);
    
    Json::StreamWriterBuilder writer;
    writer["indentation"] = "";
    std::cout << Json::writeString(writer, result) << std::endl;
    
    return 0;
}