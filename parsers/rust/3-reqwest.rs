#!/usr/bin/env rust-script
// Rust URL parser using reqwest::Url
//
// Parses URLs using reqwest (which uses url crate) and outputs JSON.

use reqwest::Url;
use serde_json::json;
use std::env;

fn parse_url(url_str: &str) -> serde_json::Value {
    match Url::parse(url_str) {
        Ok(url) => {

            json!({
                "scheme": url.scheme(),
                "authority": "EXCLUDE",
                "userinfo": "EXCLUDE",
                "username": if url.username().is_empty() { None } else { Some(url.username()) },
                "password": if url.password().is_some() { Some(url.password().unwrap()) } else { None },
                "host": if url.host_str().is_some() { Some(url.host_str().unwrap()) } else { None },
                "port": if url.port().is_some() { Some(url.port().unwrap().to_string()) } else { None },
                "path": if url.path().is_empty() { None } else { Some(url.path()) },
                "query": if url.query().is_some() { Some(url.query().unwrap()) } else { None },
                "query_dict": "EXCLUDE",
                "fragment": if url.fragment().is_some() { Some(url.fragment().unwrap()) } else { None },
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
