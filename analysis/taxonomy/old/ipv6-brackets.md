# IPv6 Bracket Handling

**Description:** IPv6 addresses are returned with surrounding brackets by one parser but without brackets (or with partial brackets) by another.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs fast-url-parser | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261...` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| whatwg vs fast-url-parser | `http://01...@[76:d:7e:8:6E:3c:5:a]:494...` | `` | `76:d:7e:8:6e:3c:5:a` |
| whatwg vs fast-url-parser | `ftp://1S9L=...@[E6:A0:Bc:F:a:9F:d:a]:063...` | `` | `e6:a0:bc:f:a:9f:d:a` |
| whatwg vs fast-url-parser | `snmp://7c8...@[f:35:91:49:B8:c5:dA:cd]:426...` | `` | `f:35:91:49:b8:c5:da:cd` |
| whatwg vs fast-url-parser | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38...` | `` | `a6:2:f:b0:2f:0:d:57` |
| whatwg vs fast-url-parser | `ftp://jz5nMvQG7TNE...@[8b:4B:8:9:a:cF:e9:8]:...` | `` | `8b:4b:8:9:a:cf:e9:8` |
| whatwg vs fast-uri | `ftp://1S9L=...@[E6:A0:Bc:F:a:9F:d:a]:063...` | `` | `e6:a0:bc:f:a:9f:d:a` |
| whatwg vs urijs | `snews://H9Ex...@[3:3:b:3B:8E:d:69:f]:84...` | `` | `[3:3:b:3b:8e:d:69:f]` |
| whatwg vs urijs | `data://7┲읝...@[5:30:6:4:2:c6:f2:77]:...` | `` | `[5:30:6:4:2:c6:f2:77]` |
| whatwg vs urijs | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:...` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
| whatwg vs deno | `snews://H9Ex󥓙V笹
%4𐸘𙵧hY5LcF@[3:3:b:3B:8E:d:69:f]:84\b1G9258{53$De1Mp28?#` | `` | `[3:3:b:3b:8e:d:69:f]` |
| whatwg vs deno | `data://7c6R	9󧫩𐽭L2@[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `[70:d:c:f3:84:ca:8:a]` | `` |
| whatwg vs deno | `ws://Ddz441H0h5q5C&
0ZႾ#k@[9:Cc:C:B:Bb:b0:C:f9]궗685M𐹅⧚⋀b4X󣓂v?#XNaA86'u2e60` | `xn--ddz441h0h5q5c&0z-ks2n` | `` |
| whatwg vs deno | `Oplatformnews://yaq8LAjve0Bi3wMPRm55LE@[9f:e:2b:6:e8:cC:86:8]:96\?#jM~2=^z[` | `` | `[9f:e:2b:6:e8:cc:86:8]` |
| whatwg vs deno | `Tms-media-stream-idX://WKAr:@[e:fa:b:0:4:6:f0:d]:2992\0ab7e3FM145?#U6#853@93&` | `` | `[e:fa:b:0:4:6:f0:d]` |
| whatwg vs deno | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:\96{𐀪'6/62쫭󠺁❪3v13Y󤐕?#*+kJ` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
| whatwg vs deno | `data://J65
=23AUT@[a7:9E:3:D:4F:9e:bC:53]:182\DW$=hQDMGG5661^59?#` | `` | `[a7:9e:3:d:4f:9e:bc:53]` |
| whatwg vs deno | `ms-useractivityset://nED44vvK@[eb:D5:3:c:e:F2:4:0d]:00\63oX549XdB4J697Sw2?` | `` | `[eb:d5:3:c:e:f2:4:d]` |
| whatwg vs deno | `https://32P8B@[1d:2:Ce:8F:4:5a:E:2]:1753` | `` | `[1d:2:ce:8f:4:5a:e:2]` |
| whatwg vs deno | `data://A5S68ⓘ84@3C-B6｡mj:6887\6P912087KQ$hc4F43?` | `` | `3C-B6%EF%BD%A154mj` |
| whatwg vs javascript-uri-js | `ftp://1S9L=󥇖��G镍518k@[E6:A0:Bc:F:a:9F:d:a]:063𢘌60Juu06ylV8j2EW4913?#` | `` | `e6:a0:bc:f:a:9f:d:a` |
| whatwg vs javascript-uri-js | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261Ư␃ 78O?4?#` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| javascript-whatwg vs javascript-deno | `data://7c6R	9@[70:d:C:f3:84:CA:8:a]:53\405?` | `[70:d:c:f3:84:ca:8:a]` | `` |
| javascript-whatwg vs javascript-deno | `data://7┲𪄝s5D@⟟SḪ@97v69↭Qin@[5:30:6:4:2:c6:f2:77]:\?` | `` | `[5:30:6:4:2:c6:f2:77]` |
| javascript-whatwg vs javascript-deno | `Oplatformnews://yaq8LAjve0Bi@[9f:e:2b:6:e8:cC:86:8]:96\?` | `` | `[9f:e:2b:6:e8:cc:86:8]` |
| javascript-whatwg vs javascript-deno | `Tms-media-stream-idX://WKAr:@[e:fa:b:0:4:6:f0:d]:2992\?` | `` | `[e:fa:b:0:4:6:f0:d]` |
| javascript-whatwg vs javascript-deno | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:\?` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
| javascript-whatwg vs javascript-deno | `file://T7srLRM12dnM3jP9u66a@[F1:9c:cD:f4:75:43:67:4AJpc]:\?` | `` | `[f1:9c:cd:f4:75:43:67:4ajpc]` |
| javascript-whatwg vs javascript-uri-js | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063?` | `` | `e6:a0:bc:f:a:9f:d:a` |
| javascript-whatwg vs javascript-uri-js | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| whatwg vs deno | `snews://H9Ex...@[3:3:b:3B:8E:d:69:f]:84\b1G9258{53$De1Mp28?#` | `` | `[3:3:b:3b:8e:d:69:f]` |
| whatwg vs deno | `data://7┲읝⩼s5D@⟟SḪ@97v69↭黝@[5:30:6:4:2:c6:f2:77]:\` | `` | `[5:30:6:4:2:c6:f2:77]` |
| whatwg vs deno | `Oplatformnews://yaq8LAjve0Bi3wMPRm55LE@[9f:e:2b:6:e8:cC:86:8]:96\` | `` | `[9f:e:2b:6:e8:cc:86:8]` |
| whatwg vs deno | `Tms-media-stream-idX://WKAr:@[e:fa:b:0:4:6:f0:d]:2992\` | `` | `[e:fa:b:0:4:6:f0:d]` |
| whatwg vs deno | `doi://3I7kKI72a3v41Eu04B0:Z@[0d:d7:bE:7d:68:0:CE:f7]:\` | `` | `[d:d7:be:7d:68:0:ce:f7]` |
| whatwg vs deno | `data://[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `[70:d:c:f3:84:ca:8:a]` | `` |
| whatwg vs url-parse | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063...` | `` | `[e6:a0:bc:f:a:9f:d:a]:063񐌌60juu06ylv8j2ew4913` |
| whatwg vs fast-url-parser | `ftp://1S9L=@[E6:A0:Bc:F:a:9F:d:a]:063...` | `` | `e6:a0:bc:f:a:9f:d:a` |
| whatwg vs fast-url-parser | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?#` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| whatwg vs fast-url-parser | `snmp://7c8@[f:35:91:49:B8:c5:dA:cd]:426?#` | `` | `f:35:91:49:b8:c5:da:cd` |
| whatwg vs fast-url-parser | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38 0whxmjk3528_888Y1e9x?#q5` | `` | `a6:2:f:b0:2f:0:d:57` |
| whatwg vs jsuri | `file://T7srLRM12dnM3jP9u66a@[F1:9c:cD:f4:75:43:67:4AJpc]:...?#` | `` | `f1:9c:cd:f4:75:43:67:4ajpc` |
| whatwg vs jsuri | `http://01@[76:d:7e:8:6E:3c:5:a]:494...?#B5g+6E;M` | `` | `[76:d:7e:8:6E:3c:5:a]` |
| whatwg vs jsuri | `snmp://7c8@[f:35:91:49:B8:c5:dA:cd]:426?#` | `` | `[f:35:91:49:b8:c5:da:cd]` |
| whatwg vs ada-uri-mime | `magnet://t1A5335=@[C:C:EB:FE:7:2:8:0]17{|/./ 72&O7T8D8jhH(6R22451?#` | `[C:C:EB:FE:7:2:8:0]17{|` | `` |
| whatwg vs trurl | `http://91Z62F8Ej31ma96VbM7:8R@[FF:33:5E:2C:F:0A:89:1]y?` | `` | `[FF:33:5E:2C:F:0A:89:1]
y𐓅\06}...` |
| whatwg vs aria2 | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:3261?4?#` | `` | `8f:d8:2f:4a:c2:67:26:50` |
| whatwg vs aria2 | `snmp://7c8@[f:35:91:49:B8:c5:dA:cd]:426?#` | `` | `[f:35:91:49:b8:c5:da:cd]` |
| whatwg vs aria2 | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38 0whxmjk3528?#q5` | `` | `[a6:2:f:b0:2f:0:d:57]` |
| whatwg vs crystal-uri | `magnet://t1A5335=@[C:C:EB:FE:7:2:8:0]17{|/./ 72&O7T8D8jhH(6R22451?#` | `[C:C:EB:FE:7:2:8:0]17{|` | `[C:C:EB:FE:7:2:8:0]17{|` |
