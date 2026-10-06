
## 2026-05-28 20:27
whatwg (1) vs legacy (2): password-parsing-error (25 hits)

## 2026-05-28 20:27
whatwg (1) vs parse_uri (3): password-parsing-error (15 hits)

## 2026-05-28 20:28
whatwg (1) vs custom (4): password-parsing-error (25 hits)

## 2026-05-28 20:39
whatwg vs legacy: password-percent-encoding (4 examples) — whatwg preserves/normalizes while legacy applies variable encoding

## 2026-05-28 20:45
whatwg vs legacy: password-percent-encoding (2 examples) — whatwg correctly encodes/returns password; legacy generates random/corrupted percent-encoded strings

## 2026-05-28 20:58
whatwg vs ada: 25 differentials, password-percent-encoding (7 examples)

## 2026-05-28 20:58
whatwg vs node: 25 differentials, password-percent-encoding (8 examples)

## 2026-05-28 21:10
whatwg vs legacy: password-percent-encoding (samples exist, not added)

## 2026-05-28 21:14
whatwg vs node-url: no differentials found

## 2026-05-28 21:16
whatwg vs legacy: no differentials found

## 2026-05-28 21:17
whatwg vs legacy: no differentials found

## 2026-05-28 21:19
whatwg vs posix: no differentials found

## 2026-05-28 21:21
whatwg vs legacy: 0 results

## 2026-05-28 21:22
whatwg vs legacy: 0 results

## 2026-05-28 21:24
whatwg vs node-url: 0 results

## 2026-05-28 21:26
whatwg vs legacy: 0 results

## 2026-05-28 21:27
whatwg vs go: 0 results

## 2026-05-28 21:30
whatwg vs legacy: 0 results

## 2026-05-28 21:34
whatwg vs ada: 0 results

## 2026-05-28 21:34
whatwg vs legacy: 0 results

## 2026-05-28 21:37
whatwg (1) vs trio (3): 0 password differentials

## 2026-05-28 21:38
whatwg (1) vs legacy (2): 0 password differentials

## 2026-05-28 21:44
legacy (2) vs radix (3): 0 password differentials

## 2026-05-28 22:04
radix (3) vs whatwg (4): 25 samples; password-percent-encoding dominant, password-parsing-error also present

## 2026-05-28 22:17
legacy vs node (3,4): password-percent-encoding (14 found, 8 existing), password-parsing-error; skipped—mostly double-parsing or userinfo bleed issues

## 2026-05-28 22:17
legacy vs rust (3,5): 0 diffs

## 2026-05-28 22:18
node vs rust (4,5): query timeout—skipping

## 2026-05-28 22:20
whatwg vs legacy (2,3): 0 diffs

## 2026-05-28 22:21
whatwg vs node (2,4): query timeout—skipping

## 2026-05-28 22:21
whatwg vs rust (2,5): 0 diffs

## 2026-05-28 22:21
legacy vs node (3,4): 20 diffs, all password-percent-encoding

## 2026-05-28 22:21
legacy vs rust (3,5): 0 diffs

## 2026-05-28 22:22
node vs rust (4,5): query timeout—skipping

## 2026-05-28 22:33
whatwg vs legacy (0,1): 0 diffs | whatwg vs ada (0,2): 0 diffs | legacy vs ada (1,2): 0 diffs

## 2026-05-28 22:34
whatwg vs legacy (0,1): 0 diffs | whatwg vs ada (0,2): 0 diffs | legacy vs ada (1,2): 0 diffs

## 2026-05-28 22:40
All pairs exhausted: 0 new diffs. password-parsing-error (4) + password-percent-encoding (13) = 17 examples total covered.

## 2026-05-28 22:50
legacy vs ada: 0 rows

## 2026-05-28 22:51
legacy vs net: 0 rows

## 2026-05-28 22:51
ada vs net: 0 rows

## 2026-05-28 22:58
legacy vs ada: 0 rows

## 2026-05-28 22:58
legacy vs net: 0 rows

## 2026-05-28 22:58
ada vs net: 0 rows

## 2026-05-28 22:59
legacy vs ada: 0 rows

## 2026-05-28 22:59
legacy vs net: 0 rows

## 2026-05-28 22:59
ada vs net: 0 rows

## 2026-05-28 23:07
legacy vs ada: 0 rows; legacy vs net: insufficient data; ada vs net: 0 rows

## 2026-05-28 23:10
legacy vs net, ada vs net: 0 cases

## 2026-05-28 23:16
legacy (1) vs whatwg (4): 25 rows. Mostly percent-encoding (legacy encoded, whatwg decoded); some parsing boundaries. Added 2 ex to password-percent-encoding (15/50).

## 2026-05-28 23:18
legacy (1) vs regexes (5): 0 rows.

## 2026-05-28 23:22
legacy (1) vs curl (6): 0 rows.

## 2026-05-28 23:24
legacy (1) vs whatwg (7): password-percent-encoding (15), new: ampersand vs comma encoding.

## 2026-05-28 23:31
legacy (1) vs rust-url (4): 20+ password-percent-encoding (most entries are partial extraction)

## 2026-05-28 23:31
go-net (3) vs rust-url (4): 20+ password-percent-encoding (percent-encoded vs raw unicode)

## 2026-05-28 23:35
go-net (3) vs rust-url (4): 25 examples, password-percent-encoding (go-net encodes userinfo spill, rust-url extracts/truncates)

## 2026-05-28 23:44
whatwg (2) vs go-net (3): 0 differentials.

## 2026-05-28 23:44
whatwg (2) vs rust-url (4): 0 differentials.

## 2026-05-28 23:44
go-net (3) vs rust-url (4): 25 examples all password-percent-encoding (23 existing, skip).

## 2026-05-28 23:48
whatwg (2) vs go-net (3): 0 differentials.

## 2026-05-28 23:50
whatwg (2) vs ada (4): 0 rows.
