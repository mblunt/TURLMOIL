#!/usr/bin/env -S deno run

// Deno URL parser using the built-in URL class.
//
// Parses URLs using Deno's standard URL class and outputs JSON.

function parseUrl(url) {
    try {
        const parsed = new URL(url);

        return {
            scheme: parsed.protocol || null,
            authority: parsed.host || null,
            userinfo: "EXCLUDE",
            username: parsed.username || null,
            password: parsed.password || null,
            host: parsed.hostname || null,
            port: parsed.port || null,
            path: parsed.pathname || null,
            query: parsed.search || null,
            query_dict: parsed.searchParams ? Object.fromEntries(parsed.searchParams) : null,
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
    if (Deno.args.length < 1) {
        console.log(JSON.stringify({ error: "No URL provided" }));
        Deno.exit(1);
    }

    const url = Deno.args[0];
    const result = parseUrl(url);
    console.log(JSON.stringify(result));
}

if (import.meta.main) {
    main();
}
