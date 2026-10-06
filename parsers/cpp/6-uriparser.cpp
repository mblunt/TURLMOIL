#include <iostream>
#include <string>
#include <uriparser/Uri.h>
#include <json/json.h>

static std::string range_str(const UriTextRangeA& r) {
    if (!r.first || !r.afterLast || r.first == r.afterLast) return "";
    return std::string(r.first, r.afterLast);
}

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    UriParserStateA state;
    UriUriA uri;
    state.uri = &uri;

    if (uriParseUriA(&state, url_str.c_str()) != URI_SUCCESS) {
        result["error"] = std::string("parse error near position ") +
                          std::to_string(state.errorPos - url_str.c_str());
        result["raw_url"] = url_str;
        uriFreeUriMembersA(&uri);
        return result;
    }

    auto set_or_null = [&](const char* k, const std::string& v) {
        if (v.empty()) result[k] = Json::nullValue;
        else result[k] = v;
    };

    // Reconstruct path from segment linked list.
    // If authority is present the path is always absolute (RFC 3986 §3.3).
    std::string host_str = range_str(uri.hostText);

    set_or_null("scheme",    range_str(uri.scheme));
    result["authority"] = "EXCLUDE";
    set_or_null("userinfo",  range_str(uri.userInfo));
    result["username"] = "EXCLUDE";
    result["password"] = "EXCLUDE";
    set_or_null("host",      host_str);
    set_or_null("port",      range_str(uri.portText));
    result["path"] = "EXCLUDE";
    set_or_null("query",     range_str(uri.query));
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment",  range_str(uri.fragment));
    result["raw_url"] = url_str;

    uriFreeUriMembersA(&uri);
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
