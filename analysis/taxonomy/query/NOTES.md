
## 2026-05-28 20:32
whatwg (1) vs legacy (2): query-percent-encoding (25 hits)

## 2026-05-28 20:32
whatwg (1) vs parse_uri (3): query-percent-encoding (16 hits)

## 2026-05-28 20:33
whatwg (1) vs uri_parse (4): query-percent-encoding (25 hits)

## 2026-05-28 20:33
whatwg (1) vs rusturl (5): query-percent-encoding (25 hits)

## 2026-05-28 20:34
legacy_url (2) vs parse_uri (3): query-percent-encoding (25 hits)

## 2026-05-28 20:34
legacy_url (2) vs uri_parse (4): query-percent-encoding (25 hits)

## 2026-05-28 20:35
legacy_url (2) vs rusturl (5): query-percent-encoding (25 hits)

## 2026-05-28 20:36
parse_uri (3) vs uri_parse (4): query-percent-encoding (25 hits)

## 2026-05-28 20:36
parse_uri (3) vs rusturl (5): query-percent-encoding (25 hits)

## 2026-05-28 20:37
uri_parse (4) vs rusturl (5): query-percent-encoding (25 hits)

## 2026-05-28 20:42
whatwg vs legacy: query-parsing-error (5 examples) — whatwg normalizes to percent-encoded form, legacy corrupts/truncates

## 2026-05-28 20:47
whatwg vs legacy: query-unicode-handling (2) — whatwg normalizes to percent-encoded; legacy preserves/mangles unicode

## 2026-05-28 21:01
whatwg vs ada: 25 differentials, query-parsing-error (6 examples)

## 2026-05-28 21:01
whatwg vs python: 25 differentials, mostly sparse/no clear categories

## 2026-05-28 21:07
whatwg vs go: query joins too slow, cannot sample efficiently

## 2026-05-28 21:12
whatwg vs legacy: query-percent-encoding, unicode-handling observed (20 rows)

## 2026-05-28 21:15
whatwg vs node-url: query-unicode-handling (2), mostly encoding diffs in 20

## 2026-05-28 21:16
whatwg vs legacy: no differentials found

## 2026-05-28 21:17
whatwg vs legacy: no differentials found

## 2026-05-28 21:20
whatwg vs posix: 25 results, query-percent-encoding (5) and query-unicode-handling (6) with new examples

## 2026-05-28 21:21
whatwg vs legacy: 0 results

## 2026-05-28 21:23
whatwg vs legacy: 0 results

## 2026-05-28 21:25
whatwg vs node-url: query-percent-encoding (7 total)

## 2026-05-28 21:26
whatwg vs legacy: 0 results

## 2026-05-28 21:29
whatwg vs go: 25/25 mixed (query-percent-encoding, query-unicode-handling)

## 2026-05-28 21:30
whatwg vs legacy: 0 results

## 2026-05-28 21:33
whatwg vs node-url: 25 results; percent-encoding and unicode handling patterns

## 2026-05-28 21:34
whatwg vs ada: 0 results

## 2026-05-28 21:36
whatwg vs legacy: query-percent-encoding (unicode + special chars), query-unicode-handling observed

## 2026-05-28 21:37
whatwg (1) vs trio (3): 0 query differentials

## 2026-05-28 21:40
whatwg (1) vs legacy (2): 25 query differentials, query-percent-encoding (9), query-unicode-handling (2)

## 2026-05-28 21:42
whatwg (1) vs legacy (2): 25 query differentials; query-percent-encoding (6), query-unicode-handling (2)

## 2026-05-28 21:42
whatwg (1) vs radix (3): 0 query differentials

## 2026-05-28 21:56
legacy (2) vs radix (3): 25 samples; query-percent-encoding and unicode patterns identified; added 6 examples (32 total)

## 2026-05-28 22:05
radix (3) vs whatwg (4): 25 samples; query-percent-encoding (5+), query-unicode-handling (1+)

## 2026-05-28 22:27
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:27
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:27
legacy vs ada (1,2): 25 diffs - query-percent-encoding, query-unicode-handling

## 2026-05-28 22:30
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:30
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:30
legacy vs ada (1,2): 25 diffs - query-percent-encoding (full 37), query-unicode-handling

## 2026-05-28 22:31
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:31
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:31
legacy vs ada (1,2): 25 diffs - query-percent-encoding (now 40), query-unicode-handling

## 2026-05-28 22:42
legacy (1) vs ada (2): 25 rows—query-percent-encoding (43/50, added 3), unicode-handling, parsing-error.

## 2026-05-28 22:43
ada (2) vs net (3): 25 rows—query-percent-encoding (45/50, added 2), unicode-handling, parsing-error.

## 2026-05-28 22:48
legacy vs ada: 25 rows, mostly query-percent-encoding (5 added, cat now 50)

## 2026-05-28 22:48
legacy vs net: 0 rows

## 2026-05-28 22:48
ada vs net: 25 rows, all query-percent-encoding (cat full)

## 2026-05-28 22:52
legacy vs ada: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 22:53
legacy vs net: 0 rows

## 2026-05-28 22:53
ada vs net: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 22:55
legacy vs ada: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 22:56
legacy vs net: 0 rows

## 2026-05-28 22:56
ada vs net: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 22:57
legacy vs ada: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 22:58
legacy vs net: 0 rows

## 2026-05-28 22:58
ada vs net: 25 rows, query-percent-encoding (already at 50)

## 2026-05-28 23:01
legacy vs ada: 25 rows query-percent-encoding (50 cap), query-unicode-handling

## 2026-05-28 23:02
legacy vs net: 0 rows

## 2026-05-28 23:02
ada vs net: 25 rows query-percent-encoding (50 cap), query-unicode-handling

## 2026-05-28 23:04
legacy vs ada: 25 rows query-percent-encoding (50 cap), query-unicode-handling

## 2026-05-28 23:05
legacy vs net: 0 rows

## 2026-05-28 23:05
ada vs net: 25 rows query-percent-encoding (50 cap), query-unicode-handling

## 2026-05-28 23:08
ada vs net: 25 query-percent-encoding cases found (category full at 50)

## 2026-05-28 23:11
ada vs net: query-percent-encoding (full), query-unicode-handling (25+ cases)

## 2026-05-28 23:17
legacy (1) vs whatwg (4): 25 rows. Percent-encoding (50/50 full) and control-char/unicode handling. Already at 16 for query-unicode-handling; no new appends.

## 2026-05-28 23:19
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:23
legacy (1) vs curl (6): query-percent-encoding (50 found, capped), query-unicode-handling (16).

## 2026-05-28 23:25
legacy (1) vs whatwg (7): query-percent-encoding (50 capped), query-unicode-handling.

## 2026-05-28 23:40
whatwg (2) vs go-net (3): 25 examples, all query-percent-encoding (capped at 50).

## 2026-05-28 23:40
whatwg (2) vs rust-url (4): 25 examples, all query-percent-encoding (capped at 50).

## 2026-05-28 23:46
legacy (1) vs go-net (3): 0 differentials.

## 2026-05-28 23:47
legacy (1) vs rust-url (4): 25 sampled; all query-percent-encoding and query-unicode-handling (both categories at capacity).

## 2026-05-28 23:48
whatwg (2) vs go-net (3): 25 rows — query-percent-encoding (25).

## 2026-05-28 23:51
whatwg (2) vs ada (4): Percent-encoding + whitespace in query, fits query-percent-encoding (50/50). 25 rows.
