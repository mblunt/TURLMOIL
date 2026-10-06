#!/usr/bin/env node
// URL parser using the parse-uri npm package.
//
// Parses URLs using the parse-uri library and outputs JSON.

const parseUri = require('parse-uri')

function parseUrl(url) {
    try {
        const parsed = parseUri(url);
        return {
            scheme: parsed.protocol || null,
            authority: parsed.authority || null,
            userinfo: parsed.userInfo || null,
            username: parsed.username || null,
            password: parsed.password || null,
            host: parsed.hostname || null,
            port: parsed.port || null,
            path: parsed.pathname || null,
            query: parsed.search || null,
            query_dict: parsed.searchParams ? Object.fromEntries(parsed.searchParams) : null,
            fragment: parsed.hash || null,
            raw_url: url,
        };
    } catch (e) {
        return {
            error: e.message,
            raw_url: url,
        };
    }
}

function main() {
    if (process.argv.length < 3) {
        console.log(JSON.stringify({ error: "No URL provided" }));
        process.exit(1);
    }

    const url = process.argv[2];
    const result = parseUrl(url);
    console.log(JSON.stringify(result));
}

if (require.main === module) {
    main();
}
