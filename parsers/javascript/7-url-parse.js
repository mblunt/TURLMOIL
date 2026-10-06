#!/usr/bin/env node

const Url = require('url-parse');

function parseUrl(url) {
    try {
        const parsed = new Url(url);

        return {
            scheme:     parsed.protocol || null,
            authority:  "EXCLUDE",
            userinfo:   parsed.auth     || null,
            username:   parsed.username || null,
            password:   parsed.password || null,
            host:       parsed.hostname || null,
            port:       parsed.port     || null,
            path:       parsed.pathname || null,
            query:      parsed.query    || null,
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
