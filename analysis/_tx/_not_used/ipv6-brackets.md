# IPv6 Bracket Handling

**Description:** Parsers disagree on whether to include or strip the square brackets surrounding an IPv6 address in the host field, or disagree on the leading-zero representation of groups.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `data://1bK715ChHWkgS83qRd2@[07:cc:bf:d7:be:1f:F:8]/}?#` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:f:8]` |
| javascript-whatwg vs javascript-legacy | `data://1bK715@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:f:8]` |
| javascript-whatwg vs javascript-uri-js | `cvs://...@[DA:DA:BD:9:8:1f:c8:EB]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `da:da:bd:9:8:1f:c8:eb` |
| javascript-whatwg vs javascript-uri-js | `http://...@[1E:BF:fa:eC:2E:D:C:26]:502` | `[1e:bf:fa:ec:2e:d:c:26]` | `1e:bf:fa:ec:2e:d:c:26` |
| javascript-whatwg vs go-net | `cvs://...@[DA:DA:BD:9:8:1f:c8:EB]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| javascript-whatwg vs go-net | `data://[d4:Ab:B5:A:dD:Ba:2d:3C]:...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| javascript-legacy vs javascript-uri-js | `ws://4+...@[e0:1:B:D2:0F:5:1B:E0]0072...#` | `[e0:1:b:d2:0f:5:1b:e0]0072ệ󩶲𡶴c≧h6pp.9zr04o4a38u25]` | `e0:1:b:d2:f:5:1b:e0` |
| java-okhttp vs java-uri | `https://[FF:33:5E:2C:F:0A:89:1]/...` | `ff:33:5e:2c:f:a:89:1` | `[FF:33:5E:2C:F:0A:89:1]` |
| java-okhttp vs java-uri | `https://[1d:2:Ce:8F:4:5a:E:2]/...` | `1d:2:ce:8f:4:5a:e:2` | `[1d:2:Ce:8F:4:5a:E:2]` |
| java-okhttp vs java-uri | `https://[D:b4:b:7:f:07:24:e0]/...` | `d:b4:b:7:f:7:24:e0` | `[D:b4:b:7:f:07:24:e0]` |
| javascript-legacy vs go-net | `data://[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| javascript-legacy vs go-net | `cvs://[DA:DA:BD:9:8:1f:c8:EB]/...` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| javascript-legacy vs python-urllib3 | `https://[07:cc:bf:d7:be:1f:f:8]/...` | `07:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs python-urllib3 | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `07:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs python-yarl | `dntp://F70_9𠃽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `d:c:a1:ce:b:33:d:f` | `[d:c:a1:ce:b:33:d:f]:42256` |
| js-legacy vs python-yarl | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `7:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs python-yarl | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `7:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs python-yarl | `dntp://F70_9𠃽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `d:c:a1:ce:b:33:d:f` | `[d:c:a1:ce:b:33:d:f]` |
| js-whatwg vs go-net | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| js-whatwg vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| rust-url vs python-yarl | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `7:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| rust-url vs python-yarl | `dntp://F70_9𠃽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `d:c:a1:ce:b:33:d:f` | `[d:c:a1:ce:b:33:d:f]` |
| js-legacy vs go-net | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| js-legacy vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| js-legacy vs python-urllib3 | `data://1bK715ChHWkgS83qRd2蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `07:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-legacy vs python-urllib3 | `dntp://F70_9𠃽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `d:c:a1:ce:b:33:d:f` | `[d:c:a1:ce:b:33:d:f]:42256` |
| js-legacy vs python-urllib3 | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `da:da:bd:9:8:1f:c8:eb` | `[da:da:bd:9:8:1f:c8:eb]` |
| js-legacy vs python-urllib3 | `http://1wlP4lEQf186I47ODj28粂˘⮁a9nf2l7@[1E:BF:fa:eC:2E:D:C:26]:502?#` | `[1e:bf:fa:ec:2e:d:c:26]:502` | `1e:bf:fa:ec:2e:d:c:26` |
| js-whatwg vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `07:cc:bf:d7:be:1f:f:8` |
| js-whatwg vs python-urllib3 | `unknown://...@[7:e:63:5d:c8:8b:ca:82]/...` | `7:e:63:5d:c8:8b:ca:82` | `[7:e:63:5d:c8:8b:ca:82]` |
| js-whatwg vs python-urllib3 | `unknown://...@[da:da:bd:9:8:1f:c8:eb]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `da:da:bd:9:8:1f:c8:eb` |
| go-net vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| rust-url vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `07:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| java-okhttp vs java-uri | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]
y𠔅\06}...` | `ff:33:5e:2c:f:a:89:1` | `[FF:33:5E:2C:F:0A:89:1]` |
| java-okhttp vs java-uri | `https://32P8B@[1d:2:Ce:8F:4:5a:E:2]:1753
Elx1=0vX16nfR12L9W}?#` | `1d:2:ce:8f:4:5a:e:2` | `[1d:2:Ce:8F:4:5a:E:2]` |
| java-okhttp vs java-uri | `https://C2K8M34D6H9˦𘐯2h@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[D:b4:b:7:f:07:24:e0]` |
| js-legacy vs python-hyperlink | `data://1bK715ChHWkgS83qRd2薆9zD725@[07:cc:bf:d7:be:1f:F:8]/}...` | `07:cc:bf:d7:be:1f:F:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| js-whatwg vs python-hyperlink | `data://1bK715ChHWkgS83qRd2薆9zD725@[07:cc:bf:d7:be:1f:F:8]/}...` | `[7:cc:bf:d7:be:1f:f:8]` | `07:cc:bf:d7:be:1f:F:8` |
| js-whatwg vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆9zD725@[07:cc:bf:d7:be:1f:F:8]/}...` | `[7:cc:bf:d7:be:1f:f:8]` | `07:cc:bf:d7:be:1f:f:8` |
| go-net vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| js-whatwg vs go-net | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| js-whatwg vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| go-net vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| rust-url vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆6...@[07:cc:bf:d7:be:1f:F:8]/...` | `07:cc:bf:d7:be:1f:f:8` | `[7:cc:bf:d7:be:1f:f:8]` |
| javascript-legacy vs python-urllib3 | `data://1bK715ChHWkgS83qRd2薆6...@[07:cc:bf:d7:be:1f:F:8]/...` | `07:cc:bf:d7:be:1f:f:8` | `[07:cc:bf:d7:be:1f:f:8]` |
| javascript-legacy vs python-urllib3 | `dntp://F70_9...@[D:C:a1:cE:b:33:D:f]:42256/...` | `d:c:a1:ce:b:33:d:f` | `[d:c:a1:ce:b:33:d:f]:42256` |
| go-net vs rust-url | `(URL with IPv6 host [64:9:6:e:6:2:d:B])` | `64:9:6:e:6:2:d:B` | `[64:9:6:e:6:2:d:b]` |
