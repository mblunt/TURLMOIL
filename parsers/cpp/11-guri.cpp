#include <iostream>
#include <string>
#include <glib.h>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    GError *error = nullptr;
    GUri *uri = g_uri_parse(url_str.c_str(), G_URI_FLAGS_NONE, &error);

    if (!uri) {
        result["error"] = error ? std::string(error->message) : "Failed to parse URL";
        result["raw_url"] = url_str;
        if (error) g_error_free(error);
        return result;
    }

    auto set_or_null = [&](const char* k, const char* v) {
        if (!v || v[0] == '\0') result[k] = Json::nullValue;
        else result[k] = std::string(v);
    };

    set_or_null("scheme",   g_uri_get_scheme(uri));
    result["authority"] = "EXCLUDE";
    set_or_null("userinfo", g_uri_get_userinfo(uri));
    set_or_null("username", g_uri_get_user(uri));
    set_or_null("password", g_uri_get_password(uri));
    set_or_null("host",     g_uri_get_host(uri));

    int port = g_uri_get_port(uri);
    if (port == -1) result["port"] = Json::nullValue;
    else            result["port"] = std::to_string(port);

    set_or_null("path",     g_uri_get_path(uri));
    set_or_null("query",    g_uri_get_query(uri));
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment", g_uri_get_fragment(uri));
    result["raw_url"] = url_str;

    g_uri_unref(uri);
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
