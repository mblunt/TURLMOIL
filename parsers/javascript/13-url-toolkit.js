#!/usr/bin/env node

const urlToolkit = require('url-toolkit');

function parseUrl(url) {
    try {
        const parsed = urlToolkit.parseURL(url);

        return {
            scheme:     parsed.scheme    || null,
            authority:  parsed.netLoc    || null,
            userinfo:   "EXCLUDE",
            username:   "EXCLUDE",
            password:   "EXCLUDE",
            host:       "EXCLUDE",
            port:       "EXCLUDE",
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
