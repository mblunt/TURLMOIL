// C++ URL parser using ADA URL
//
// Parses URLs using ADA URL library and outputs JSON.

#include <iostream>
#include <string>
#include <boost/json.hpp>

// Ada single-header C++ distribution is fetched at build time; include it
#include "ada.cpp"
#include "ada.h"

//  1. scheme
//  2. authority
//     2a. userinfo
//         2aa. username
//         2ab. password
//     2b. host
//     2c. port
// 3. path
// 4. query
//     4a. query_dict
// 5. fragment

using namespace boost::json;
value parse_url(const std::string& url_str) {
    object result;
    auto parsed = ada::parse<ada::url_aggregator>(url_str);
    if (!parsed) {
        // ada::errors is an enum; provide a generic message and numeric code
        result["error"] = std::string("parse_error");
        result["error_code"] = static_cast<int>(parsed.error());
        result["raw_url"] = url_str;
        return value(result);
    }

    auto url = *parsed;

    // helpers: store null when empty view
    auto set_or_null = [&](const char* k, std::string_view v){
        if (v.empty()) result[k] = nullptr; else result[k] = std::string(v);
    };

    // ADA accessors use get_ prefixes for aggregated URL
    set_or_null("scheme", url.get_protocol());
    result["authority"] = "EXCLUDE";
    result["userinfo"] = "EXCLUDE";
    set_or_null("username", url.get_username());
    set_or_null("password", url.get_password());
    set_or_null("host", url.get_hostname());
    set_or_null("port", url.get_port());
    set_or_null("path", url.get_pathname());
    set_or_null("query", url.get_search());
    // ada doesn't provide a parsed query-dict API on url_aggregator
    result["query_dict"] = "EXCLUDE";
    set_or_null("fragment", url.get_hash());

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
