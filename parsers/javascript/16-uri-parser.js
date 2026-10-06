#!/usr/bin/env node

const uriParser = require('uri-parser');

function parseUrl(url) {
    try {
        const parsed = uriParser.parse(url);

        return {
            scheme:     parsed.protocol    || null,
            authority:  parsed.authority   || null,
            userinfo:   parsed.userInfo  || null,
            username:   parsed.user      || null,
            password:   parsed.password  || null,
            host:       parsed.host      || null,
            port:       parsed.port != null ? String(parsed.port) : null,
            path:       parsed.path      || null,
            query:      parsed.query     || null,
            query_dict: parsed.queryKey  || null,
            fragment:   parsed.anchor  || null,
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
