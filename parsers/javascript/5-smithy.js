#!/usr/bin/env node

const smithy = require('@smithy/url-parser');

function parseUrl(url) {
    try {
        const parsed = smithy.parseUrl(url);
        return {
            scheme: parsed.protocol || null,
            authority: "EXCLUDE",
            userinfo: "EXCLUDE",
            username: "EXCLUDE",
            password: "EXCLUDE",
            host: parsed.hostname || null,
            port: parsed.port || null,
            path: parsed.path || null,
            query: "EXCLUDE",
            query_dict: parsed.query || null,
            fragment: "EXCLUDE",
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
