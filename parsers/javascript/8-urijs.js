#!/usr/bin/env node

const URI = require('urijs');

function parseUrl(url) {
    try {
        const uri = new URI(url);

        const scheme   = uri.scheme();
        const username = uri.username();
        const password = uri.password();
        const host     = uri.hostname();
        const port     = uri.port();
        const path     = uri.path();
        const query    = uri.query();
        const fragment = uri.fragment();

        return {
            scheme:     scheme   || null,
            authority:  "EXCLUDE",
            userinfo:   "EXCLUDE",
            username:   username || null,
            password:   password || null,
            host:       host     || null,
            port:       port     || null,
            path:       path     || null,
            query:      query    || null,
            query_dict: "EXCLUDE",
            fragment:   fragment || null,
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
