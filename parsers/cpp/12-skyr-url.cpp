#include <iostream>
#include <string>
#include <skyr/url.hpp>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    auto parsed = skyr::make_url(url_str);
    if (!parsed) {
        result["error"] = "Failed to parse URL";
        result["raw_url"] = url_str;
        return result;
    }

    auto& url = parsed.value();

    auto set_or_null = [&](const char* k, const std::string& v) {
        if (v.empty()) result[k] = Json::nullValue;
        else result[k] = v;
    };

    set_or_null("scheme", url.protocol());

    result["authority"] = "EXCLUDE";
    result["userinfo"]  = "EXCLUDE";
    set_or_null("username", url.username());
    set_or_null("password", url.password());
    set_or_null("host", url.hostname());  // hostname() omits port
    set_or_null("port", url.port());
    set_or_null("path", url.pathname());
    set_or_null("query", url.search());
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment", url.hash());

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
