#include <iostream>
#include <string>
#include <QUrl>
#include <QUrlQuery>
#include <QString>
#include <json/json.h>

Json::Value parse_url(const std::string& url_str) {
    Json::Value result(Json::objectValue);

    QUrl url(QString::fromStdString(url_str), QUrl::TolerantMode);

    auto set_or_null = [&](const char* k, const QString& v) {
        if (v.isEmpty()) result[k] = Json::nullValue;
        else result[k] = v.toStdString();
    };

    set_or_null("scheme",    url.scheme());
    result["authority"] = "EXCLUDE";
    set_or_null("userinfo",  url.userInfo());
    set_or_null("username",  url.userName());
    set_or_null("password",  url.password());
    set_or_null("host",      url.host());

    int port = url.port();
    if (port < 0) result["port"] = Json::nullValue;
    else result["port"] = std::to_string(port);

    set_or_null("path",      url.path());
    set_or_null("query",     url.query());

    if (!url.hasQuery()) {
        result["query_dict"] = Json::nullValue;
    } else {
        QUrlQuery q(url);
        Json::Value qd(Json::objectValue);
        for (const auto& pair : q.queryItems())
            qd[pair.first.toStdString()].append(pair.second.toStdString());
        result["query_dict"] = qd;
    }

    set_or_null("fragment",  url.fragment());
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
