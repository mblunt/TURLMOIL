#!/usr/bin/env node
// Node.js URL parser using legacy Node.js 'url' module.
//
// Parses URLs using Node.js's legacy 'url' module and outputs JSON.

process.noDeprecation = true;

const urlModule = require('url');
const querystring = require('querystring');

function parseUrl(url) {
    try {
        const parsed = urlModule.parse(url);

        return {
            scheme: parsed.protocol || null,
            authority: "EXCLUDE" || null,
            userinfo: parsed.auth || null,
            username: "EXCLUDE",
            password: "EXCLUDE",
            host: parsed.host || null,
            port: parsed.port || null,
            path: parsed.pathname || null,
            query: parsed.query || null,
            query_dict: parsed.query ? querystring.parse(parsed.query) : null,
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
