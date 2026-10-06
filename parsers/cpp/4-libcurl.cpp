#include <iostream>
#include <string>
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
        char *content = nullptr;
        if (curl_url_get(url_handle, part, &content, 0) == CURLUE_OK && content) {
            std::string s(content);
            curl_free(content);
            return s;
        }
        return "";
    };

    auto set_or_null = [&](const char* k, const std::string& v) {
        if (v.empty()) result[k] = Json::Value(Json::nullValue);
        else result[k] = v;
    };

    std::string scheme   = get_part_str(CURLUPART_SCHEME);
    std::string user     = get_part_str(CURLUPART_USER);
    std::string pass     = get_part_str(CURLUPART_PASSWORD);
    std::string host     = get_part_str(CURLUPART_HOST);
    std::string port     = get_part_str(CURLUPART_PORT);
    std::string path     = get_part_str(CURLUPART_PATH);
    std::string query    = get_part_str(CURLUPART_QUERY);
    std::string fragment = get_part_str(CURLUPART_FRAGMENT);

    set_or_null("scheme",    scheme);
    result["authority"] = "EXCLUDE";
    result["userinfo"]  = "EXCLUDE";
    set_or_null("username",  user);
    set_or_null("password",  pass);
    set_or_null("host",      host);
    set_or_null("port",      port);
    set_or_null("path",      path);
    set_or_null("query",     query);
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment",  fragment);
    result["raw_url"] = url_str;

    curl_url_cleanup(url_handle);
    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        Json::Value e(Json::objectValue);
        e["error"] = "No URL provided";
        Json::StreamWriterBuilder w; w["indentation"] = "";
        std::cout << Json::writeString(w, e) << std::endl;
        return 1;
    }
    Json::Value result = parse_url(argv[1]);
    Json::StreamWriterBuilder w; w["indentation"] = "";
    std::cout << Json::writeString(w, result) << std::endl;
    return 0;
}
