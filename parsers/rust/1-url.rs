#!/usr/bin/env rust-script
// Rust URL parser using url crate
//
// Parses URLs using url crate and outputs JSON.

use url::Url;
use serde_json::json;
use std::env;
use std::collections::HashMap;


fn parse_url(url_str: &str) -> serde_json::Value {
    match Url::parse(url_str) {
        Ok(url) => {

            let mut query_dict: HashMap<String, Vec<String>> = HashMap::new();
            for (key, val) in url.query_pairs() {
                query_dict.entry(key.into_owned())
                    .or_insert_with(Vec::new)
                    .push(val.into_owned());
            }

            json!({
                "scheme": url.scheme(),
                "authority": "EXCLUDE",
                "userinfo": "EXCLUDE",
                "username": if url.username().is_empty() { None } else { Some(url.username()) },
                "password": url.password(),
                "host": url.host_str(),
                "port": url.port().map(|p| p.to_string()),
                "path": if url.path().is_empty() { None } else { Some(url.path()) },
                "query": url.query(),
                "query_dict": query_dict,
                "fragment": url.fragment(),
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
