
## 2026-05-28 20:25
whatwg (1) vs legacy (2): percent-encoding-normalization (25 hits)

## 2026-05-28 20:25
whatwg (1) vs parse_uri (3): host-parsing-differences (25 hits)

## 2026-05-28 20:25
whatwg (1) vs php (4): host-parsing-differences, userinfo-bleed (25 hits, most whatwg returns 0.0.0.0 or fallback)

## 2026-05-28 20:43
whatwg vs legacy: percent-encoding-normalization (4 examples) — whatwg properly encodes authority, legacy generates random/corrupted encoded strings

## 2026-05-28 20:49
whatwg vs userfriendlyurl: userinfo-port-extraction (25) — whatwg returns only host; userfriendlyurl includes port/userinfo

## 2026-05-28 20:49
whatwg vs chromedevtools: scheme-vs-authority (25), host-parsing-differences (some)

## 2026-05-28 20:49
whatwg vs python: percent-encoding-normalization (25) — different host encodings

## 2026-05-28 20:50
whatwg vs php-http: host-parsing-differences (25) — whatwg accepts, php-http returns junk

## 2026-05-28 20:51
whatwg vs js-url: scheme-vs-authority (25) — js-url extracts userinfo as authority

## 2026-05-28 20:51
whatwg vs ada: host-parsing-differences (25) — ada returns malformed authority

## 2026-05-28 20:54
uripara vs php-http: percent-encoding-normalization (25) — likely unicode/percent-encoding issues

## 2026-05-28 20:54
uripara vs ada: 0 differentials

## 2026-05-28 20:55
uripara vs node: authority-host-userinfo-confusion (25) — userinfo parsing or @ ambiguity

## 2026-05-28 20:55
php-http vs ada: authority-host-userinfo-confusion (25) — IPv6 parsing or userinfo bleed

## 2026-05-28 20:55
java-jdk vs whatwg: 0 differentials

## 2026-05-28 21:10
whatwg vs legacy: joins timeout consistently

## 2026-05-28 21:13
whatwg vs node-url: timeout on join

## 2026-05-28 21:15
whatwg vs legacy: authority-host-userinfo-confusion (3 more), control char stripping diffs

## 2026-05-28 21:16
whatwg vs legacy: control-char-stripping (9 rows)

## 2026-05-28 21:19
whatwg vs posix: no differentials found

## 2026-05-28 21:21
whatwg vs legacy: 9 results, control-char-stripping (5 new), userinfo-port-extraction (0)

## 2026-05-28 21:22
whatwg vs legacy: control-char-stripping x9

## 2026-05-28 21:23
whatwg vs node-url: 0 results

## 2026-05-28 21:26
whatwg vs legacy: control-char-stripping (25 total)

## 2026-05-28 21:27
whatwg vs go: 0 results

## 2026-05-28 21:29
whatwg vs legacy: 9/25 control-char-stripping

## 2026-05-28 21:31
whatwg vs deno: control-char-stripping (9 new, now 41)

## 2026-05-28 21:33
whatwg vs ada: 9 results; control-char-stripping pattern

## 2026-05-28 21:34
whatwg vs legacy: 0 results

## 2026-05-28 21:36
whatwg (1) vs trio (3): control-char-stripping now at 50 examples (full)

## 2026-05-28 21:38
whatwg (1) vs legacy (2): 0 authority differentials

## 2026-05-28 21:40
whatwg (1) vs legacy (2): 0 authority differentials

## 2026-05-28 21:44
legacy (2) vs radix (3): query timeout; skipping pair

## 2026-05-28 22:03
radix (3) vs whatwg (4): 25 samples; scheme-in-authority (8), host-case-normalization (2), punycode-encoding-differences (3), port-stripping-from-authority (2) identified

## 2026-05-28 22:09
radix vs jsprim (3,4): host-case-normalization(+2), control-char-stripping(full), userinfo-port-extraction(+1), punycode/encoding/parsing errors in 15+ rows

## 2026-05-28 22:11
legacy vs whatwg (1,2): 0 results

## 2026-05-28 22:11
legacy vs ruby_uri (1,3): control-char-stripping (category exists with 50+ examples)

## 2026-05-28 22:12
legacy vs jsprim (1,4): host-case-normalization+1, percent-encoding-normalization+3, scheme-in-authority+4, punycode-encoding-differences+1

## 2026-05-28 22:12
legacy vs node (1,5): no differentials found

## 2026-05-28 22:12
legacy vs python (1,6): no differentials found

## 2026-05-28 22:12
legacy vs whatwg (1,7): no differentials found

## 2026-05-28 22:12
jsprim vs whatwg (2,3): no differentials found

## 2026-05-28 22:13
jsprim vs node (2,4): timeout, skipping

## 2026-05-28 22:13
jsprim vs python (2,5): no differentials found

## 2026-05-28 22:13
jsprim vs rust (2,6): no differentials found

## 2026-05-28 22:13
jsprim vs whatwg (2,7): no differentials found

## 2026-05-28 22:13
jsprim vs php (2,8): no differentials found

## 2026-05-28 22:13
legacy vs node (3,4): 25 diffs, host-case-normalization +1, punycode-encoding-differences +1, scheme-in-authority already full

## 2026-05-28 22:14
legacy vs rust (3,5): 0 diffs

## 2026-05-28 22:14
node vs rust (4,5): query timeout—skipping

## 2026-05-28 22:38
legacy (1) vs net (3): control-char-stripping (7 rows, already at cap)

## 2026-05-28 22:45
Legacy (1) vs net (3): 9 rows with authority differences. Appears to be control char and percent-encoding edge cases; existing categories may cover some.

## 2026-05-28 22:49
legacy vs ada: 0 rows

## 2026-05-28 22:49
legacy vs net: 9 rows control-char-stripping; ada vs net: 0 rows

## 2026-05-28 23:06
legacy vs ada: 0 rows

## 2026-05-28 23:06
legacy vs net: 9 rows, control-char-stripping (5)

## 2026-05-28 23:06
ada vs net: 0 rows

## 2026-05-28 23:10
legacy vs net: control-char-stripping (9 cases, category full); ada vs net: running

## 2026-05-28 23:13
legacy vs net: control-char-stripping (3), scheme-in-authority (1). 4 total.

## 2026-05-28 23:14
legacy (1) vs net (3): all 9 rows are control-char-stripping (category full at 50).

## 2026-05-28 23:15
legacy (1) vs whatwg (4): 25 rows, added to scheme-in-authority (5 ex), host-case-normalization (5 ex). Also punycode, percent-encoding, IPv6, parsing errors but categories full or low coverage.

## 2026-05-28 23:18
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:20
legacy (1) vs curl (6): 0 rows.

## 2026-05-28 23:27
legacy (1) vs go-net (3): all 9 samples → control-char-stripping (already at 50)

## 2026-05-28 23:27
legacy (1) vs rust-url (4): 8 scheme-in-authority (one has colon suffix), 4 punycode, 6 host-case-norm, 7 mixed/complex

## 2026-05-28 23:29
go-net (3) vs rust-url (4): 6 scheme-in-authority, 3 host-case-norm, 3 punycode, 13 complex/mixed

## 2026-05-28 23:41
whatwg (2) vs go-net (3): 0 differentials.

## 2026-05-28 23:42
whatwg (2) vs rust-url (4): 0 differentials.

## 2026-05-28 23:42
go-net (3) vs rust-url (4): 25 examples, all corrupted or covered by existing categories (skip).

## 2026-05-28 23:47
whatwg (2) vs go-net (3): 0 differentials.

## 2026-05-28 23:49
whatwg (2) vs ada (4): 0 rows.

## 2026-05-28 23:52
legacy (1) vs whatwg (2): 0 rows.
