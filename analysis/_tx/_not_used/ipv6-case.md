# IPv6 Address Case Normalization

**Description:** Parsers disagree on the case of hexadecimal digits in IPv6 addresses — one normalizes to lowercase (or uppercase) while the other preserves the original case or uses a different convention.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-uri vs rust-url | `https://user@[DA:DA:BD:9:8:1f:c8:EB]/` | `[da:da:bd:9:8:1f:c8:eb]` | `[DA:DA:BD:9:8:1f:c8:EB]` |
| java-uri vs rust-url | `data://user@[d4:Ab:B5:A:dD:Ba:2d:3C]/` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` |
| go-net vs csharp-systemuri | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| go-net vs python-urllib3 | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `d4:ab:b5:a:dd:ba:2d:3c` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| rust-url vs php-parseurl | `dntp://F70_9𣳽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `[D:C:a1:cE:b:33:D:f]` | `[d:c:a1:ce:b:33:d:f]` |
| js-legacy vs java-uri | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[da:da:bd:9:8:1f:c8:eb]` | `[DA:DA:BD:9:8:1f:c8:EB]` |
| go-net vs python-urllib3 | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `da:da:bd:9:8:1f:c8:eb` |
| js-whatwg vs go-net | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| js-whatwg vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| js-legacy vs elixir-uri | `file://T7srLRM12dnM3jP9u66a@[F1:9c:cD:f4:75:43:67:4AJpc]:	 ⩱䪰𗃢
`🀑📟 Ax`79`a;PW29&~53H?#` | `[f1:9c:cd:f4:75:43:67:4ajpc]` | `F1:9c:cD:f4:75:43:67:4AJpc` |
| go-net vs python-yarl | `data://X2:Hcyf@[64:9:6:e:6:2:d:B]/./:0959330tU676WFWJ41894G"?#` | `64:9:6:e:6:2:d:b` | `64:9:6:e:6:2:d:B` |
| js-legacy vs go-net | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| js-legacy vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| js-whatwg vs ruby-addressable | `data://1bK715ChHWkgS83qRd2薆蕦93zD725@[07:cc:bf:d7:be:1f:F:8]/}` | `[7:cc:bf:d7:be:1f:f:8]` | `[07:cc:bf:d7:be:1f:F:8]` |
| js-whatwg vs ruby-addressable | `dntp://F70_9𠃽Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `[D:C:a1:cE:b:33:D:f]` | `[d:c:a1:ce:b:33:d:f]` |
| js-whatwg vs ruby-addressable | `ms-settings-airplanemode://Z5j5Pu732c04yq.񌓠	츭'~⃭911@[7:E:63:5D:C8:8B:cA:82]/..:56{⅁334=10g322*0(45C8T4?#` | `[7:E:63:5D:C8:8B:cA:82]` | `[7:e:63:5d:c8:8b:ca:82]` |
| go-net vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| java-okhttp vs java-uri | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]
y𠔅\06}...` | `ff:33:5e:2c:f:a:89:1` | `[FF:33:5E:2C:F:0A:89:1]` |
| java-okhttp vs java-uri | `https://C2K8M34D6H9˦𘐯2h@[D:b4:b:7:f:07:24:e0]:8624?#` | `d:b4:b:7:f:7:24:e0` | `[D:b4:b:7:f:07:24:e0]` |
| java-uri vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `[DA:DA:BD:9:8:1f:c8:EB]` |
| java-uri vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` |
| java-uri vs rust-url | `https://C2K8M34D6H9...@[D:b4:b:7:f:07:24:e0]:8624` | `[D:b4:b:7:f:07:24:e0]` | `[d:b4:b:7:f:7:24:e0]` |
| go-net vs python-urllib3 | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `DA:DA:BD:9:8:1f:c8:EB` | `da:da:bd:9:8:1f:c8:eb` |
| java-galimatias vs elixir-uri | `ftp://1S9L=...@[a6:2:f:B0:2f:0:D:57]?#` | `a6:2:f:b0:2f::d:57` | `a6:2:f:B0:2f:0:D:57` |
| java-galimatias vs elixir-uri | `...(URL with mixed-case IPv6)...` | `ff:33:5e:2c:f:a:89:1` | `FF:33:5E:2C:F:0A:89:1` |
| java-galimatias vs elixir-uri | `...(URL with mixed-case IPv6)...` | `e6::a:23:af:d:fb:dd` | `e6:0:A:23:AF:D:fB:Dd` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| go-net vs python-urllib3 | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `DA:DA:BD:9:8:1f:c8:EB` | `da:da:bd:9:8:1f:c8:eb` |
| go-net vs python-urllib3 | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `d4:ab:b5:a:dd:ba:2d:3c` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| java-url vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` |
| java-url vs rust-url | `https://C2K8M34D6H9...@[D:b4:b:7:f:07:24:e0]:8624?#` | `[D:b4:b:7:f:07:24:e0]` | `[d:b4:b:7:f:7:24:e0]` |
| java-url vs rust-url | `http://3C77P6T2z8871:0y@[9F:DE:B:7:E2:6:0C:4]:59556?#` | `[9f:de:b:7:e2:6:c:4]` | `[9F:DE:B:7:E2:6:0C:4]` |
| go-net vs rust-url | `data://X2:Hcyf@[64:9:6:e:6:2:d:B]/./:0959330tU676WFWJ41894G"?#` | `64:9:6:e:6:2:d:B` | `[64:9:6:e:6:2:d:b]` |
| go-net vs rust-url | `data://M5U31AQ0VnX43@[a9:EB:F:F:C1:8:c7:38]:231?#}` | `a9:EB:F:F:C1:8:c7:38` | `[a9:eb:f:f:c1:8:c7:38]` |
| go-net vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| go-net vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...` | `[da:da:bd:9:8:1f:c8:eb]` | `DA:DA:BD:9:8:1f:c8:EB` |
| zig-std-uri vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[DA:DA:BD:9:8:1f:c8:EB]` | `[da:da:bd:9:8:1f:c8:eb]` |
| zig-std-uri vs rust-url | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/27e3434$3hupSZH98t7#` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` | `[d4:ab:b5:a:dd:ba:2d:3c]` |
| zig-std-uri vs rust-url | `ftp://c7ZE`12@9FP.8.108a6Es0mNc958171BTV3y_8o2xeOkZgw6pN#` | `[ea:7:d:cf:Be:D:aD:f]:07.y87ZfC8284jj293s04` | `[ea:7:d:cf:be:d:ad:f]` |
| zig-std-uri vs rust-url | `https://4N67nvv13/../75vaqW91L2𬑑1r1m75@[D:A9:4:fb:F:8:40:8]64j8U838kLz6e6jSOeL6^?#` | `4N67nvv13` | `4n67nvv13` |
| zig-std-uri vs rust-url | `wss://79049h@R-650i3B`bnb7jn8CK8ae044?#` | `R-650i3B`bnb7jn8CK8ae044` | `r-650i3b`bnb7jn8ck8ae044` |
| csharp-systemuri vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `DA:DA:BD:9:8:1f:c8:EB` | `[da:da:bd:9:8:1f:c8:eb]` |
| go-net vs rust-url | `ws://Fz5I56GS16533di62us~?N@[EA:7:d:cf:Be:D:aD:f]:07.y87ZfC8284jj293s04?#` | `fz5i56gs16533di62us~` | `Fz5I56GS16533di62us~` |
| csharp-systemuri vs rust-url | `ms-sttoverlay://17Wnꖈ/OY[d:7:7:c4:2d:6E:F7:A]:629q30fR5e5fiwva9fPsIx?#` | `17Wnꖈ` | `17Wn%F3%B6%A5%88` |
| crystal-uri vs rust-url | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[da:da:bd:9:8:1f:c8:eb]` | `[DA:DA:BD:9:8:1f:c8:EB]` |
| crystal-uri vs rust-url | `dntp://F70_9퐏�Qh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `[D:C:a1:cE:b:33:D:f]` | `[d:c:a1:ce:b:33:d:f]` |
| crystal-uri vs rust-url | `http://1wlP4lEQf186I47ODj28籂˘⬁a9nf2l7@[1E:BF:fa:eC:2E:D:C:26]:502?#` | `[1E:BF:fa:eC:2E:D:C:26]` | `[1e:bf:fa:ec:2e:d:c:26]` |
| zig-std-uri vs csharp-systemuri | `snews://9e28Kdug@[c:C:D6:5:d:8:a:6e]70ArG6vn776VI0_de919f?#` | `[c:C:D6:5:d:8:a:6e]` | `[c:c:d6:5:d:8:a:6e]` |
| zig-std-uri vs csharp-systemuri | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `[DA:DA:BD:9:8:1f:c8:EB]` | `[da:da:bd:9:8:1f:c8:eb]` |
