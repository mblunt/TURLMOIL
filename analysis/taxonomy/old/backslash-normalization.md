# Backslash Normalization

**Description:** WHATWG-compliant parsers treat `\` as equivalent to `/` in the authority and path, so `http://good.com\@evil.com/` resolves `evil.com` as the host; non-compliant parsers leave the backslash literal, extracting a different or empty host.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
