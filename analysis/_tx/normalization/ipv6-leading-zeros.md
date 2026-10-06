# IPv6 Leading Zero Normalization

**Description:** Parsers disagree on whether to strip leading zeros from individual IPv6 address groups (e.g., 07 vs 7), where one normalizes groups to their minimal representation and the other preserves the original encoding.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-legacy vs rust-url | `data://...@[07:cc:bf:d7:be:1f:F:8]/...` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| java-uri vs rust-url | `https://user@[D:b4:b:7:f:07:24:e0]/` | `[D:b4:b:7:f:07:24:e0]` | `[d:b4:b:7:f:7:24:e0]` |
| rust-url vs php-parseurl | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}𚗐?J08` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:F:8]` |
| js-legacy vs rust-url | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs python-yarl | `ws://4+𧶢54@[e0:1:B:D2:0F:5:1B:E0]0072Ỉ?#` | `[e0:1:b:d2:0f:5:1b:e0]0072Ỉ...` | `e0:1:b:d2:f:5:1b:e0` |
| js-legacy vs python-yarl | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `7:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs rust-url | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `07:cc:bf:d7:be:1f:f:8` |
| js-whatwg vs ruby-addressable | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:F:8]` |
| rust-url vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `07:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs csharp-systemuri | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs csharp-systemuri | `ws://4+񃶢54@[e0:1:B:D2:0F:5:1B:E0]0072Ẹ𯨲𡺴C≧H6PP.9zR04o4a38U25]?#` | `[e0:1:b:d2:0f:5:1b:e0]0072ặ𯨲𡺴c≧h6pp.9zr04o4a38u25]` | `[e0:1:b:d2:f:5:1b:e0]` |
| java-okhttp vs java-uri | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]
y...` | `ff:33:5e:2c:f:a:89:1` | `[FF:33:5E:2C:F:0A:89:1]` |
| java-okhttp vs java-uri | `https://C2K8M34D6H9˦𘐯2h@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[D:b4:b:7:f:07:24:e0]` |
| javascript-legacy vs rust-url | `data://1bK715ChHWkgS83qRd2薆6...@[07:cc:bf:d7:be:1f:F:8]/...` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| python-urllib3 vs python-yarl | `data://...@[07:cc:bf:d7:be:1f:F:8]/...?#` | `7:cc:bf:d7:be:1f:f:8` | `07:cc:bf:d7:be:1f:f:8` |
| python-urllib3 vs python-yarl | `https://...@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:07:24:e0` | `d:b4:b:7:f:7:24:e0` |
| python-urllib3 vs python-yarl | `https://2bW4@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `af:f:ac:d:d:04:4a:43` | `af:f:ac:d:d:4:4a:43` |
| js-whatwg vs rust-url | `data://...@[07:cc:bf:d7:be:1f:F:8]/...` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs rust-url | `...(IPv6 URL with leading zeros)...` | `[07:cc:bf:d7:be:1f:f:8]` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs java-galimatias | `https://C2K8M34D6H9...@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[d:b4:b:7:f:07:24:e0]:8624` |
| rust-url vs python-urllib3 | `data://1bK715ChHWkgS83qRd2...@[07:cc:bf:d7:be:1f:F:8]/...?#` | `07:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| java-url vs rust-url | `http://3C77P6T2z8871:0y@[9F:DE:B:7:E2:6:0C:4]:59556?#` | `[9f:de:b:7:e2:6:c:4]` | `[9F:DE:B:7:E2:6:0C:4]` |
| java-galimatias vs rust-url | `https://5WGP95k2r3A15...@[3:F:04:9:75:B:d:d]:73?...` | `3:f:4:9:75:b:d:d` | `[3:f:4:9:75:b:d:d]` |
| java-galimatias vs rust-url | `wss://Lh...@[8E:1a:0F:b4:d:e:F:9]/./:...` | `8e:1a:f:b4:d:e:f:9` | `[8e:1a:f:b4:d:e:f:9]` |
| java-galimatias vs rust-url | `wss://I2dbX10c7D4Z5p5WK3r...@[Ae:0a:0:B:4:9:0A:2d]:7/...` | `ae:a::b:4:9:a:2d` | `[ae:a:0:b:4:9:a:2d]` |
| java-galimatias vs rust-url | `wss://553de5u44LPLuC40nwL...@[f2:3D:16:Af:8C:2:e:55]:03552?` | `f2:3d:16:af:8c:2:e:55` | `[f2:3d:16:af:8c:2:e:55]` |
| javascript-whatwg vs javascript-legacy | `https://2bW4 
362830@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `[af:f:ac:d:d:4:4a:43]` | `[af:f:ac:d:d:04:4a:43]:8699` |
| javascript-whatwg vs javascript-legacy | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...?` | `[b8:3:ad:ed:f:d:1:5]` | `[b8:3:ad:ed:0f:d:1:5]:52` |
| java-galimatias vs rust-url | `https://2bW4 
362830@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `[af:f:ac:d:d:4:4a:43]` | `[af:f:ac:d:d:04:4a:43]` |
| java-galimatias vs rust-url | `https://...@[a:fB:b5:F6:0E:ab:c2:fa]:622...` | `a:fb:b5:f6:e:ab:c2:fa` | `[a:fb:b5:f6:e:ab:c2:fa]` |
| java-galimatias vs rust-url | `ftp://...:8?...` | `::db:6e:0:dd:ba:a5:6a` | `[0:db:6e:0:dd:ba:a5:6a]` |
| javascript-legacy vs java-galimatias | `https://C2K8M34D6H9...@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[d:b4:b:7:f:07:24:e0]:8624` |
| javascript-legacy vs java-galimatias | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `d4:ab:b5:a:dd:ba:2d:3c` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` |
| javascript-legacy vs java-galimatias | `http://6N47sQ34...@[06:E:E:6:8:7F:9E:61]:39459320/...` | `6:e:e:6:8:7f:9e:61` | `[06:e:e:6:8:7f:9e:61]:39459320` |
| javascript-legacy vs java-galimatias | `ws://V1112A...@[e:B5:f1:e:a6:27:E:B]:025?#` | `[e:b5:f1:e:a6:27:e:b]:025` | `e:b5:f1:e:a6:27:e:b` |
| java-galimatias vs rust-url | `wss://...@[D:72:a:A0:91:a5:6:D1]:8?...` | `xn--gt4vc9sbhs6241bd44w-yo3k` | `[d:72:a:a0:91:a5:6:d1]` |
| java-galimatias vs rust-url | `http://3C77P6T2z8871:0y@[9F:DE:B:7:E2:6:0C:4]:59556?#...` | `9f:de:b:7:e2:6:c:4` | `[9f:de:b:7:e2:6:c:4]` |
| java-galimatias vs rust-url | `ftp://...@[Ff:1:C0:4B:Ad:B:4b:61]:330?...` | `ff:1:c0:4b:ad:b:4b:61` | `[ff:1:c0:4b:ad:b:4b:61]` |
| java-galimatias vs rust-url | `wss://...@[c:Ea:c5:Bc:c5:6d:1b:b]:...` | `c:ea:c5:bc:c5:6d:1b:b` | `[c:ea:c5:bc:c5:6d:1b:b]` |
| java-galimatias vs rust-url | `https://2bW4 ...@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `[af:f:ac:d:d:4:4a:43]` | `[af:f:ac:d:d:04:4a:43]` |
| java-galimatias vs rust-url | `ws://V1112A...@[e:B5:f1:e:a6:27:E:B]:025?#` | `e:b5:f1:e:a6:27:e:b` | `[e:b5:f1:e:a6:27:e:b]` |
| zig-std-uri vs rust-url | `https://2bW4 
362830@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `[AF:F:Ac:D:D:04:4A:43]` | `[af:f:ac:d:d:4:4a:43]` |
| zig-std-uri vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` | `[d4:ab:b5:a:dd:ba:2d:3c]` |
| zig-std-uri vs rust-url | `https://2bW4 
362830@[AF:F:Ac:D:D:04:4A:43]:8699?#` | `[AF:F:Ac:D:D:04:4A:43]` | `[af:f:ac:d:d:4:4a:43]` |
| crystal-uri vs rust-url | `https://C2K8M34D6H9˦𙧲h@[D:b4:b:7:f:07:24:e0]:8624?#` | `[D:b4:b:7:f:07:24:e0]` | `[d:b4:b:7:f:7:24:e0]` |
| crystal-uri vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` | `[d4:ab:b5:a:dd:ba:2d:3c]` |
| zig-std-uri vs csharp-systemuri | `ftp://2yO57b$𑷒kRN2X@[8:eC:2c:31:cc:0D:f:B]02741T54A'LEb`-Vj4*v=6?#` | `[8:ec:2c:31:cc:d:f:b]` | `[8:eC:2c:31:cc:0D:f:B]` |
| zig-std-uri vs csharp-systemuri | `dlna-playsingle://6밡⧏1@[8:8:2:eF:D:00:d9:9]15ACB*159QAorZp5f1^g6?#` | `[8:8:2:ef:d:0:d9:9]` | `[8:8:2:eF:D:00:d9:9]` |
| zig-std-uri vs csharp-systemuri | `http://6B9r5G2G1m{4:fK82p36G1X59@[Ee:B5:03:3:D6:Df:c:2D]801870Z!1EJ6Y81#` | `[ee:b5:3:3:d6:df:c:2d]` | `[Ee:B5:03:3:D6:Df:c:2D]` |
