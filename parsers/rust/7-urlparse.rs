#!/usr/bin/env rust-script
// Rust URL parser using urlparse crate
//
// Parses URLs using urlparse crate and outputs JSON.

use urlparse::urlparse;
use urlparse::parse_qs;
use serde_json::json;
use std::env;

fn parse_url(url_str: &str) -> serde_json::Value {
    let url = urlparse(url_str);

    let scheme = url.scheme;
    let authority = url.netloc;
    let username = url.username;
    let password = url.password;
    let host = url.hostname;
    let port = url.port;
    let path = url.path;
    let query_dict = parse_qs(url.query.as_deref().unwrap_or("{}"));
    let query = url.query;
    let fragment = url.fragment;

    json!({
        "scheme": scheme,
        "authority": authority,
        "userinfo": "EXCLUDE",
        "username": username,
        "password": password,
        "host": host,
        "port": port,
        "path": path,
        "query": query,
        "query_dict": query_dict,
        "fragment": fragment,
        "raw_url": url_str
    })
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("{}", json!({"error": "No URL provided"}));
        std::process::exit(1);
    }

    let url = &args[1];
    let result = parse_url(url);
    println!("{}", serde_json::to_string(&result).unwrap());
}
