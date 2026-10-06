#include "common.h"

#include <iostream>
#include <string>

#include "uri.h"
#include "uri_split.h"

namespace {

// Proper JSON string escape (double-quoted, handles all JSON special chars)
std::string jsonString(const std::string& value)
{
  std::string out;
  out.reserve(value.size() + 2);
  out += '"';
  for (unsigned char ch : value) {
    switch (ch) {
    case '"':  out += "\\\""; break;
    case '\\': out += "\\\\"; break;
    case '\n': out += "\\n";  break;
    case '\r': out += "\\r";  break;
    case '\t': out += "\\t";  break;
    case '\b': out += "\\b";  break;
    case '\f': out += "\\f";  break;
    default:
      if (ch < 0x20) {
        char buf[7];
        snprintf(buf, sizeof(buf), "\\u%04x", ch);
        out += buf;
      } else {
        out += ch;
      }
    }
  }
  out += '"';
  return out;
}

// Output a JSON key:value pair; null when value is empty
void kv(const std::string& key, const std::string& value, bool& first)
{
  if (!first) std::cout << ',';
  first = false;
  std::cout << jsonString(key) << ':';
  if (value.empty())
    std::cout << "null";
  else
    std::cout << jsonString(value);
}

// Overload for always-string values (like "EXCLUDE")
void kvLit(const std::string& key, const std::string& literal, bool& first)
{
  if (!first) std::cout << ',';
  first = false;
  std::cout << jsonString(key) << ':' << jsonString(literal);
}

std::string getField(const uri_split_result& split, uri_split_field field,
                     const std::string& url)
{
  return aria2::uri::getFieldString(split, field, url.c_str());
}

} // namespace

int main(int argc, char** argv)
{
  if (argc < 2) {
    std::cout << "{\"error\":\"No URL provided\"}\n";
    return 1;
  }

  const std::string rawUrl = argv[1];
  aria2::uri::UriStruct uri;
  uri_split_result split;

  if (!aria2::uri::parse(uri, rawUrl) || uri_split(&split, rawUrl.c_str()) != 0) {
    std::cout << "{\"error\":\"failed to parse URL\","
              << "\"raw_url\":" << jsonString(rawUrl) << "}\n";
    return 1;
  }

  const auto fragment = getField(split, USR_FRAGMENT, rawUrl);
  const auto query    = getField(split, USR_QUERY, rawUrl);
  const auto userinfo = getField(split, USR_USERINFO, rawUrl);
  const auto path     = split.field_set & (1 << USR_PATH)
                          ? getField(split, USR_PATH, rawUrl)
                          : std::string("/");

  bool first = true;
  std::cout << '{';
  kv("scheme",     uri.protocol, first);
  kvLit("authority", "EXCLUDE",  first);
  kv("userinfo",   userinfo,     first);
  kv("username",   uri.username, first);
  kv("password",   uri.password, first);
  kv("host",       uri.host,     first);
  kv("port",       uri.port ? std::to_string(uri.port) : std::string(), first);
  kv("path",       path,         first);
  kv("query",      query,        first);
  kvLit("query_dict", "EXCLUDE", first);
  kv("fragment",   fragment,     first);
  kv("raw_url",    rawUrl,       first);
  std::cout << "}\n";

  return 0;
}
