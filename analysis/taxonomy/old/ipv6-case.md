# IPv6 Case Normalization

**Description:** IPv6 hex digits are returned in different cases (upper vs lower) by different parsers

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-url | `snews://H9Ex󵝙V窹
%4􁨘𩵧hY5LcF@[3:3:b:3B:8E:d:69:f]:84\b1G9258{53$De1Mp28?#` | `` | `[3:3:b:3b:8e:d:69:f]` |
| javascript-whatwg vs rust-url | `data://7c6R	9󝛩􆟭L2@[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `` | `[70:d:c:f3:84:ca:8:a]` |
| javascript-whatwg vs rust-url | `Oplatformnews://yaq8LAjve0Bi3wMPRm55LE@[9f:e:2b:6:e8:cC:86:8]:96\𡄶	0ykdJiJ7juM5kLJv491M?#jM~2=^z[` | `` | `[9f:e:2b:6:e8:cc:86:8]` |
| javascript-whatwg vs rust-url | `Tms-media-stream-idX://WKAr:@[e:fa:b:0:4:6:f0:d]:2992\0ab7e3FM145?#U6#853@93&` | `` | `[e:fa:b:0:4:6:f0:d]` |
| javascript-whatwg vs rust-url | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:\96{򀐪'6/62쫓񂾁❺3v13Y󴠕?#*+kJ` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
| javascript-whatwg vs rust-url | `data://J65
=23AUT@[a7:9E:3:D:4F:9e:bC:53]:182\DW$=hQDMGG5661^59?#` | `` | `[a7:9e:3:d:4f:9e:bc:53]` |
| javascript-whatwg vs rust-url | `ms-useractivityset://nED44vvK@[eb:D5:3:c:e:F2:4:0d]:00\63oX549XdB4J697Sw2?` | `` | `[eb:d5:3:c:e:f2:4:d]` |
| javascript-whatwg vs rust-url | `teamspeak://8Hl03dr5f4LMRr12182+|	𱴡e65v6@[E:2e:1:e0:4:a:7:EA]:7067\B3SQb55q39qME7j9?#` | `` | `[e:2e:1:e0:4:a:7:ea]` |
| javascript-whatwg vs rust-url | `data://7┲읝⩼s5D@⟟SḪ@97v69↭黝@[5:30:6:4:2:c6:f2:77]:	\󀓵b546+Y0+xr6C60dD,83?#` | `` | `[5:30:6:4:2:c6:f2:77]` |
| javascript-whatwg vs javascript-uri-js | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063?` | `` | `e6:a0:bc:f:a:9f:d:a` |
| javascript-whatwg vs javascript-deno | `snews://H9Ex@[3:3:b:3B:8E:d:69:f]:84?` | `` | `[3:3:b:3b:8e:d:69:f]` |
| javascript-whatwg vs javascript-uri-js | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| rust-url vs rust-urlparse | `beshare://2406TUm7F68SmK2m3a/...@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406tum7f68smk2m3a` | `2406TUm7F68SmK2m3a` |
| rust-url vs rust-urlparse | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `e6:a0:bc:f:a:9f:d:a` | `E6:A0:Bc:F:a:9F:d:a` |
| rust-url vs rust-urlparse | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?4?#` | `8f:d8:2f:4a:c2:67:26:50` | `8f:D8:2f:4A:C2:67:26:50` |
| elixir-uri vs elixir-ex_url | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `E6:A0:Bc:F:a:9F:d:a` | `` |
| elixir-uri vs elixir-ex_url | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?#` | `8f:D8:2f:4A:C2:67:26:50` | `` |
| erlang-uri-string vs erlang-hackney-url | `http://01@[76:d:7e:8:6E:3c:5:a]:494...?#B5g+6E;M` | `` | `76:d:7e:8:6E:3c:5:a` |
| erlang-uri-string vs erlang-hackney-url | `snmp://7c8@[f:35:91:49:B8:c5:dA:cd]:426?#` | `` | `f:35:91:49:B8:c5:dA:cd` |
| erlang-uri-string vs erlang-hackney-url | `http://R8I5235G@[E:A4:e0:1:7:B8:d:86]:963...?#` | `` | `E:A4:e0:1:7:B8:d:86` |
| python-urllib3 vs python-yarl | `https://1Yg7@[8D:e9:e:c:66:e:EC:D1]14...?#` | `8d:e9:e:c:66:e:ec:d1` | `` |
| python-urllib3 vs python-yarl | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]...?` | `ff:33:5e:2c:f:a:89:1` | `` |
| python-urllib3 vs python-yarl | `https://TDT1@[D6:C:e3:E2:2:A:c5:2]6...?#` | `d6:c:e3:e2:2:a:c5:2` | `` |
| java-uri vs java-galimatias | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]...?` | `ff:33:5e:2c:f:a:89:1` | `[FF:33:5E:2C:F:0A:89:1]` |
| go-net vs java-okhttp | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38...?#q5` | `[a6:2:f:B0:2f:0:D:57]` | `a6:2:f:b0:2f::d:57` |
| java-uri vs java-galimatias | `https://1Yg7@[8D:e9:e:c:66:e:EC:D1]14...?#` | `8d:e9:e:c:66:e:ec:d1` | `` |
| java-spring-web vs java-apache-httpclient | `https://1Yg7@[8D:e9:e:c:66:e:EC:D1]14...?#` | `[8d:e9:e:c:66:e:ec:d1]` | `` |
| java-spring-web vs java-apache-httpclient | `https://TDT1@[D6:C:e3:E2:2:A:c5:2]...?#` | `[d6:c:e3:e2:2:a:c5:2]` | `` |
| rust-url vs rust-http | `cvs://4FJ27Ov@[DA:DA:BD:9:8:1f:c8:EB]/...?#` | `[da:da:bd:9:8:1f:c8:eb]` | `[DA:DA:BD:9:8:1f:c8:EB]` |
| rust-url vs rust-http | `ftp://64ny5g@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517?#` | `[d4:Ab:B5:A:dD:Ba:2d:3C]` | `[d4:ab:b5:a:dd:ba:2d:3c]` |
| rust-url vs rust-http | `data://Kqtf14@[79:42:Ef:E:eC:b:db:Eb]:5961?#` | `[79:42:Ef:E:eC:b:db:Eb]` | `[79:42:ef:e:ec:b:db:eb]` |
| rust-url vs rust-http | `data://a08Azc@[F8:E1:d:06:B:B:08:67]:6120?#B` | `[F8:E1:d:06:B:B:08:67]` | `[f8:e1:d:6:b:b:8:67]` |
| rust-url vs rust-http | `ftp://a89pPVmz6J0@[A:08:e:5:F:fC:AA:fF]:4/..?#` | `[a:8:e:5:f:fc:aa:ff]` | `[A:08:e:5:F:fC:AA:fF]` |
| rust-url vs rust-http | `ws://s93Ah07YX8@[db:ea:B:cA:cD:0:AF:8]:45?#` | `[db:ea:b:ca:cd:0:af:8]` | `[db:ea:B:cA:cD:0:AF:8]` |
| rust-url vs rust-http | `https://U939oH786V7@[C:7B:8E:Cd:8:da:8:39]:/../297g9?#` | `[c:7b:8e:cd:8:da:8:39]` | `[C:7B:8E:Cd:8:da:8:39]` |
| rust-url vs rust-http | `file://d30ay@[Ce:3C:0:5:3:9:4d:AA]/...:023?#` | `[ce:3c:0:5:3:9:4d:aa]` | `[Ce:3C:0:5:3:9:4d:AA]` |
| rust-url vs rust-http | `wss://H3x4U3vVs@[1:56:9:D:3f:b:F6:1]:34/...?#` | `[1:56:9:d:3f:b:f6:1]` | `[1:56:9:D:3f:b:F6:1]` |
| rust-url vs rust-http | `http://189Ez3@[35:10:Fa:5c:eC:3B:72:fe]:202?#` | `[35:10:Fa:5c:eC:3B:72:fe]` | `[35:10:fa:5c:ec:3b:72:fe]` |
| python-stdlib vs python-whatwg | `ftp://1S9L@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `[E6:A0:Bc:F:a:9F:d:a]` | `[E6:A0:Bc:F:a:9F:d:a]:063版...` |
| python-stdlib vs python-whatwg | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?#` | `[8f:D8:2f:4A:C2:67:26:50]:3261ǯ...` | `[8f:D8:2f:4A:C2:67:26:50]` |
| javascript-whatwg vs javascript-uri-js | `ftp://1S9L@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `[e6:a0:bc:f:a:9f:d:a]` | `e6:a0:bc:f:a:9f:d:a` |
| javascript-whatwg vs javascript-parse-uri | `ftp://1S9L@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `[e6:a0:bc:f:a:9f:d:a]` | `[E6` |
| javascript-whatwg vs javascript-fast-url-parser | `ftp://1S9L@[E6:A0:Bc:F:a:9F:d:a]:063?#` | `[e6:a0:bc:f:a:9f:d:a]` | `e6:a0:bc:f:a:9f:d:a` |
| javascript-whatwg vs javascript-fast-url-parser | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?#` | `[8f:d8:2f:4a:c2:67:26:50]` | `8f:d8:2f:4a:c2:67:26:50` |
| javascript-whatwg vs javascript-fast-url-parser | `snmp://7c8@[f:35:91:49:B8:c5:dA:cd]:426?#` | `[f:35:91:49:b8:c5:da:cd]` | `f:35:91:49:b8:c5:da:cd` |
| javascript-whatwg vs javascript-fast-url-parser | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38?#` | `[a6:2:f:b0:2f:0:d:57]` | `a6:2:f:b0:2f:0:d:57` |
| javascript-whatwg vs rust-url | `snews://H9Ex@[3:3:b:3B:8E:d:69:f]:84?#` | `` | `[3:3:b:3b:8e:d:69:f]` |
| javascript-whatwg vs rust-url | `data://7c6R@[70:d:C:f3:84:CA:8:a]:53?#` | `` | `[70:d:c:f3:84:ca:8:a]` |
| javascript-whatwg vs rust-url | `Oplatformnews://yaq8LAjve0Bi3wMPRm55LE@[9f:e:2b:6:e8:cC:86:8]:96?#` | `` | `[9f:e:2b:6:e8:cc:86:8]` |
| javascript-whatwg vs rust-url | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:\96?#` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
