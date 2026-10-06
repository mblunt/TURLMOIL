
## 2026-05-23 20:39
## javascript-whatwg (1) vs rust-url (59)
Found ~50 differentials. Categories: empty-vs-null (21 added), ipv6-case (9 added), fullwidth-chars (7 added), ip-normalization (8 added), leading-zeros-ip (2 added). WHATWG rejects many custom/unusual scheme URLs that rust-url accepts, and vice-versa for some. IPv6 case normalization is prominent (rust-url preserves case from URL, WHATWG lowercases). Fullwidth dots produce percent-encoded host in WHATWG, empty in rust-url.

## 2026-05-23 22:02
## Pair 1 (whatwg) vs 2 (legacy) — 50 host diffs
Categories found: case-folding (8 new), scheme-as-host (5 new), port-in-host (8 new), percent-encoding (6 new), punycode (5 new), ip-normalization (1 new), empty-vs-null (11 new). Also userinfo-in-host edge cases.

## 2026-05-23 22:03
## Pair 1 (whatwg) vs 3 (deno) — 50 host diffs
Categories: empty-vs-null (hit 50 cap), ipv6-brackets (+10), fullwidth-chars (+4), punycode (+3), port-in-host (+4), percent-encoding (no new appended), case-folding (minor). Many diffs are whatwg rejecting vs deno accepting invalid hosts.

## 2026-05-23 22:12
## Pair 1 (whatwg) vs 4 (javascript-parse-uri) — 50 host diffs
Categories: case-folding (+3), percent-encoding (+1), scheme-as-host (+2), userinfo-in-host (+4), fullwidth-chars (+2). Also empty-vs-null (cap), ip-normalization, ipv6-brackets with partial bracket truncation. Very many parse-uri failures where junk chars bleed into host.

## 2026-05-23 22:18
## Pair 1 (whatwg) vs 5 (javascript-smithy) — 50 host diffs
Categories: scheme-as-host (+4), path-affects-host (+4, new category), punycode (+2), percent-encoding (+4), ip-normalization (+2). Smithy often returns empty where whatwg extracts a host. Heavy use of query/fragment chars in authority causing smithy to fail.

## 2026-05-23 22:19
## Pair 1 (whatwg) vs 6 (javascript-uri-js) — 50 host diffs
Categories: case-folding (+3), percent-encoding (+4), ipv6-brackets (+2), scheme-as-host (+1), ip-normalization (+1). uri-js heavily percent-encodes non-ASCII in host; whatwg usually returns empty for same URLs. Also trailing-dot, punycode, userinfo-in-host patterns visible.

## 2026-05-23 22:20
## Pair 1 (whatwg) vs 7 (javascript-url-parse) — 50 host diffs
Categories: port-in-host (+6), userinfo-in-host (+2), scheme-as-host (+1), fullwidth-chars (+3), case-folding, punycode, percent-encoding, ipv6-brackets. url-parse rarely strips port from host and often includes userinfo. Very messy host extraction with control chars/Unicode in URLs.

## 2026-05-23 22:21
## Pair 1 (whatwg) vs 8 (javascript-urijs) — 50 host diffs
Categories: scheme-as-host (+5), case-folding (+3), percent-encoding, port-in-host, userinfo-in-host, punycode, ip-normalization. urijs does not lowercase host and includes port/userinfo in host field. Heavy scheme-as-host with double-slash URLs.

## 2026-05-23 22:22
## Pair 1 (whatwg) vs 9 (javascript-fast-url-parser) — 50 host diffs
Categories: punycode (+3), fullwidth-chars (+3), leading-zeros-ip (+2), scheme-as-host, case-folding, ipv6-brackets, ip-normalization. fast-url-parser does punycode encode but differently than whatwg; normalizes fullwidth periods; doesn't lowercase host.

## 2026-05-23 23:32
Pair lib1 vs lib2 (javascript-whatwg vs javascript-legacy): 32057 differentials. Found: case-folding(6), ip-normalization(2), port-in-host(5), scheme-as-host(3), trailing-dot(2), punycode(7), path-affects-host(2), userinfo-in-host(2), percent-encoding(5), empty-vs-null(many). Whatwg percent-encodes non-ASCII in host; legacy leaves raw or extracts punycode. Legacy includes port in host field for many non-standard schemes.

## 2026-05-23 23:35
Pair lib1 vs lib3 (whatwg vs deno, 259 diffs): fullwidth-chars(6), punycode(6), scheme-as-host(3), percent-encoding(1), port-in-host(3), ip-normalization(0 new), ipv6-brackets(6), trailing-dot(1), path-affects-host(1), empty-vs-null(many). Deno keeps port in host for opaque schemes. Whatwg outputs punycode; deno often rejects same URL.
Pair lib1 vs lib5 (whatwg vs smithy, 86 diffs): scheme-as-host(3), punycode(3), percent-encoding(4), ip-normalization(3), path-affects-host(2), case-folding(3), empty-vs-null(many). Smithy often returns host_b where whatwg returns empty and vice versa.

## 2026-05-23 23:37
Pair lib1 vs lib6 (whatwg vs uri-js, 153593 diffs): percent-encoding(2, surrogate pairs encoded differently), case-folding(2), ip-normalization(1), ipv6-brackets(2 - uri-js strips brackets), ipv6-case(2), userinfo-in-host(1), scheme-as-host(1), empty-vs-null(many). URI-js uses surrogate-pair percent-encoding vs WTF-8 style, strips IPv6 brackets.

## 2026-05-24 00:13
## Pairs 1v2 through 1v9 (whatwg vs legacy/deno/parse-uri/smithy/uri-js/url-parse/urijs/fast-url-parser)
- case-folding: host case normalization differences → now 50
- scheme-as-host: file://http://, file://ftp:// → now 50
- punycode: IDN/unicode to xn-- → now 50
- percent-encoding: host encoding differences → now 48
- port-in-host: port included in host field → now 49
- fullwidth-chars: fullwidth period/chars → now 36
- ip-normalization: hex/octal/dotless IPs → now 30
- ipv6-brackets: brackets stripped/added → now 41
- empty-vs-null: parser rejects vs accepts host (already capped at 50)

## 2026-05-24 00:14
## Pairs 1v10, 1v11, 1v12 (whatwg vs fast-uri/parse-url/parseuri)
- userinfo-in-host: parse-url bleeds userinfo into host (10 new examples) → now 19
- port-in-host: now capped at 50
- fullwidth-chars: 5\uff0e etc. → now 40
- ip-normalization: 0.0.0.0 vs decimal → now 33
- case-folding, punycode, percent-encoding, scheme-as-host: already at/near cap

## 2026-05-24 00:15
## Pairs 1v13, 1v14, 1v15 (whatwg vs url-toolkit/jsuri/domurl)
- 1v13 (url-toolkit): 0 rows, skip
- 1v14 (jsuri): trailing-dot, scheme-as-host, fullwidth-chars, ipv6-brackets, ip-normalization
- 1v15 (domurl): ip-normalization, percent-encoding, punycode, case-folding
- percent-encoding now at 50 (capped), scheme-as-host at 50 (capped)

## 2026-05-24 00:16
## Pairs 1v16, 1v17, 1v18 (whatwg vs uri-parser/ada-uri-mime/trurl)
- userinfo-in-host: uri-parser confuses @-sign → now 23
- trailing-dot: → now 15
- ipv6-brackets: → now 46
- ip-normalization: → now 38
- path-affects-host: → now 12

## 2026-05-24 00:17
## Pairs 1v19, 1v20, 1v21 (whatwg vs aria2/wget/haskell-network-uri)
- Mostly empty-vs-null: whatwg extracts host, bin tools return null
- ipv6-brackets: brackets stripped for raw IPv6 → now 49
- ip-normalization: leading-zero IPs → now 40
- punycode now at 50 (capped)

## 2026-05-24 00:18
## Pairs 1v26, 1v28, 1v29 (whatwg vs crystal-uri/cpp-boost-url/cpp-ada-url)
- crystal-uri: userinfo bleeds into host, ip-normalization, case-folding
- cpp-boost-url: mostly empty-vs-null (whatwg extracts, boost rejects invalid)
- cpp-ada-url: only 1 row (example.com)
- ipv6-brackets now at 50 (capped)

## 2026-05-24 00:19
## Pairs 1v30, 1v42, 1v48 (whatwg vs poco-uri/swift-url/go-net)
- poco-uri: case-folding (capped), ip-normalization leading zeros
- swift-url: path-affects-host (dir traversal changes host), ip-normalization
- go-net: mostly empty-vs-null, fullwidth-chars (retains fullwidth periods)
- case-folding at 50 (capped)

## 2026-05-24 00:20
## Pairs 1v59, 1v69, 1v86 (whatwg vs rust-url/ruby-uri/python-urllib3)
- rust-url: fullwidth-chars (percent-encodes fullwidth dots), empty-vs-null for non-http schemes
- ruby-uri: case-folding (capped), ip-normalization, userinfo-in-host, path-affects-host
- python-urllib3: mostly empty-vs-null + ip-normalization
- fullwidth-chars now 48, ip-normalization now 48

## 2026-05-24 00:21
## Pairs 1v56, 1v49 (whatwg vs csharp-systemuri/java-okhttp)
- csharp-systemuri: case-folding (capped), percent-encoding (capped), ipv6-brackets differences, userinfo-in-host
- java-okhttp: leading-zeros-ip, empty-vs-null for non-http schemes
- leading-zeros-ip now 12, userinfo-in-host now 26

## 2026-05-24 00:22
## Pairs 2v3, 2v7 (javascript-legacy vs javascript-deno/url-parse)
- 2v3: case-folding (capped), trailing-dot (now 16), ip-normalization
- 2v7: port-in-host (capped at 50), ip-normalization, punycode (capped), fullwidth-chars
- Noted: url-parse includes port in host field for non-special schemes

## 2026-05-24 00:23
## Pairs 2v8, 2v14 (javascript-legacy vs javascript-urijs/jsuri)
- 2v8 (urijs): case-folding (capped), scheme-as-host (capped), port-in-host (capped), punycode
- 2v14 (jsuri): userinfo-in-host (@ in query misinterpreted), scheme-as-host (capped), ip-normalization
- ip-normalization now 49, userinfo-in-host now 29

## 2026-05-24 00:24
## Pairs 2v15, 21v22 (javascript-legacy vs javascript-domurl; haskell-network-uri vs haskell-uri-bytestring)
- domurl: port-in-host (capped), ipv6-brackets (capped), trailing-dot (now 18), path-affects-host
- haskell 21v22: empty-vs-null (capped), scheme-as-host (capped), userinfo-in-host
- trailing-dot now 18

## 2026-05-24 00:25
## Pairs 30v31, 36v37 (php-rfc3986 vs php-league-uri; python-urllib-parse vs python-furl)
- php 30v31: case-folding (capped), ipv6-brackets (capped), empty-vs-null (capped), punycode (capped)
- python 36v37: path-affects-host (now 17), fullwidth-chars (now 50, capped!), ip-normalization (now 50, capped!)
- All three major numeric-IP categories now capped

## 2026-05-24 00:26
## Pairs 40v42, 45v46 (ruby-addressable vs ruby-standard; go-stdlib vs go-gourl)
- ruby 40v42: port-in-host (capped), scheme-as-host (capped), punycode (capped), ipv6-brackets (capped)
- go 45v46: NEW variant — scheme-as-host with trailing colon (http: vs http), all numeric/text categories capped
- Notable: go-gourl punycode-encodes IPv6 addresses and fullwidth-period hosts strangely
- All major categories now capped

## 2026-05-24 00:26
## Pairs 50v51, 55v56 (rust-url vs rust-rust-url; swift-foundation vs swift-misc)
- rust 50v51: only 1 differential — scheme-as-host (file://file://), nearly identical libraries
- swift 55v56: scheme-as-host (capped), path-affects-host (now 19), ipv6-brackets (capped), empty-vs-null (capped)
- path-affects-host now 19

## 2026-05-24 00:28
## Pairs 59v65, 66v67 (rust-url vs rust-urlparse; elixir-uri vs elixir-ex_url)
- rust 59v65: ipv6-case (now 17), userinfo-in-host (now 33), path-affects-host (now 22), trailing-dot (now 20)
- elixir 66v67: ipv6-case, userinfo-in-host, path-affects-host — same recurring patterns
- New rust-urlparse quirk: returns 0.0.0.0 for invalid IPs (variant of ip-normalization, capped)
- Interesting: rust-url percent-encodes non-ASCII chars in host; percent-encoding capped

## 2026-05-24 00:32
## Pair 83v84 (erlang-uri-string vs erlang-hackney-url)
- ipv6-case (now 20), userinfo-in-host (now 36), path-affects-host (now 24)
- hackney-url extracts unicode scheme text as host for non-standard scheme URLs
- php-parseurl query timed out; skipping that pair

## 2026-05-24 00:33
## Pairs 86v87, 87v88 (python-urllib3 vs python-yarl; python-yarl vs python-furl)
- NEW CATEGORY: unicode-normalization (NFC/NFD/NFKC) — z4ᾔ4e vs z4ἤι4e, ⑳ decoded to 20
- ipv6-case (now 23), trailing-dot (now 22)
- punycode/case-folding/scheme-as-host all capped
- python-furl extracts inner scheme (http, file, ftp, wss, https) as host for double-scheme URLs

## 2026-05-24 00:34
## Pairs 89v90, 91v94 (python-httpx vs python-rfc3986; python-uritools vs python-hyperlink)
- path-affects-host (now 28), trailing-dot (now 25), userinfo-in-host (now 39), leading-zeros-ip (now 14)
- case-folding/punycode/scheme-as-host/port-in-host/percent-encoding all capped
- Notable: python-rfc3986 returns empty for many invalid hosts; python-hyperlink keeps port in host field

## 2026-05-24 00:35
## Pairs 48v49, 51v54 (go-net vs java-okhttp; java-uri vs java-galimatias)
- NEW CATEGORY: ipv6-compression — [a6:2:f:B0:2f:0:D:57] vs a6:2:f:b0:2f::d:57 (zero-group elision)
- ipv6-case (now 26), path-affects-host (now 31), userinfo-in-host (now 42)
- punycode/scheme-as-host/case-folding all capped
- java-galimatias converts punycode in IDN hostnames; java-uri does not
- go-net lowercases IPv6 and strips brackets; java-okhttp keeps brackets and original case

## 2026-05-24 00:36
## Pairs 55v56, 60v61 (java-spring-web vs java-apache-httpclient; ruby-addressable vs ruby-uri)
- path-affects-host (now 36), unicode-normalization (now 5), ipv6-case (now 28), leading-zeros-ip (now 17)
- Ruby-addressable percent-encodes non-ASCII bytes in host (66z%F2%B1%B8%87...)
- Ruby-addressable encodes circled number ⑳ into punycode label as part of IDN encoding
- java-spring-web retains IPv6 brackets with lowercase; apache-httpclient extracts nothing for invalid IPv6

## 2026-05-24 00:37
## Pairs 62v63, 65v66 (rust-url vs rust-http; swift-foundation vs node-whatwg)
- ipv6-case (now 38): rust-url lowercases + removes leading zeros in IPv6 groups; rust-http preserves original
- leading-zeros-ip (now 19): leading zeros in IPv6 hex groups also show up here
- swift-foundation vs node-whatwg: mostly case-folding (capped); node-whatwg includes port garbage in host
- port-in-host capped

## 2026-05-24 00:38
## Pairs 67v68, 70v71 (node-whatwg vs php-league; java-jdk-uri vs java-spring-mvc)
- NEW CATEGORY: whitespace-control — tab/newline in host treated differently (now 4)
- leading-zeros-ip (now 21): node-whatwg accepts "08.61.1.95" keeping leading zero; spring-mvc sees "99.01.1.20"
- path-affects-host (now 39): /../ causes different host extractions
- empty-vs-null, scheme-as-host, port-in-host all capped
- java-jdk-uri bleeds garbage after IPv6 bracket into host field

## 2026-05-24 00:39
## Pairs 72v73, 75v76 (php-pecl-http vs php-pear-net-url2; perl-uri vs perl-mojo)
- whitespace-control (now 9): tabs replaced by underscores in php-pecl-http
- leading-zeros-ip (now 24): perl-uri keeps "08.61.1.95", "99.01.1.20", "00"; perl-mojo rejects
- userinfo-in-host (now 44), trailing-dot (now 27)
- percent-encoding capped; scheme-as-host capped; port-in-host capped; case-folding capped
- perl-uri percent-encodes non-ASCII bytes in host; perl-mojo does not (or fails)

## 2026-05-24 00:40
## Pairs 78v79, 80v81 (python-stdlib vs python-whatwg; r-httr vs r-curl)
- whitespace-control (now 11): python-stdlib keeps tabs in host; python-whatwg stops/strips
- trailing-dot (now 29): r-httr keeps trailing dot; r-curl strips
- leading-zeros-ip (now 26): "00" kept by r-httr and python-stdlib
- ipv6-case (now 40): python-stdlib returns mixed-case IPv6
- python-stdlib bleeds port+garbage into host (port-in-host capped)
- r-httr vs r-curl: mostly case-folding (capped)

## 2026-05-24 00:41
## Pairs 82v83, 84v85 (scala-play vs elixir-uri; kotlin-ktor vs java-okhttp3)
- whitespace-control (12): scala-play replaces tabs with underscores
- leading-zeros-ip (28): scala-play keeps leading zeros; elixir-uri rejects
- unicode-normalization (7): java-okhttp3 appears to double-UTF8 encode Unicode bytes
- userinfo-in-host (45): java-okhttp3 includes userinfo in host
- scheme-as-host, case-folding, percent-encoding: capped in both pairs
- kotlin-ktor: many percent-encoded scheme patterns as host

## 2026-05-24 01:30
## Pairs 1v2, 1v3 (javascript-whatwg vs javascript-legacy; javascript-whatwg vs javascript-deno)
- ip-normalization capped: "00" → "0.0.0.0" by whatwg
- whitespace-control (14): tab truncates host in legacy at the tab char
- trailing-dot (30): both libs retain trailing dot but case differs
- percent-encoding capped; case-folding capped; ipv6-brackets capped; fullwidth-chars capped
- deno (lib 3): fullwidth dots get percent-encoded in host; ipv6 case differences
- leading-zeros-ip (28): "99.01.1.20:88" included as one value vs empty

## 2026-05-24 01:31
## Pairs 1v4, 1v6 (whatwg vs parse-uri; whatwg vs uri-js)
- userinfo-in-host (47): parse-uri uses wrong @ boundary
- whitespace-control (16): parse-uri and uri-js percent-encode or truncate at tab
- ipv6-case (42): ipv6-brackets capped; uri-js strips brackets, leaves mixed-case hex
- percent-encoding capped; ip-normalization capped; case-folding capped
- uri-js encodes non-BMP chars as surrogate pairs (%ED%A0...) vs proper UTF-8; fits percent-encoding (capped)

## 2026-05-24 01:32
## Pairs 1v7, 1v8 (whatwg vs url-parse; whatwg vs urijs)
- punycode capped: whatwg encodes IDN/non-ASCII labels to xn--; url-parse and urijs keep raw Unicode
- leading-zeros-ip (30): url-parse/urijs keeps leading-zero octets; whatwg rejects
- userinfo-in-host (49): urijs uses wrong @ boundary in multi-@ URLs
- percent-encoding capped; port-in-host capped; scheme-as-host capped; case-folding capped
- urijs: percent-encodes raw non-ASCII codepoints in host as UTF-8 %XX sequences

## 2026-05-24 01:33
## Pairs 1v9, 1v10 (whatwg vs fast-url-parser; whatwg vs fast-uri)
- leading-zeros-ip (32): fast-url-parser/fast-uri accept leading-zero octets; whatwg rejects
- whitespace-control (18): fast-uri retains tab in host; fast-url-parser truncates at tab
- ipv6-case (46): fast-url-parser strips brackets and may leave mixed case
- percent-encoding capped; punycode capped; scheme-as-host capped; userinfo-in-host capped
- fast-uri: keeps raw Unicode in host (punycode capped), retains tab chars

## 2026-05-24 01:33
## Pairs 1v11, 1v13 (whatwg vs parse-url; whatwg vs url-toolkit)
- userinfo-in-host (50): parse-url includes userinfo in host field; now capped
- empty-vs-null capped: parse-url returns empty for many URLs whatwg accepts
- url-toolkit: no differentials found
- parse-url: accepts invalid ports (65536), treats as empty host in whatwg

## 2026-05-24 01:34
## Pairs 1v12, 1v14 (whatwg vs javascript-parseuri; whatwg vs javascript-jsuri)
- scheme-as-host capped; percent-encoding capped; case-folding capped
- whitespace-control (20): parseuri retains tab/newline in host
- leading-zeros-ip (34): parseuri/jsuri accept leading-zero octets
- jsuri: parses @ after ? as userinfo separator (query-in-host confusion — fits userinfo-in-host capped)
- jsuri percent-encodes scheme://... differently, sometimes scheme appears as host

## 2026-05-24 01:35
## Pairs 1v15, 1v16 (whatwg vs domurl; whatwg vs uri-parser)
- whitespace-control (22): domurl retains tabs; uri-parser retains tabs in host
- path-affects-host (41): uri-parser resolves .. segments against host
- ipv6-brackets capped: uri-parser truncates IPv6 at first colon (only "[A" extracted)
- ip-normalization, percent-encoding, scheme-as-host, userinfo-in-host all capped

## 2026-05-24 01:35
## Pairs 1v17, 1v29 (whatwg vs ada-uri-mime; whatwg vs cpp-ada-url)
- ada-uri-mime: accepts leading-zero IP octets (leading-zeros-ip 36)
- port-in-host capped; empty-vs-null capped; scheme-as-host capped; case-folding capped
- ada-uri-mime: applies punycode to IDN labels in some cases while whatwg doesn't (non-http schemes)
- cpp-ada-url: minimal diff, only example.com empty-vs-null (1 row)
- interesting: ada-uri-mime returns port+garbage as host for file:// URLs (port-in-host capped)

## 2026-05-24 01:36
## Pairs 1v59, 59v63 (whatwg vs rust-url; rust-url vs rust-uriparse)
- ipv6-case (50 capped): rust-url lowercases IPv6; uriparse doesn't always parse
- leading-zeros-ip (39): rust-url accepts leading-zero octets; whatwg rejects
- trailing-dot (32): rust-url accepts trailing dots; whatwg rejects
- path-affects-host (44): rust-uriparse resolves ... as host; data://host/../ etc.
- empty-vs-null, scheme-as-host, percent-encoding all capped

## 2026-05-24 01:37
## Pairs 48v59, 48v86 (go-net vs rust-url; go-net vs python-urllib3)
- path-affects-host (47): /./  and /.../ patterns cause different host extraction
- trailing-dot (34): go-net accepts trailing dot, urllib3 does too but differs in case
- percent-encoding capped: go-net returns Unicode in host, rust-url percent-encodes it
- case-folding capped: go-net retains case, rust-url lowercases
- leading-zeros-ip (39): go-net accepts, urllib3 rejects
- unicode in hostname: go-net tolerates, urllib3 rejects (empty-vs-null capped)

## 2026-05-24 01:38
## Pairs 56v59, 66v86 (csharp-systemuri vs rust-url; elixir-uri vs python-urllib3)
- csharp: returns IPv6 without brackets (missing-brackets variant), rust rejects garbage-appended IPv6 
- csharp vs rust: punycode capped; case-folding capped
- elixir: strips IPv6 brackets (ipv6-brackets capped)
- elixir: strips tabs from host (whitespace-control 24)
- trailing-dot (37): urllib3 accepts trailing-dot hosts; elixir rejects
- Multiple @-sign ambiguity in some URLs (userinfo-in-host capped)

## 2026-05-24 01:39
## Pairs 48v56, 56v86 (go-net vs csharp; csharp vs python-urllib3)
- path-affects-host now capped at 50
- trailing-dot (41): urllib3 accepts trailing-dot/double-dot hosts, csharp/go reject
- leading-zeros-ip (42): urllib3 accepts leading zeros; csharp/go reject
- case-folding capped, ipv6-brackets capped, empty-vs-null capped
- csharp strips IPv6 brackets (appears as bare addr without brackets)

## 2026-05-24 01:41
## Pairs 48v66, 56v63, 1v86, 66v59 (go-net vs elixir; csharp vs rust-uriparse; whatwg vs urllib3; elixir vs rust-url)
- elixir vs rust-url: 0 differentials (fully agree)
- leading-zeros-ip (46): whatwg normalizes 00 -> 0.0.0.0; urllib3 keeps raw
- trailing-dot (44): various pairs differ on retaining vs stripping trailing/leading dots
- whitespace-control (27): whatwg percent-encodes control chars in host; urllib3 strips or rejects
- punycode capped, case-folding capped, percent-encoding capped across all pairs

## 2026-05-24 01:43
## Pairs 1v59, 1v48, 63v86, 59v86 (whatwg vs rust-url; whatwg vs go-net; rust-uriparse vs urllib3; rust-url vs urllib3)
- leading-zeros-ip now capped at 50
- whitespace-control (32): whatwg percent-encodes control chars; go-net/rust-url reject
- ipv6-compression: not seen in these batches - need to look at different pairs
- unicode-normalization: need to find more examples
- All major categories now at or near cap except: trailing-dot (44), whitespace-control (32), unicode-normalization (7), ipv6-compression (1)
