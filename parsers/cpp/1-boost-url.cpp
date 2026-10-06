// C++ URL parser using Boost.URL
//
// Parses URLs using Boost.URL library and outputs JSON.

#include <iostream>
#include <string>
#include <boost/url.hpp>
#include <boost/json.hpp>

using namespace boost::urls;
using namespace boost::json;

// Components of a URL:

// https://username:password@subdomain.hostname.tld:port/path?query_key=query_value&query#fragment
//  1. scheme
//  2. authority
//     2a. userinfo
//         2aa. username
//         2ab. password
//     2b. host
//     2c. port
// 3. path
// 4. query
//     4a. query_keys
//     4b. query_values
// 5. fragment


// https://www.boost.org/doc/libs/latest/doc/antora/url/reference/boost/urls/url_view.html
// Boost has lots of ways to return the components; you can choose to return encoded or decoded forms.
// We will return decoded for this parser.

value parse_url(const std::string& url_str) {
    object result;
    auto parsed = parse_uri(url_str);
    if (!parsed) {
        result["error"] = "Failed to parse URL";
        result["raw_url"] = url_str;
        return value(result);
    }

    url_view uv = *parsed;

    // helpers for string-like components
    auto set_or_null = [&](const char* k, string_view v){
        if (v.empty()) result[k] = nullptr; else result[k] = std::string(v);
    };

    set_or_null("scheme", uv.scheme());
    // authority is an authority_view (not directly convertible to string_view)
    // build it manually from userinfo, host, and port
    set_or_null("authority", "EXCLUDE");


    set_or_null("userinfo", uv.userinfo());
    set_or_null("username", uv.user());
    set_or_null("password", uv.password());
    set_or_null("host", uv.host());
    set_or_null("port", uv.port());
    set_or_null("path", uv.path());
    set_or_null("query", uv.query());

    // Extract query keys and values as a dict
    object query_dict;
    for (auto const& param : uv.params()) {
        query_dict[std::string(param.key)] = std::string(param.value);
    }
    result["query_dict"] = query_dict;

    set_or_null("fragment", uv.fragment());
    result["raw_url"] = url_str;

    return value(result);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        boost::json::object out;
        out["error"] = "No URL provided";
        std::cout << boost::json::serialize(out) << std::endl;
        return 1;
    }

    std::string url = argv[1];
    value result = parse_url(url);
    std::cout << serialize(result) << std::endl;
    
    return 0;
}
