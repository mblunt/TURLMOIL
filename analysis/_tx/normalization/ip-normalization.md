# IP Normalization

**Description:** One parser expands hex/octal/dotless IP addresses to standard dotted-decimal notation while the other leaves them as-is.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `https://JxUSvT@99.93.4.62:22F56@00?` | `0.0.0.0` | `00` |
| whatwg vs legacy | `http://n@3/..` | `0.0.0.3` | `3` |
| whatwg vs legacy | `http://2?@[eC:F:c:F:AA:6B:C1:A3]:1057#` | `0.0.0.2` | `2` |
| whatwg vs legacy | `https://7#` | `0.0.0.7` | `7` |
| whatwg vs legacy | `http://n@3/.8:311` | `0.0.0.3` | `3` |
| whatwg vs legacy | `https://zy|a@2.6.29?#.47:1` | `2.6.29` | `2.6.0.29` |
| whatwg vs legacy | `https://tn27@53123/..8:311` | `0.0.207.131` | `53123` |
| whatwg vs legacy | `wss://853?#vU9o` | `853` | `0.0.3.85` |
| whatwg vs legacy | `data://B8TTO@36.65.0.102452秖𨭂}j6393c3x0Gn783Do14?#` | `36.65.0.102452%E7%A7%96%F0%A8%AD%82}j6393c3x0Gn783Do14` | `36.65.0.xn--102452-ur1p66994a` |
| whatwg vs legacy | `https://4@3.97.6/..34:6` | `3.97.0.6` | `3.97.6` |
| javascript-whatwg vs javascript-legacy | `https://JxUSv@99.93.4.62:22F56@00?` | `0.0.0.0` | `00` |
| javascript-whatwg vs javascript-legacy | `wss://853?#` | `0.0.3.85` | `853` |
| javascript-whatwg vs javascript-legacy | `http://n@3/..` | `0.0.0.3` | `3` |
| javascript-whatwg vs javascript-legacy | `http://2?` | `0.0.0.2` | `2` |
| javascript-whatwg vs javascript-legacy | `https://7#` | `0.0.0.7` | `7` |
| javascript-whatwg vs javascript-legacy | `https://53123/..8:` | `0.0.207.131` | `53123` |
| javascript-whatwg vs javascript-legacy | `https://a@3.97.6/..` | `3.97.0.6` | `3.97.6` |
| javascript-whatwg vs javascript-legacy | `https://v7j@2.6.29?#` | `2.6.29` | `2.6.0.29` |
| javascript-whatwg vs javascript-parse-uri | `wss://853?#` | `853` | `0.0.3.85` |
| javascript-whatwg vs javascript-parse-uri | `https://6.2/...` | `6.0.0.2` | `6.2` |
| javascript-whatwg vs javascript-uri-js | `https://7#` | `0.0.0.7` | `7` |
| javascript-whatwg vs javascript-uri-js | `https://53123/..8:` | `0.0.207.131` | `53123` |
| javascript-whatwg vs javascript-uri-js | `https://a@3.97.6/..` | `3.97.0.6` | `3.97.6` |
| javascript-whatwg vs javascript-url-parse | `https://zy...@2.6.29?...` | `2.6.0.29` | `2.6.29` |
| javascript-whatwg vs javascript-urijs | `https://zy...@2.6.29?...` | `2.6.29` | `2.6.0.29` |
| javascript-whatwg vs go-net | `wss://853?#` | `853` | `0.0.3.85` |
| javascript-whatwg vs go-net | `https://2?#` | `2` | `0.0.0.2` |
| javascript-whatwg vs go-net | `https://7/...` | `7` | `0.0.0.7` |
| js-whatwg vs elixir-uri | `https://JxUSvT@99.93.4.62:22F56^<o?@00?"U` | `00` | `0.0.0.0` |
| js-whatwg vs elixir-uri | `wss://853?#vU9o0jE...0:90s` | `853` | `0.0.3.85` |
| js-whatwg vs python-urllib3 | `https://JxUS...@00?...` | `0.0.0.0` | `00` |
| rust-url vs python-urllib3 | `(URL with dotless IP host '00')` | `00` | `0.0.0.0` |
| rust-url vs python-urllib3 | `(URL with 3-part IP host '2.6.29')` | `2.6.29` | `2.6.0.29` |
| rust-url vs python-urllib3 | `(URL with 3-part IP host '3.97.6')` | `3.97.6` | `3.97.0.6` |
| javascript-legacy vs rust-url | `https://tn27Oy6074Wb]...@53123/...` | `53123` | `0.0.207.131` |
| js-whatwg vs python-yarl | `https://...@2.6.29?#...` | `2.6.0.29` | `2.6.29` |
| js-whatwg vs python-yarl | `https://4⦽ v7j@3.97.6/...` | `3.97.0.6` | `3.97.6` |
| java-galimatias vs rust-url | `https://...@00?...` | `00` | `0.0.0.0` |
| java-galimatias vs rust-url | `https://...@2.6.29?#...` | `2.6.0.29` | `2.6.29` |
| java-galimatias vs rust-url | `https://...@3.97.6/...` | `3.97.6` | `3.97.0.6` |
| java-galimatias vs rust-url | `http://...@53123?...` | `53123` | `0.0.207.131` |
| java-galimatias vs rust-url | `ws://...@6.2/...` | `6.2` | `6.0.0.2` |
| java-galimatias vs rust-url | `http://...@41/...` | `0.0.0.41` | `41` |
| go-net vs rust-url | `...@853...` | `853` | `0.0.3.85` |
| go-net vs rust-url | `...@2...` | `2` | `0.0.0.2` |
| go-net vs rust-url | `...@7...` | `7` | `0.0.0.7` |
| go-net vs rust-url | `...@5810...` | `5810` | `0.0.22.178` |
| perl-uri vs rust-url | `https://...@00...` | `00` | `0.0.0.0` |
| perl-uri vs rust-url | `...@853...` | `853` | `0.0.3.85` |
| elixir-uri vs python-urllib3 | `...(dotless IP)...` | `853` | `0.0.3.85` |
