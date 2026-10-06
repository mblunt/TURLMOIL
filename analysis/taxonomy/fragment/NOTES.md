
## 2026-05-28 20:30
whatwg (1) vs legacy (2): fragment-unicode-stripping (25 hits)

## 2026-05-28 20:30
whatwg (1) vs parse_uri (3): fragment-percent-encoding (25 hits)

## 2026-05-28 20:31
whatwg (1) vs uri_parse (4): fragment-percent-encoding (25 hits)

## 2026-05-28 20:37
parse_uri (3) vs uri_parse (4): fragment-multiple-hashes, fragment-unicode-stripping (25 hits) - first # vs last # handling

## 2026-05-28 20:41
whatwg vs legacy: multiple-hash-handling (10 total) — whatwg preserves raw fragment content, legacy returns empty or truncated

## 2026-05-28 20:46
whatwg vs legacy: fragment-unicode-stripping (2), multiple-hash-handling (1) — whatwg preserves unicode; legacy strips/encodes inconsistently

## 2026-05-28 21:02
whatwg vs ada: 25 differentials, fragment-unicode-stripping (4 examples)

## 2026-05-28 21:02
whatwg vs python: 25 differentials, mostly sparse/parsing errors

## 2026-05-28 21:05
whatwg vs go: 25 differentials found, fragment-leading-hash (new), 2 examples added

## 2026-05-28 21:05
ada vs python: 25 differentials, fragment-leading-hash, 3 examples added

## 2026-05-28 21:11
whatwg vs legacy: fragment-percent-encoding (full), multiple-hash-handling and unicode-stripping seen

## 2026-05-28 21:15
whatwg vs node-url: fragment-unicode-stripping (2), fragment-percent-encoding (2) in 20

## 2026-05-28 21:16
whatwg vs legacy: no differentials found

## 2026-05-28 21:17
whatwg vs legacy: no differentials found

## 2026-05-28 21:20
whatwg vs posix: 25 results, fragment-percent-encoding (9) and fragment-unicode-stripping (8) with new examples

## 2026-05-28 21:21
whatwg vs legacy: 0 results

## 2026-05-28 21:23
whatwg vs legacy: 0 results

## 2026-05-28 21:25
whatwg vs node-url: fragment-percent-encoding (12 total)

## 2026-05-28 21:26
whatwg vs legacy: 0 results

## 2026-05-28 21:28
whatwg vs go: 25/25 mixed (fragment-percent-encoding, fragment-unicode-stripping, multiple-hash-handling)

## 2026-05-28 21:30
whatwg vs legacy: 0 results

## 2026-05-28 21:33
whatwg vs node-url: 25 results; pattern mix: percent-encoding normalization, unicode stripping - fits existing categories

## 2026-05-28 21:34
whatwg vs ada: 0 results

## 2026-05-28 21:36
whatwg vs legacy: fragment-percent-encoding (unicode + case), fragment-unicode-stripping, multiple-hash-handling observed in batch

## 2026-05-28 21:37
whatwg (1) vs trio (3): 0 fragment differentials

## 2026-05-28 21:39
whatwg (1) vs legacy (2): 25 fragment differentials, mostly fragment-percent-encoding and unicode-stripping

## 2026-05-28 21:41
whatwg (1) vs legacy (2): 25 fragment differentials; fragment-percent-encoding (8), fragment-unicode-stripping (2), multiple-hash-handling (1)

## 2026-05-28 21:56
legacy (2) vs radix (3): query timeout; skipping pair

## 2026-05-28 22:05
radix (3) vs whatwg (4): 25 samples; fragment-percent-encoding (5+), fragment-unicode-stripping (1+)

## 2026-05-28 22:26
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:26
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:26
whatwg vs node (0,3): 0 diffs

## 2026-05-28 22:26
whatwg vs rust (0,4): 0 diffs

## 2026-05-28 22:26
legacy vs ada (1,2): 25 diffs = fragment-percent-encoding (6) + fragment-unicode-stripping (3 partial)

## 2026-05-28 22:27
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:28
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:28
legacy vs ada (1,2): 25 diffs - fragment-percent-encoding, fragment-unicode-stripping

## 2026-05-28 22:30
whatwg vs legacy (0,1): 0 diffs

## 2026-05-28 22:30
whatwg vs ada (0,2): 0 diffs

## 2026-05-28 22:31
legacy vs ada (1,2): 25 diffs - fragment-percent-encoding (now 35), fragment-unicode-handling, multiple-hash-handling

## 2026-05-28 22:41
legacy (1) vs ada (2): 25 rows—fragment-percent-encoding (38/50, added 3), unicode-stripping, multiple-hash-handling.

## 2026-05-28 22:41
ada (2) vs net (3): 25 rows—fragment-percent-encoding (41/50, added 3), unicode-stripping, multiple-hash-handling.

## 2026-05-28 22:47
legacy vs ada: 25 rows, all fragment-percent-encoding (9 added, cat now 50)

## 2026-05-28 22:47
legacy vs net: 0 rows

## 2026-05-28 22:47
ada vs net: 25 rows, all fragment-percent-encoding (cat full at 50)

## 2026-05-28 22:51
legacy vs ada: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 22:52
legacy vs net: 0 rows

## 2026-05-28 22:52
ada vs net: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 22:53
legacy vs ada: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 22:54
legacy vs net: 0 rows

## 2026-05-28 22:54
ada vs net: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 22:56
legacy vs ada: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 22:57
legacy vs net: 0 rows

## 2026-05-28 22:57
ada vs net: 25 rows, fragment-percent-encoding (already at 50)

## 2026-05-28 23:01
legacy vs ada: 25 rows fragment-percent-encoding (50 cap), fragment-unicode-stripping (13 total)

## 2026-05-28 23:01
legacy vs net: 0 rows

## 2026-05-28 23:01
ada vs net: 25 rows fragment-percent-encoding (50 cap), fragment-unicode-stripping (13 total)

## 2026-05-28 23:03
legacy vs ada: 25 rows fragment-percent-encoding (50 cap), fragment-unicode-stripping, multiple-hash-handling

## 2026-05-28 23:04
legacy vs net: 0 rows

## 2026-05-28 23:04
ada vs net: 25 rows fragment-percent-encoding (50 cap), fragment-unicode-stripping, multiple-hash-handling

## 2026-05-28 23:09
ada vs net: 25 fragment-percent-encoding cases found (category full at 50)

## 2026-05-28 23:11
ada vs net: fragment-percent-encoding (25+ cases, full); fragment-unicode-stripping observed

## 2026-05-28 23:17
legacy (1) vs whatwg (4): 25 rows. Percent-encoding (legacy encoded, whatwg decoded, 50/50 full) and control-char/unicode stripping. Added 2 ex to fragment-unicode-stripping (15/50).

## 2026-05-28 23:19
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:22
legacy (1) vs curl (6): fragment-percent-encoding (50 found, capped), fragment-unicode-stripping (15).

## 2026-05-28 23:25
legacy (1) vs whatwg (7): fragment-percent-encoding (50 capped), multiple-hash-handling, fragment-unicode.

## 2026-05-28 23:39
whatwg (2) vs go-net (3): 25 examples, all fragment-percent-encoding (capped at 50).

## 2026-05-28 23:39
whatwg (2) vs rust-url (4): 25 examples, all fragment-percent-encoding (capped at 50).

## 2026-05-28 23:46
legacy (1) vs go-net (3): 0 differentials.

## 2026-05-28 23:46
legacy (1) vs rust-url (4): 25 sampled; all fragment-percent-encoding (category at 50 examples).

## 2026-05-28 23:48
whatwg (2) vs go-net (3): 25 rows — fragment-percent-encoding (25).

## 2026-05-28 23:51
whatwg (2) vs ada (4): Percent-encoding case + whitespace in fragment, fits fragment-percent-encoding (50/50). 25 rows.
