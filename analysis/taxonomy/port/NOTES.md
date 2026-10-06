
## 2026-05-28 20:29
whatwg (1) vs legacy (2): port-parsing-error (25 hits)

## 2026-05-28 20:29
whatwg (1) vs parse_uri (3): port-dot-vs-numeric (25 hits)

## 2026-05-28 20:30
whatwg (1) vs custom (4): port-parsing-error (24 hits)

## 2026-05-28 20:40
whatwg vs legacy: port-parsing-error (7 total) — whatwg normalizes valid port while legacy returns malformed random values

## 2026-05-28 20:46
whatwg vs legacy: port-parsing-error (2 examples) — whatwg correctly returns port; legacy returns random numeric strings

## 2026-05-28 20:59
whatwg vs ada: 25 differentials, port-parsing-error (10 examples)

## 2026-05-28 20:59
whatwg vs node: 24 differentials, port-parsing-error (11 examples)

## 2026-05-28 21:00
whatwg vs python: 25 differentials, port-parsing-error (12 examples)

## 2026-05-28 21:00
ada vs node: 25 differentials, port-parsing-error (13 examples)

## 2026-05-28 21:02
whatwg vs ada: 25 differentials, port-parsing-error (14 examples), mostly ada returning garbage/large numbers

## 2026-05-28 21:03
whatwg vs python: 25 differentials, port-parsing-error (mostly whatwg getting 53 or ., python random numbers)

## 2026-05-28 21:03
whatwg vs node: 25 differentials, port-parsing-error (whatwg 767332, node random values)

## 2026-05-28 21:03
whatwg vs go: 25 differentials, port-parsing-error (669 vs 0, mostly matching 0s)

## 2026-05-28 21:03
whatwg vs rust: 25 differentials, port-parsing-error (whatwg 7 or empty, rust empty or sparse)

## 2026-05-28 21:04
ada vs python: 25 differentials, leading-zero-octal (ada 0130 vs python 88, 068 vs 56, etc.)

## 2026-05-28 21:04
ada vs go: 25 differentials, port-parsing-error (ada 3/2/28 vs go 76/20/0130 octal strings)

## 2026-05-28 21:04
python vs go: 25 differentials, port-dot-vs-numeric (python . vs go numeric) and port-parsing-error

## 2026-05-28 21:04
python vs legacy: no port differentials

## 2026-05-28 21:11
whatwg vs legacy: timeout on large join

## 2026-05-28 21:14
whatwg vs node-url: leading-zero-octal (20 examples)

## 2026-05-28 21:16
whatwg vs legacy: no differentials found

## 2026-05-28 21:17
whatwg vs legacy: no differentials found

## 2026-05-28 21:19
whatwg vs posix: 25 all leading-zero-octal; category has 7 examples

## 2026-05-28 21:21
whatwg vs legacy: 0 results

## 2026-05-28 21:23
whatwg vs legacy: 0 results

## 2026-05-28 21:25
whatwg vs node-url: 25/25 leading-zero-octal (17 total)

## 2026-05-28 21:26
whatwg vs legacy: 0 results

## 2026-05-28 21:28
whatwg vs go: 25/25 leading-zero-octal

## 2026-05-28 21:30
whatwg vs legacy: 0 results

## 2026-05-28 21:34
whatwg vs ada: 0 results

## 2026-05-28 21:35
whatwg vs legacy: 25 leading-zero-octal samples (category at 17+)

## 2026-05-28 21:37
whatwg (1) vs trio (3): 0 port differentials

## 2026-05-28 21:38
whatwg (1) vs legacy (2): 25 port differentials, mostly leading-zero-octal (16) + others

## 2026-05-28 21:41
whatwg (1) vs legacy (2): 25 port differentials, all leading-zero-octal

## 2026-05-28 21:48
legacy (2) vs radix (3): query timeout; skipping pair

## 2026-05-28 22:22
whatwg vs legacy (1,2): 25 diffs, all leading-zero-octal (whatwg strips leading 0s, legacy preserves)

## 2026-05-28 22:22
whatwg vs node (1,3): 0 diffs

## 2026-05-28 22:23
whatwg vs legacy (1,4): timeout—skipping

## 2026-05-28 22:23
whatwg vs rust (1,5): 0 diffs

## 2026-05-28 22:23
legacy vs node (2,3): 25 diffs, all leading-zero-octal

## 2026-05-28 22:24
legacy vs rust (2,4): 25 diffs, mostly port-parsing-error + a few leading-zero-octal

## 2026-05-28 22:24
legacy vs rust (2,5): 25 diffs, all leading-zero-octal

## 2026-05-28 22:25
node vs rust (3,4): TIMEOUT, skipping

## 2026-05-28 22:25
node vs rust (3,5): 0 diffs

## 2026-05-28 22:26
rust vs rust (4,5): 25 diffs, mix of leading-zero-octal + port-parsing-error

## 2026-05-28 22:28
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:29
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:30
legacy vs ada (1,2): 25 diffs - leading-zero-octal (full)

## 2026-05-28 22:32
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:32
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:32
legacy vs ada (1,2): 25 diffs - leading-zero-octal (capped at 50)

## 2026-05-28 22:40
legacy (1) vs ada (2): 25 rows all leading-zero-octal (category full at 50).

## 2026-05-28 22:40
ada (2) vs net (3): 25 rows all leading-zero-octal (category full at 50).

## 2026-05-28 22:45
legacy vs ada: 25 rows, all leading-zero-octal (cat full at 50)

## 2026-05-28 22:45
ada vs net: 25 rows, all leading-zero-octal (cat full at 50)

## 2026-05-28 22:51
legacy vs net: 0 rows

## 2026-05-28 22:51
ada vs net: 25 rows, all leading-zero-octal (already at 50)

## 2026-05-28 22:55
legacy vs ada: 25 rows, leading-zero-octal (already at 50)

## 2026-05-28 22:55
legacy vs net: 0 rows

## 2026-05-28 22:55
ada vs net: 25 rows, leading-zero-octal (already at 50)

## 2026-05-28 23:00
legacy vs ada: 25 rows leading-zero-octal (already has 50, skipped)

## 2026-05-28 23:00
legacy vs net: 0 rows

## 2026-05-28 23:00
ada vs net: 25 rows leading-zero-octal (already has 50, skipped)

## 2026-05-28 23:03
legacy vs ada: 25 rows leading-zero-octal (50 cap)

## 2026-05-28 23:03
legacy vs net: 0 rows

## 2026-05-28 23:03
ada vs net: 25 rows leading-zero-octal (50 cap)

## 2026-05-28 23:08
ada vs net: 25 leading-zero-octal cases found (category full at 50)

## 2026-05-28 23:10
legacy vs net: 0 cases; ada vs net: leading-zero-octal (25 cases, category full)

## 2026-05-28 23:17
legacy (1) vs whatwg (4): 25 rows, all leading-zero-octal (e.g. 06→6, 0956→956). Category at 50, full; no additions.

## 2026-05-28 23:19
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:25
legacy (1) vs whatwg (7): leading-zero-octal (50 capped).

## 2026-05-28 23:36
legacy (1) vs whatwg (2): 25 examples, leading-zero-octal (whatwg preserves leading zeros in port output; legacy strips them)

## 2026-05-28 23:37
legacy (1) vs rust-url (4): 25 examples, leading-zero-octal (preserve zeros), port-corruption-arithmetic (5 cases differ by modulo/truncation).

## 2026-05-28 23:37
whatwg (2) vs go-net (3): 25 examples, leading-zero-octal (at 50 cap).

## 2026-05-28 23:37
whatwg (2) vs rust-url (4): 25 examples, port-corruption-arithmetic (8 cases).

## 2026-05-28 23:38
whatwg (2) vs node (5): 25 examples, leading-zero-octal (all cases).

## 2026-05-28 23:38
go-net (3) vs rust-url (4): 25 examples, port-corruption-arithmetic (2 cases) + leading-zero-octal.

## 2026-05-28 23:39
rust-url (4) vs node (5): 25 examples, port-corruption-arithmetic (3 cases) + leading-zero-octal.

## 2026-05-28 23:44
legacy (1) vs whatwg (2): 25 examples all leading-zero-octal (50+ examples, skip).

## 2026-05-28 23:45
legacy (1) vs go-net (3): 0 differentials.

## 2026-05-28 23:46
legacy (1) vs rust-url (4): 25 sampled; 24 leading-zero-octal, rest arithmetic-diff. Added 20 examples to port-corruption-arithmetic (now 33).

## 2026-05-28 23:48
whatwg (2) vs go-net (3): 25 rows — leading-zero-octal (25).

## 2026-05-28 23:51
whatwg (2) vs ada (4): IPv6 port parsing—arithmetic corruption + parsing errors, fits port-corruption-arithmetic (33/50). 25 rows.
