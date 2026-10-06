#!/usr/bin/env rust-script
// Rust URL parser using uriparse crate
//
// Parses URLs using uriparse crate and outputs JSON.

use std::convert::TryFrom;
use uriparse::URI;
use serde_json::json;
use std::env;

fn parse_url(url_str: &str) -> serde_json::Value {
    match URI::try_from(url_str) {
        Ok(uri) => {
            let scheme = uri.scheme().as_str();

            let (authority, username, password, host, port) = if let Some(auth) = uri.authority() {
                let authority = Some(auth.to_string());
                let username = auth.username().map(|u| u.as_str().to_string());
                let password = auth.password().map(|p| p.as_str().to_string());
                let host = Some(auth.host().to_string());
                let port = auth.port().map(|p| p.to_string());
                (authority, username, password, host, port)
            } else {
                (None, None, None, None, None)
            };

            let path = uri.path().to_string();
            let path = if path.is_empty() { None } else { Some(path) };
            let query = uri.query().map(|q| q.as_str().to_string());
            let fragment = uri.fragment().map(|f| f.as_str().to_string());

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
                "query_dict": "EXCLUDE",
                "fragment": fragment,
                "raw_url": url_str
            })
        }
        Err(e) => {
            json!({
                "error": e.to_string(),
                "raw_url": url_str
            })
        }
    }
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
