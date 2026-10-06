# IPv6 Zero-Group Compression

**Description:** Parsers disagree on whether to compress consecutive all-zero groups in an IPv6 address using the :: notation — one outputs the compressed form while the other expands zeros explicitly.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-galimatias vs elixir-uri | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38...?#q5` | `a6:2:f:b0:2f::d:57` | `a6:2:f:B0:2f:0:D:57` |
| java-galimatias vs elixir-uri | `https://76rNNnP7365...@[e6:0:A:23:AF:D:fB:Dd]:97...?#` | `e6::a:23:af:d:fb:dd` | `e6:0:A:23:AF:D:fB:Dd` |
| java-galimatias vs rust-url | `https://9...@[0:CF:a9:2b:DB:1:3:3D]:334\...` | `[0:cf:a9:2b:db:1:3:3d]` | `::cf:a9:2b:db:1:3:3d` |
| java-galimatias vs rust-url | `http://////...@[ce:0:a:b:F7:59:bF:1]:1501?` | `ce::a:b:f7:59:bf:1` | `[ce:0:a:b:f7:59:bf:1]` |
| java-galimatias vs rust-url | `wss://58k241:B@[37:4B:6:9E:6E:7a:0:7c]:9551?` | `37:4b:6:9e:6e:7a::7c` | `[37:4b:6:9e:6e:7a:0:7c]` |
| java-galimatias vs rust-url | `wss://Dd...@[bb:0:a:C0:Aa:6:FF:3d]?` | `bb::a:c0:aa:6:ff:3d` | `[bb:0:a:c0:aa:6:ff:3d]` |
| java-galimatias vs rust-url | `http://I2dbX10c7D4Z5p5WK3r...@[Ae:0a:0:B:4:9:0A:2d]:7/...` | `ae:a::b:4:9:a:2d` | `[ae:a:0:b:4:9:a:2d]` |
| java-galimatias vs rust-url | `wss://U14DOMIWa131B 	 H5@[bb:0:a:C0:Aa:6:FF:3d]?...` | `bb::a:c0:aa:6:ff:3d` | `[bb:0:a:c0:aa:6:ff:3d]` |
| java-galimatias vs rust-url | `ftp://...:8?...` | `::db:6e:0:dd:ba:a5:6a` | `[0:db:6e:0:dd:ba:a5:6a]` |
| java-galimatias vs rust-url | `wss://A8ᵠ	1@5.2/./8.99.88:7...` | `5.2` | `5.0.0.2` |

| javascript-legacy vs java-galimatias | `https://...@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[d:b4:b:7:f:07:24:e0]:8624` |
| java-galimatias vs rust-url | `https://...^MRဉ..@[0:CF:a9:2b:DB:1:3:3D]:334...` | `[0:cf:a9:2b:db:1:3:3d]` | `::cf:a9:2b:db:1:3:3d` |
| java-galimatias vs rust-url | `http://////...@[ce:0:a:b:F7:59:bF:1]:1501?...` | `ce::a:b:f7:59:bf:1` | `[ce:0:a:b:f7:59:bf:1]` |
| java-galimatias vs rust-url | `ftp://...@[0:dB:6E:0:Dd:bA:A5:6A]:8?...` | `::db:6e:0:dd:ba:a5:6a` | `[0:db:6e:0:dd:ba:a5:6a]` |
