#include <iostream>
#include <string>
#include <network/uri.hpp>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    try {
        network::uri u(url_str);

        auto set_or_null = [&](const char* k, network::optional<network::uri::string_type> v) {
            if (!v || v->empty()) result[k] = Json::nullValue;
            else result[k] = std::string(v->begin(), v->end());
        };

        set_or_null("scheme",   u.scheme());
        result["authority"] = "EXCLUDE";
        set_or_null("userinfo", u.user_info());
        result["username"] = "EXCLUDE";
        result["password"] = "EXCLUDE";
        set_or_null("host",     u.host());
        set_or_null("port",     u.port());
        set_or_null("path",     u.path());
        set_or_null("query",    u.query());
        result["query_dict"] = "EXCLUDE";
        set_or_null("fragment", u.fragment());
        result["raw_url"] = url_str;

    } catch (const std::exception& e) {
        result["error"] = e.what();
        result["raw_url"] = url_str;
    }

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
