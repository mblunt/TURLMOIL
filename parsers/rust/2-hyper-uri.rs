#!/usr/bin/env rust-script
// Rust URL parser using hyper::Uri
//
// Parses URLs using hyper library and outputs JSON.

use hyper::Uri;
use serde_json::json;
use std::env;


fn parse_url(url_str: &str) -> serde_json::Value {
    match url_str.parse::<Uri>() {
        Ok(uri) => {

            json!({
                "scheme": if uri.scheme_str().is_some() { Some(uri.scheme_str().unwrap()) } else { None },
                "authority": if uri.authority().is_some() { Some(uri.authority().unwrap().to_string()) } else { None },
                "userinfo": "EXCLUDE",
                "username": "EXCLUDE",
                "password": "EXCLUDE",
                "host": if uri.host().is_some() { Some(uri.host().unwrap()) } else { None },
                "port": if uri.port_u16().is_some() { Some(uri.port_u16().unwrap().to_string()) } else { None },
                "path": if uri.path().is_empty() { None } else { Some(uri.path()) },
                "query": if uri.query().is_some() { Some(uri.query().unwrap()) } else { None },
                "query_dict": "EXCLUDE",
                "fragment": "EXCLUDE",
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
