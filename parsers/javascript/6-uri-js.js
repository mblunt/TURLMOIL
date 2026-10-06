#!/usr/bin/env node

const { parse } = require('uri-js');

function parseUrl(url) {
    try {
        const parsed = parse(url);

        return {
            scheme:     parsed.scheme    || null,
            authority:  "EXCLUDE",
            userinfo:   parsed.userinfo  || null,
            username:   "EXCLUDE",
            password:   "EXCLUDE",
            host:       parsed.host      || null,
            port:       parsed.port != null ? String(parsed.port) : null,
            path:       parsed.path      || null,
            query:      parsed.query     || null,
            query_dict: "EXCLUDE",
            fragment:   parsed.fragment  || null,
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
