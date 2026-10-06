#!/usr/bin/env node

const Uri = require('jsuri');

function parseUrl(url) {
    try {
        const uri = new Uri(url);

        return {
            scheme:     uri.protocol()  || null,
            authority:  "EXCLUDE",
            userinfo:   uri.userInfo()  || null,
            username:   "EXCLUDE",
            password:   "EXCLUDE",
            host:       uri.host()      || null,
            port:       uri.port()      || null,
            path:       uri.path()      || null,
            query:      uri.query()     || null,
            query_dict: "EXCLUDE",
            fragment:   uri.anchor()    || null,
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
