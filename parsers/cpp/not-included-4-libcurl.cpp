#include <iostream>
#include <string>
#include <vector>
#include <curl/curl.h>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);
    CURLU *url_handle = curl_url();
    
    if (!url_handle) {
        result["error"] = "Failed to create URL handle";
        result["raw_url"] = url_str;
        return result;
    }
    
    CURLUcode rc = curl_url_set(url_handle, CURLUPART_URL, url_str.c_str(), 0);
    if (rc != CURLUE_OK) {
        result["error"] = curl_url_strerror(rc);
        result["raw_url"] = url_str;
        curl_url_cleanup(url_handle);
        return result;
    }

    auto get_part_str = [&](CURLUPart part) -> std::string {
        char *content;
        if (curl_url_get(url_handle, part, &content, 0) == CURLUE_OK && content) {
            std::string s(content);
            curl_free(content);
            return s;
        }
        return "";
    };

    // 1. Get Base Components
    std::string scheme = get_part_str(CURLUPART_SCHEME);
    std::string user = get_part_str(CURLUPART_USER);
    std::string pass = get_part_str(CURLUPART_PASSWORD);
    std::string host = get_part_str(CURLUPART_HOST);
    std::string port = get_part_str(CURLUPART_PORT);
    std::string path = get_part_str(CURLUPART_PATH);
    std::string query = get_part_str(CURLUPART_QUERY);
    std::string fragment = get_part_str(CURLUPART_FRAGMENT);

    Json::Value query_dict(Json::objectValue);
    char *query_part;
    // CURLU_QUERYARRAY iterates through individual key=value pairs
    CURLUcode q_rc = curl_url_get(url_handle, CURLUPART_QUERY, &query_part, CURLU_QUERYARRAY);
    
    while(q_rc == CURLUE_OK) {
        std::string pair(query_part);
        curl_free(query_part);
        
        size_t pos = pair.find('=');
        std::string k = (pos != std::string::npos) ? pair.substr(0, pos) : pair;
        std::string v = (pos != std::string::npos) ? pair.substr(pos + 1) : "";
        
        query_dict[k].append(v);
        q_rc = curl_url_get(url_handle, CURLUPART_QUERY, &query_part, CURLU_QUERYARRAY);
    }

    // Map to JSON
    result["scheme"] = scheme.empty() ? Json::nullValue : scheme;
    result["authority"] = "EXCLUDE";
    result["userinfo"] = "EXCLUDE";
    result["username"] = user.empty() ? Json::nullValue : user;
    result["password"] = pass.empty() ? Json::nullValue : pass;
    result["host"] = host.empty() ? Json::nullValue : host;
    result["port"] = port.empty() ? Json::nullValue : port;
    result["path"] = path.empty() ? Json::nullValue : path;
    result["query"] = query.empty() ? Json::nullValue : query;
    result["query_dict"] = query_dict.empty() ? Json::nullValue : query_dict;
    result["fragment"] = fragment.empty() ? Json::nullValue : fragment;
    result["raw_url"] = url_str;

    curl_url_cleanup(url_handle);
    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        Json::Value error;
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