
## 2026-05-27 22:12
## Progress Log

- **1 (javascript-whatwg) vs 2 (javascript-legacy)**: dot-segment-resolution, percent-encoding, whitespace-handling, backslash-normalisation
- **1 (javascript-whatwg) vs 3 (javascript-uri-js)**: dot-segment-resolution, percent-encoding, whitespace-handling, backslash-normalisation, surrogate-pair-encoding
- **1 (javascript-whatwg) vs 7 (javascript-url-parse)**: dot-segment-resolution, percent-encoding, whitespace-handling, backslash-normalisation, double-slash-collapse
- **1 (javascript-whatwg) vs 8 (javascript-urijs)**: dot-segment-resolution, percent-encoding, whitespace-handling
- **1 (javascript-whatwg) vs 9 (javascript-fast-url-parser)**: dot-segment-resolution, percent-encoding, whitespace-handling, backslash-normalisation
- **1 (javascript-whatwg) vs 10 (javascript-fast-uri)**: surrogate-pair-encoding (%uXXXX format), dot-segment-resolution, whitespace-handling, double-slash-collapse
- **1 (javascript-whatwg) vs 11 (javascript-parse-url)**: no results
- **1 (javascript-whatwg) vs 29 (cpp-ada-url)**: no results
- **48 (go-net) vs 59 (rust-url)**: dot-segment-resolution, percent-encoding, backslash-normalisation, double-slash-collapse
- **56 (csharp-systemuri) vs 59 (rust-url)**: whitespace-handling, backslash-normalisation, dot-segment-resolution
- **59 (rust-url) vs 66 (elixir-uri)**: dot-segment-resolution, percent-encoding, whitespace-handling
- **86 (python-urllib3) vs 87 (python-yarl)**: percent-encoding-normalization (double-encoded %25XX decoded)
- **2 (javascript-legacy) vs 7 (javascript-url-parse)**: whitespace-handling (CR stripping vs preserving)
- **2 (javascript-legacy) vs 8 (javascript-urijs)**: whitespace-handling, percent-encoding


## 2026-05-27 22:53
cpp-poco-uri (30) vs rust-url (59): dot-segment-resolution (poco leaves .., rust resolves), percent-encoding (rust encodes unicode, poco leaves raw), whitespace-handling (rust strips CR/LF, poco keeps). ~20 diffs.
javascript-uri-js (6) vs javascript-whatwg (1): 0 diffs found.
csharp-systemuri (56) vs elixir-uri (66): whitespace-handling (CR/LF encoding diffs), percent-encoding (csharp encodes, elixir leaves raw). ~20 diffs.
javascript-legacy (2) vs csharp-systemuri (56): whitespace-handling, percent-encoding, backslash-normalisation. ~20 diffs.
javascript-whatwg (1) vs elixir-uri (66): percent-encoding (whatwg encodes, elixir raw), whitespace-handling. ~20 diffs.
python-yarl (87) vs python-furl (88): percent-encoding-normalization (furl double-decodes %25XX, yarl double-encodes). ~10 diffs.
rust-url (59) vs python-urllib3 (86): dot-segment-resolution, percent-encoding. ~10 diffs.
go-net (48) vs python-yarl (87): timeout — no data found.
perl-uri (46) vs go-net (48): percent-encoding (perl raw, go encodes), backslash-normalisation, percent-encoding-normalization. ~15 diffs.
cpp-ada-url (29) vs rust-url (59): percent-encoding (caret ^), double-slash-collapse (file:///). ~15 diffs.
crystal-uri (26) vs rust-url (59): dot-segment-resolution, percent-encoding, whitespace-handling. ~15 diffs.
ruby-uri (69) vs go-net (48): 0 diffs.
ruby-addressable (70) vs go-net (48): 0 diffs.
java-okhttp (49) vs rust-url (59): percent-encoding (caret), whitespace-handling. ~10 diffs.
python-urllib3 (86) vs python-furl (88): percent-encoding-normalization (double-encoding). ~10 diffs.
python-urllib3 (86) vs python-rfc3986 (90): percent-encoding-normalization. ~5 diffs.
php-parseurl (71) vs rust-url (59): 0 diffs.
erlang-uri-string (83) vs rust-url (59): 0 diffs.
cpp-poco-uri (30) vs rust-url (59): dot-segment-resolution, percent-encoding, whitespace-handling. ~15 diffs.
