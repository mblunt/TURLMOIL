#!/usr/bin/env swift
import Foundation

struct URLResult: Codable {
    let scheme: String?
    let authority: String?
    let userinfo: String?
    let username: String?
    let password: String?
    let host: String?
    let port: String?
    let path: String?
    let query: String?
    let query_dict: String?
    let fragment: String?
    let raw_url: String
    let error: String?

    enum CodingKeys: String, CodingKey {
        case scheme
        case authority
        case userinfo
        case username
        case password
        case host
        case port
        case path
        case query
        case query_dict
        case fragment
        case raw_url
        case error
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)

        if let scheme { try container.encode(scheme, forKey: .scheme) } else { try container.encodeNil(forKey: .scheme) }
        if let authority { try container.encode(authority, forKey: .authority) } else { try container.encodeNil(forKey: .authority) }
        if let userinfo { try container.encode(userinfo, forKey: .userinfo) } else { try container.encodeNil(forKey: .userinfo) }
        if let username { try container.encode(username, forKey: .username) } else { try container.encodeNil(forKey: .username) }
        if let password { try container.encode(password, forKey: .password) } else { try container.encodeNil(forKey: .password) }
        if let host { try container.encode(host, forKey: .host) } else { try container.encodeNil(forKey: .host) }
        if let port { try container.encode(port, forKey: .port) } else { try container.encodeNil(forKey: .port) }
        if let path { try container.encode(path, forKey: .path) } else { try container.encodeNil(forKey: .path) }
        if let query { try container.encode(query, forKey: .query) } else { try container.encodeNil(forKey: .query) }
        if let query_dict { try container.encode(query_dict, forKey: .query_dict) } else { try container.encodeNil(forKey: .query_dict) }
        if let fragment { try container.encode(fragment, forKey: .fragment) } else { try container.encodeNil(forKey: .fragment) }

        try container.encode(raw_url, forKey: .raw_url)
        if let error { try container.encode(error, forKey: .error) } else { try container.encodeNil(forKey: .error) }
    }
}

func parseURL(_ urlString: String) -> URLResult {
    guard let components = URLComponents(string: urlString) else {
        return URLResult(
            scheme: nil, 
            authority: nil, 
            userinfo: nil, 
            username: nil, 
            password: nil,
            host: nil, 
            port: nil, 
            path: nil, 
            query: nil, 
            query_dict: nil,
            fragment: nil, 
            raw_url: urlString, 
            error: "Failed to parse URL"
        )
    }

    return URLResult(
        scheme: components.scheme,
        authority: "EXCLUDE",
        userinfo: "EXCLUDE",
        username: components.user,
        password: components.password,
        host: components.host,
        port: components.port.map { String($0) },
        path: components.path.isEmpty ? nil : components.path,
        query: components.query,
        query_dict: "EXCLUDE",
        fragment: components.fragment,
        raw_url: urlString,
        error: nil
    )
}

func printJSON(_ result: URLResult) {
    let encoder = JSONEncoder()
    encoder.outputFormatting = []
    do {
        let jsonData = try encoder.encode(result)
        if let jsonString = String(data: jsonData, encoding: .utf8) {
            print(jsonString)
        }
    } catch {
        let fallback = URLResult(
            scheme: nil,
            authority: nil,
            userinfo: nil,
            username: nil,
            password: nil,
            host: nil,
            port: nil,
            path: nil,
            query: nil,
            query_dict: nil,
            fragment: nil,
            raw_url: result.raw_url,
            error: error.localizedDescription
        )
        if let jsonData = try? encoder.encode(fallback),
           let jsonString = String(data: jsonData, encoding: .utf8) {
            print(jsonString)
        } else {
            print("{\"error\":\"Encoding failed\",\"raw_url\":\"\(result.raw_url)\"}")
        }
    }
}

func main() {
    let args = CommandLine.arguments
    
    guard args.count >= 2 else {
        printJSON(URLResult(
            scheme: nil,
            authority: nil,
            userinfo: nil,
            username: nil,
            password: nil,
            host: nil,
            port: nil,
            path: nil,
            query: nil,
            query_dict: nil,
            fragment: nil,
            raw_url: "",
            error: "No URL provided"
        ))
        exit(1)
    }
    
    let urlString = args[1]
    let result = parseURL(urlString)

    printJSON(result)
}

main()
