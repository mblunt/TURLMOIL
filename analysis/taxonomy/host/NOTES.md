
## 2026-05-24 11:34
Pair lib1 (whatwg) vs lib2 (legacy): 50 rows — case-folding (20), ip-normalization (10), port-in-host (10), punycode (4), path-affects-host (5), percent-encoding (1), ipv6-brackets (1). Pair 1v59, 1v29, 2v6, 59v86, 48v86, 49v86: no results (JOIN filters all out due to success=false or empty hosts).

## 2026-05-24 11:38
Pair 1v3 (whatwg vs deno): minimal both-succeed differentials (control chars, whitespace).
Pair 1v7 (whatwg vs url-parse): 50 rows — percent-encoding (14), punycode (13), case-folding (4), port-in-host (2), path-affects-host (2).
Pair 2v7 (legacy vs url-parse): 50 rows — punycode (3), path-affects-host (5), port-in-host (5), fullwidth-chars (2), percent-encoding (3), case-folding (2).
Pair 2v59 (legacy vs rust-url): 50 rows — same patterns as 1v2 mirrored (ip-norm, case-fold, port-in-host, punycode, percent-encoding, path-affects-host, ipv6-brackets).

## 2026-05-24 14:07
Pair 1 (javascript-whatwg) vs 2 (javascript-legacy): case-folding(17), ip-normalization(8), port-in-host(11), path-affects-host(7), punycode(5), percent-encoding(1), ipv6-brackets(1). Pair (2,3) is mirror of (1,2).

## 2026-05-24 14:09
Pair 1 (javascript-whatwg) vs 4 (javascript-parse-uri): case-folding(7→50), percent-encoding(11), punycode(3), ip-normalization(2), userinfo-in-host(1), path-affects-host(3). Confirmed pairs 1,5 / 1,6 / 1,7 / 1,8 all exist.

## 2026-05-24 14:11
Pair 1 (whatwg) vs 5 (smithy): 0 both-succeed rows. Pair 1 vs 6 (uri-js): case-folding(~12, already@50), percent-encoding(6, surrogate-pair vs UTF-8 encoding variants + backtick + tab), punycode(2, different punycode labels), ipv6-brackets(2, brackets stripped), ip-normalization(3), userinfo-in-host(2, double-@ confusion + %40 as host), fullwidth-chars(1, U+3002). Pair 1 vs 7 (url-parse): similar categories, new: fullwidth U+3002 ideographic period. Pair 1 vs 8 (urijs): percent-encoding, case-folding, punycode.

## 2026-05-24 14:13
Pair 1 (whatwg) vs 48 (go-net): case-folding(capped), percent-encoding(5 raw-Unicode vs %-encoded), punycode(5), ipv6-brackets(2), ip-normalization(3). Pair 1 vs 59 (rust-url): 0 both-succeed rows.

## 2026-05-24 14:15
Pair 2 (legacy) vs 4 (parse-uri): port-in-host(3), punycode(2), fullwidth-chars(1, U+FF61 halfwidth японский period), userinfo-in-host, path-affects-host. Pair 2 vs 6 (uri-js): percent-encoding(tab in punycode label), punycode(surrogate vs punycode), ipv6-brackets, fullwidth-chars(U+FF61).

## 2026-05-24 14:18
Pair 1 (whatwg) vs 86 (python-urllib3): case-folding(capped), percent-encoding(2), punycode(2), ip-normalization. Pair 1 vs 56 (csharp-systemuri): case-folding(capped), percent-encoding(1 fullwidth dot), ipv6-brackets, punycode. Pair 49 (java-okhttp) vs 51 (java-uri): ipv6-brackets(3, strips vs keeps brackets + case/leading-zeros in IPv6), case-folding(many).

## 2026-05-24 14:21
Pair 2 (legacy) vs 48 (go-net): ipv6-brackets(2), punycode(1 - 15⅃), port-in-host(2). Pair 2 vs 86 (python-urllib3): ipv6-brackets(1), punycode(2), fullwidth-chars(2 - U+FF0E and U+FF61).

## 2026-05-24 14:52
## Pairs processed (batch 2)
- js-legacy(2) vs go-net(48): case-folding, port-in-host, ipv6-brackets(new), ipv6-case(new), punycode, unicode-normalization
- go-net(48) vs python-yarl(87): case-folding, unicode-normalization(+2: ᵛ→v, µ→μ), ipv6-case(+1)
- js-whatwg(1) vs csharp-systemuri(56): punycode, percent-encoding, case-folding, unicode-normalization(+1: ⁴→4), fullwidth-chars(+2)
- js-legacy(2) vs rust-url(59): case-folding, ip-normalization, punycode, ipv6-leading-zeros(+1: [07:…]→[7:…]), port-in-host
- js-legacy(2) vs python-urllib3(86): case-folding, punycode, port-in-host, ipv6-brackets(+2), fullwidth-chars(+3: 。,．), path-affects-host
- rust-url(59) vs php-parseurl(71): case-folding, punycode, percent-encoding, ip-normalization (rich pair)
- js-whatwg(1) vs php-parseurl(71): case-folding, punycode, percent-encoding, ip-normalization (rich pair)

## 2026-05-24 15:25
## Batch: js-whatwg(1) vs csharp-systemuri(56), perl-uri(46) vs python-urllib3(86), csharp-systemuri(56) vs rust-url(59), rust-url(59) vs python-urllib3(86), js-whatwg(1) vs python-yarl(87), go-net(48) vs python-urllib3(86), go-net(48) vs rust-url(59), js-whatwg(1) vs go-net(48), js-whatwg(1) vs rust-url(59)=none, javascript-legacy(2) vs rust-url(59), javascript-legacy(2) vs go-net(48)

Categories found: ipv6-brackets (added 5 more→47), fullwidth-chars (added 5 more→26), unicode-normalization (added 1→11), charset-confusion (added 2→5, confirmed pattern), percent-encoding (added 1→43), ip-normalization (added 4→35), port-in-host (added 5→43), ipv6-leading-zeros (added 1→15), case-folding (pervasive across all pairs, already full at 50), punycode (pervasive).

Key observations:
- go-net does NOT strip IPv6 brackets on some URLs, but strips them on others — inconsistent behavior
- javascript-legacy bleeds port number into host field for many URLs
- csharp-systemuri and rust-url disagree on percent-encoding vs decoding Unicode chars in host
- js-whatwg vs rust-url: ZERO differentials (both follow WHATWG spec)
- charset-confusion: go-net reads UTF-8 multibyte sequences as Latin-1, same as perl-uri

## 2026-05-24 15:34
Pairs processed (continuing):
- perl-uri (46) vs rust-url (59): scheme-as-host (with/without trailing colon in inner scheme), case-folding, punycode, ip-normalization. Added 5 scheme-as-host examples.
- javascript-legacy (2) vs python-urllib3 (86): port-in-host (urllib3 leaks port into host), ipv6-brackets, userinfo-in-host (perl leaks @), punycode, case-folding.
- perl-uri (46) vs python-urllib3 (86): charset-confusion, scheme-as-host, case-folding, punycode, userinfo-in-host.
- go-net (48) vs python-urllib3 (86): case-folding (primary), ipv6-case.
- js-whatwg (1) vs csharp-systemuri (56): case-folding, unicode-normalization, fullwidth-chars (whatwg percent-encodes fullwidth period), punycode, double-at sign ambiguity (1 case).
- js-whatwg (1) vs python-yarl (87): percent-encoding (control chars), ip-normalization (3-part IP expanded), ipv6-brackets, punycode, case-folding.
- js-whatwg (1) vs rust-url (59): NO results — perfect agreement!
- go-net (48) vs rust-url (59): ipv6-brackets+case, case-folding, unicode-normalization (⁴→4), punycode, percent-encoding.
- javascript-legacy (2) vs perl-uri (46): scheme-as-host, userinfo-in-host, case-folding, punycode, ip-normalization, port-in-host.

## 2026-05-24 15:49
## Batch progress

### perl-uri (46) vs rust-url (59)
Categories: scheme-as-host (colon), ip-normalization, case-folding, punycode, whitespace-in-authority. Added 6 scheme-as-host examples.

### elixir-uri (66) vs python-urllib3 (86)
Categories: case-folding (dominant), whitespace-in-authority (tabs in host), charset-confusion (Latin-1 vs UTF-8). Added 4 whitespace examples.

### go-net (48) vs rust-url (59)
Categories: case-folding, percent-encoding (50, capped), punycode, ip-normalization (now 49), ipv6-brackets (50, capped), unicode-normalization, fullwidth-chars. Added examples across multiple categories.

### go-net (48) vs java-galimatias (54)
Same categories as above (case-folding dominant). No new categories.

### java-galimatias (54) vs elixir-uri (66)
Categories: case-folding, punycode, whitespace-in-authority (tabs/newlines in host, elixir truncates), fullwidth-chars (。→.). Added 4 whitespace examples.

### go-net (48) vs perl-uri (46): NO RESULTS

### js-whatwg (2) vs elixir-uri (66)
Categories: port-in-host (elixir leaks port for non-standard+special-char schemes), case-folding, punycode. Added 7 port-in-host examples.

### js-whatwg (2) vs rust-url (59)
Categories: ip-normalization, port-in-host, case-folding, ipv6-leading-zeros, percent-encoding. Added 1 ipv6-leading-zeros, 4 port-in-host.

### js-whatwg (2) vs perl-uri (46)
Categories: scheme-as-host (colon), port-in-host, case-folding, punycode, path-affects-host.

### js-whatwg (2) vs java-galimatias (54)
Categories: ipv6-brackets+port-in-host, ip-normalization, case-folding, percent-encoding.


## 2026-05-24 15:55
## Session continued from context trim

**rust-url (59) vs elixir-uri (66)**: 50 diffs. Categories: case-folding (capped), ip-normalization (capped), percent-encoding (capped), punycode (capped), whitespace-control, ipv6-brackets (capped), unicode-normalization.

**elixir-uri (66) vs java-galimatias (54)**: 0 diffs, skipped.

**java-galimatias (54) vs rust-url (59)**: 50 diffs. Categories: ip-normalization (capped), ipv6-brackets (capped — added 3 examples), port-in-host (capped — added 1 with galimatias leaking port).

**perl-uri (46) vs java-galimatias (54)**: 50 diffs. Categories: case-folding (capped), scheme-as-host (added 3 real URLs), port-in-host (added 1 with IPv6), punycode (added 1).

**python-urllib3 (86) vs rust-url (59)**: 0 diffs, skipped.
**python-urllib3 (86) vs java-galimatias (54)**: 0 diffs, skipped.
**python-urllib3 (86) vs perl-uri (46)**: 0 diffs, skipped.

**js-whatwg (2) vs go-net (48)**: 50 diffs. Categories: case-folding (capped), port-in-host (capped), punycode (added 3), unicode-normalization (added 2), ipv6-brackets (capped), percent-encoding (capped).

**js-whatwg (2) vs rust-url (59)**: 50 diffs. Categories: case-folding (capped), ip-normalization (capped), percent-encoding (capped), port-in-host (capped), ipv6-leading-zeros (added 1), scheme-as-host, punycode.

**js-whatwg (2) vs java-galimatias (54)**: 50 diffs. Categories: case-folding (capped), ip-normalization (capped), percent-encoding (capped), port-in-host (capped — galimatias leaks port with IPv6), punycode, ipv6-brackets (capped).

**js-whatwg (2) vs perl-uri (46)**: 50 diffs. Categories: case-folding (capped), scheme-as-host, userinfo-in-host (added 2 with real URLs), punycode, whitespace-in-authority.

**go-net (48) vs java-galimatias (54)**: 50 diffs. Categories: case-folding (capped), punycode (added 2), unicode-normalization.


## 2026-05-24 16:00
perl-uri (46) vs rust-url (59): case-folding (capped), scheme-as-host (44), punycode (capped), ip-normalization (capped), path-affects-host. Many double-scheme URLs.
java-galimatias (54) vs rust-url (59): ip-normalization (capped), ipv6-brackets (capped). galimatias expands dotless IPs like `3`→`0.0.0.3`.
java-galimatias (54) vs elixir-uri (66): case-folding (capped), ipv6-case (27), ipv6-compression (2 new examples), fullwidth-chars (44), punycode (capped), scheme-as-host.
perl-uri (46) vs elixir-uri (66): userinfo-in-host (21), fullwidth-chars (44), scheme-as-host (44), case-folding (capped). Elixir has unusual ipv6+punycode encoding of [IPv6]:port as xn-- label.
Created new category: ipv6-compression (2 examples).

## 2026-05-24 16:04
js-whatwg (2) vs go-net (48): case-folding (capped), port-in-host (capped), ipv6-brackets (capped), ipv6-case, unicode-normalization (20), punycode (capped), scheme-as-host (capped), percent-encoding (capped).
js-whatwg (2) vs elixir-uri (66): case-folding (capped), scheme-as-host (44), ipv6-brackets (capped), punycode (capped), percent-encoding (capped), path-affects-host (capped).
js-whatwg (2) vs perl-uri (46): case-folding (capped), scheme-as-host (44), ipv6-brackets (capped), percent-encoding (capped), punycode (capped).
go-net (48) vs rust-url (59): case-folding (capped), ip-normalization (capped), percent-encoding (capped), unicode-normalization (20), ipv6-brackets (capped), ipv6-case (28), punycode (capped).
js-whatwg (2) vs java-galimatias (54): port-in-host (capped), ipv6-brackets (capped), ipv6-leading-zeros (21), path-affects-host, scheme-as-host (44).

## 2026-05-24 16:06
js-whatwg (1) vs go-net (48): case-folding (capped), ip-normalization (capped), percent-encoding (capped), unicode-normalization, punycode (capped), ipv6-brackets (capped).
csharp-systemuri (56) vs rust-url (59): case-folding (capped), punycode (capped), percent-encoding (capped), unicode-normalization (21), fullwidth-chars (45).
rust-url (59) vs python-urllib3 (86): case-folding (capped), ip-normalization (capped), percent-encoding (capped), punycode (capped), ipv6-brackets+ipv6-leading-zeros, whitespace-control (TAB in host punycoded by urllib3).

## 2026-05-24 16:48
java-galimatias (54) vs rust-url (59): ip-normalization, ipv6-brackets, ipv6-compression, ipv6-leading-zeros, leading-zeros-ip, path-affects-host, punycode — large batch.
javascript-whatwg (1) vs perl-uri (46): case-folding, punycode, scheme-as-host — multiple.
javascript-whatwg (1) vs perl-mojo-url (47): charset-confusion (Latin-1 vs UTF-8), case-folding, scheme-as-host, punycode — charset-confusion dominant.
go-net (48) vs rust-url (59): ip-normalization, ipv6-brackets, ipv6-case, unicode-normalization, percent-encoding, punycode, case-folding.

## 2026-05-24 16:50
javascript-legacy (2) vs java-galimatias (54): port-in-host (50+), ipv6-brackets (50+), ipv6-leading-zeros, ipv6-compression, charset-confusion (mojibake punycode), whitespace-in-authority, case-folding, path-affects-host.
python-urllib3 (86) vs javascript-legacy (2): 0 results.
ruby-addressable (70) vs rust-url (59): 0 results.

## 2026-05-24 16:54
java-galimatias (54) vs rust-url (59): ip-normalization (50+, dword/partial IP expansion), ipv6-brackets (50+), ipv6-leading-zeros, charset-confusion, path-affects-host, case-folding, punycode.
erlang-uri-string (83) vs rust-url (59): 0 results.
csharp-systemuri (56) vs java-galimatias (54): 0 results.
go-net (48) vs javascript-legacy (2): 0 results.
python-urllib3 (86)/yarl (87) vs javascript-whatwg (1): 0 results.
