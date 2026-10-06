#!/usr/bin/env node

const Url = require('domurl');

function parseUrl(url) {
    try {
        const parsed = new Url(url);

        const queryStr = parsed.query ? String(parsed.query) : null;

        return {
            scheme:     parsed.protocol || null,
            authority:  "EXCLUDE",
            userinfo:   "EXCLUDE",
            username:   parsed.user     || null,
            password:   parsed.pass     || null,
            host:       parsed.host     || null,
            port:       parsed.port     || null,
            path:       parsed.path     || null,
            query:      queryStr        || null,
            query_dict: "EXCLUDE",
            fragment:   parsed.hash     || null,
            raw_url:    url,
        };
    } catch (e) {
        return {
            error:   e.message,
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
