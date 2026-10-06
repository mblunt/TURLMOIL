#!/usr/bin/env node

const parseUrl = require('parse-url');

function parseUrlWrapper(url) {
    try {
        const parsed = parseUrl(url);

        return {
            scheme:     parsed.protocol  || null,
            authority:  "EXCLUDE",
            userinfo:   "EXCLUDE",
            username:   parsed.user      || null,
            password:   "EXCLUDE",
            host:       parsed.resource  || null,
            port:       parsed.port != null ? String(parsed.port) : null,
            path:       parsed.pathname  || null,
            query:      parsed.search    || null,
            query_dict: "EXCLUDE",
            fragment:   parsed.hash      || null,
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
    const result = parseUrlWrapper(url);
    console.log(JSON.stringify(result));
}

if (require.main === module) {
    main();
}
