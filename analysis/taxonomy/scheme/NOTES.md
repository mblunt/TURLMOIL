
## 2026-05-28 20:23
whatwg (1) vs legacy (2): special-scheme-parsing; whatwg (1) vs deno (3): special-scheme-parsing

## 2026-05-28 20:24
whatwg (1) vs smithy (5): special-scheme-parsing (9 hits)

## 2026-05-28 20:42
whatwg vs legacy: special-scheme-parsing (5 examples) — whatwg preserves wss: and ldaps: schemes, legacy returns random/wrong schemes

## 2026-05-28 20:47
whatwg vs userfriendlyurl: special-scheme-parsing (25) — whatwg recognizes mms/ws as special; userfriendlyurl doesn't

## 2026-05-28 20:48
whatwg vs ansiweburl: (0 results after filtering success/non-null)

## 2026-05-28 20:48
whatwg vs python: special-scheme-parsing (25) — whatwg recognizes wss/ldaps; python prefers others

## 2026-05-28 20:52
uripara vs php-http: special-scheme-parsing (25) — php-http parses wrong scheme

## 2026-05-28 20:53
uripara vs ada: special-scheme-parsing (25) — ada parses wrong scheme

## 2026-05-28 20:53
php-http vs ada: special-scheme-parsing (25) — both parse different schemes for same URL

## 2026-05-28 20:54
uripara vs node: special-scheme-parsing (25) — node parses encoded chars as scheme

## 2026-05-28 21:08
ada vs python: joins consistently timeout

## 2026-05-28 21:12
whatwg vs node-url: timeout on join

## 2026-05-28 21:15
whatwg vs legacy: no differentials found

## 2026-05-28 21:16
whatwg vs legacy: no differentials found

## 2026-05-28 21:19
whatwg vs posix: query timeout (too many results or slow index)

## 2026-05-28 21:20
whatwg vs legacy: 0 results

## 2026-05-28 21:22
whatwg vs legacy: 0 results

## 2026-05-28 21:23
whatwg vs node-url: 0 results

## 2026-05-28 21:25
whatwg vs legacy: 0 results

## 2026-05-28 21:27
whatwg vs go: 0 results

## 2026-05-28 21:29
whatwg vs legacy: 0 results

## 2026-05-28 21:34
whatwg vs ada: 0 results

## 2026-05-28 21:36
whatwg (1) vs trio (3): 0 scheme differentials

## 2026-05-28 21:38
whatwg (1) vs legacy (2): 0 scheme differentials

## 2026-05-28 21:43
legacy (2) vs radix (3): query timeout; skipping pair

## 2026-05-28 22:02
radix (3) vs whatwg (4): query timeout; skipping pair

## 2026-05-28 22:09
whatwg vs whatwg_legacy (2,1): no differentials with both success and non-null scheme

## 2026-05-28 22:09
whatwg vs jsprim (2,4): special-scheme-parsing+5 (mixed case normalization, non-standard schemes)

## 2026-05-28 22:10
whatwg vs legacy (2,6): special-scheme-parsing+5 (scheme terminator colon included in legacy)

## 2026-05-28 22:35
whatwg vs legacy (0,1): 0 diffs | whatwg vs ada (0,2): 0 diffs | legacy vs ada (1,2): timeout

## 2026-05-28 22:49
legacy vs ada: 0 rows

## 2026-05-28 22:49
legacy vs net: 0 rows

## 2026-05-28 22:49
ada vs net: 0 rows

## 2026-05-28 23:05
legacy vs ada: 0 rows

## 2026-05-28 23:06
legacy vs net: 0 rows

## 2026-05-28 23:06
ada vs net: 0 rows

## 2026-05-28 23:08
legacy vs ada: 30 cases in special-scheme-parsing; legacy vs net: 0 rows; ada vs net: 0 rows

## 2026-05-28 23:10
legacy vs net, ada vs net: 0 cases

## 2026-05-28 23:14
legacy (1) vs whatwg (4): 25 rows all case-normalization (lowercasing → uppercase in whatwg scheme), fits existing special-scheme-parsing (full at 30).

## 2026-05-28 23:18
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:20
legacy (1) vs curl (6): scheme-colon-handling (23 examples).

## 2026-05-28 23:41
go-net (3) vs rust-url (4): 25 examples, scheme-case-normalization (8), others likely colon/special parsing (skip).

## 2026-05-28 23:47
whatwg (2) vs go-net (3): 0 differentials.

## 2026-05-28 23:49
whatwg (2) vs ada (4): 25 rows — scheme-case-normalization (25).

## 2026-05-28 23:52
legacy (1) vs whatwg (2): 0 rows.
