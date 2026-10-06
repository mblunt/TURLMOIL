#include <iostream>
#include <string>
#include <vector>
#include <json/json.h>

extern "C" {
#include "url.h"
}

static std::string url_string_to_str(const URL_String& s) {
    if (!s.ptr || s.len <= 0) return "";
    return std::string(s.ptr, s.len);
}

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    std::vector<char> buf(url_str.begin(), url_str.end());

    URL url;
    int cur = 0;
    // flags = 0 → WHATWG mode (no URL_FLAG_RFC3986)
    int ret = url_parse(buf.data(), (int)buf.size(), &cur, &url, 0);

    if (ret < 0) {
        result["error"] = "parse error";
        result["raw_url"] = url_str;
        return result;
    }

    auto set_or_null = [&](const char* k, const std::string& v) {
        if (v.empty()) result[k] = Json::nullValue;
        else result[k] = v;
    };

    set_or_null("scheme",   url_string_to_str(url.scheme));
    result["authority"] = "EXCLUDE";
    if (url.no_userinfo) {
        result["userinfo"] = Json::nullValue;
        result["username"] = Json::nullValue;
        result["password"] = Json::nullValue;
    } else {
        result["userinfo"] = "EXCLUDE";
        set_or_null("username", url_string_to_str(url.username));
        set_or_null("password", url_string_to_str(url.password));
    }
    set_or_null("host",     url_string_to_str(url.host_text));
    if (url.no_port) result["port"] = Json::nullValue;
    else result["port"] = std::to_string(url.port);
    set_or_null("path",     url_string_to_str(url.path));
    set_or_null("query",    url_string_to_str(url.query));
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment", url_string_to_str(url.fragment));
    result["raw_url"] = url_str;
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
