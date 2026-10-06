# Port Leaked into Host

**Description:** One parser includes the port number in the host field (e.g. host:port) while the other correctly separates them.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9?#` | `5gHx.3n2u6P4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| whatwg vs legacy | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#` | `1` | `1:5` |
| whatwg vs legacy | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63/Jchz3zh8jlOCB682cyu?#` | `71-h59w-o` | `71-h59w-o:63` |
| whatwg vs legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs legacy | `wss://cmP3J9s7@f..7S1j-2..dO6-B-In:8#QUT~(287s4707D50]12?#` | `f..7s1j-2..do6-b-in` | `f..7s1j-2..do6-b-in:8` |
| whatwg vs legacy | `ut2004://4881CYNhgxL9ta019G7@4o:246/..lu0u9'756.13t15Sh?#` | `4o` | `4o:246` |
| whatwg vs legacy | `http://Zn8857EzY2D021w9627@u:3983?#` | `u` | `u:3983` |
| whatwg vs legacy | `ws://Un02qddshipwv1i5m7f1189Nz395zqkBh3A866V@p:6411?#` | `p` | `p:6411` |
| whatwg vs legacy | `ws://32a60IQ3dJ6i24j35KI5S}r@F68-W:38/...0J#` | `f68-w:38` | `f68-w` |
| whatwg vs legacy | `dntp://F70_9@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `[d:c:a1:ce:b:33:d:f]` | `[d:c:a1:ce:b:33:d:f]:42256` |
| legacy vs url-parse | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `08.61.1.95:76` |
| legacy vs url-parse | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#` | `.8agd-.64.z64.091.e` | `.8agd-.64.z64.091.e:1478` |
| legacy vs url-parse | `wss://cmP3J9s7@f..7S1j-2..dO6-B-In:8#` | `f..7s1j-2..do6-b-in` | `f..7s1j-2..do6-b-in:8` |
| legacy vs url-parse | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#` | `1` | `1:5` |
| legacy vs url-parse | `dntp://F70_9@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `[d:c:a1:ce:b:33:d:f]` | `[d:c:a1:ce:b:33:d:f]:42256` |
| javascript-whatwg vs javascript-legacy | `sLopenpgp4fpraFQ7://...@5gHx.3n2u6P4401.-7l:048/` | `5gHx.3n2u6P4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| javascript-whatwg vs javascript-legacy | `pttp://...@1:5/` | `1` | `1:5` |
| javascript-whatwg vs javascript-legacy | `ircsw://...@71-h59w-o:63/` | `71-h59w-o` | `71-h59w-o:63` |
| javascript-whatwg vs javascript-legacy | `ms-settings-cellular://...@.8agD-.64.z64.091.E:1478` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| javascript-whatwg vs javascript-legacy | `wss://...@f..7S1j-2..dO6-B-In:8` | `f..7s1j-2..do6-b-in` | `f..7s1j-2..do6-b-in:8` |
| javascript-whatwg vs javascript-legacy | `pttp://...@1:5/` | `1` | `1:5` |
| javascript-whatwg vs javascript-legacy | `ut2004://...@4o:246/` | `4o` | `4o:246` |
| javascript-whatwg vs javascript-legacy | `wss://...@p:6411?` | `p` | `p:6411` |
| javascript-whatwg vs javascript-legacy | `http://...@u:3983?` | `u` | `u:3983` |
| javascript-whatwg vs javascript-legacy | `dntp://...@[D:C:a1:cE:b:33:D:f]:42256/` | `[d:c:a1:ce:b:33:d:f]` | `[d:c:a1:ce:b:33:d:f]:42256` |
| javascript-whatwg vs javascript-legacy | `ws://...@F68-W:38/` | `f68-w:38` | `f68-w` |
| javascript-legacy vs javascript-parse-uri | `bolo://0𬫓1e65.4.17.3:77058479/...` | `xn--01e65-qp48f.4.17.3:77058479` | `0𬫓1e65.4.17.3` |
| javascript-legacy vs javascript-parse-uri | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751}...` | `k9-2kr23.u.c.1s272-:751` | `K9-2kr23.u.C.1s272-` |
| javascript-legacy vs javascript-parse-uri | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#` | `1` | `1:5` |
| javascript-legacy vs javascript-uri-js | `https://99.01.1.20:88/...` | `99.01.1.20:88` | `99.1.1.20` |
| javascript-legacy vs javascript-uri-js | `data://p:6411/...` | `p:6411` | `p` |
| javascript-legacy vs go-net | `https://[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` | `d4:Ab:B5:A:dD:Ba:2d:3C` |
| javascript-legacy vs go-net | `https://f..7s1j-2..dO6-B-In:8/...` | `f..7s1j-2..do6-b-in:8` | `f..7S1j-2..dO6-B-In` |
| js-legacy vs csharp-systemuri | `stun://Pj05xp616px32e1F715ᆥC8Y@Bj0982C5a.:48/..4kQQT0J7P5/?#` | `bj0982c5a.` | `bj0982c5a.:48` |
| js-legacy vs csharp-systemuri | `ws://qr0S81N0W9b3frlJo3
6108cPJ4QP869@f49HI-PC20-6uAIj｡jf:173?#` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf:173` |
| js-legacy vs python-hyperlink | `ftp://Kds2CYszhi8H67d金🦚Qtjf@08.61.1.95:76?#` | `08.61.1.95` | `08.61.1.95:76` |
| js-legacy vs python-hyperlink | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[g...?` | `5gHx.3n2u6P4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| js-legacy vs python-hyperlink | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63/Jchz3zh8jlOCB682cyu?#` | `71-h59w-o` | `71-h59w-o:63` |
| javascript-legacy vs rust-url | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/...` | `5ghx.3n2u6p4401.-7l:048` | `5gHx.3n2u6P4401.-7l` |
| javascript-legacy vs rust-url | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63/...` | `71-h59w-o:63` | `71-h59w-o` |
| javascript-legacy vs rust-url | `dntp://F70_9...@[D:C:a1:cE:b:33:D:f]:42256/...` | `[d:c:a1:ce:b:33:d:f]:42256` | `[d:c:a1:ce:b:33:d:f]` |
| javascript-legacy vs go-net | `(URL with host 71-h59w-o and port 63)` | `71-h59w-o` | `71-h59w-o:63` |
| javascript-legacy vs go-net | `ftp://64ny5g4h6u5ev4z6rGaBG6@[d4:Ab:B5:A:dD:Ba:2d:3C]:4517/...` | `[d4:ab:b5:a:dd:ba:2d:3c]:4517` | `d4:Ab:B5:A:dD:Ba:2d:3C` |

| js-whatwg vs rust-url | `dntp://F70_9...@[D:C:a1:cE:b:33:D:f]:42256/...` | `[d:c:a1:ce:b:33:d:f]:42256` | `[d:c:a1:ce:b:33:d:f]` |
| js-whatwg vs rust-url | `http://f..7S1j-2..do6-b-in:8/...` | `f..7s1j-2..do6-b-in:8` | `f..7s1j-2..do6-b-in` |
| js-whatwg vs rust-url | `...@1:5...` | `1` | `1:5` |
| js-whatwg vs rust-url | `...@p:6411...` | `p` | `p:6411` |
| perl-uri vs java-galimatias | `...(IPv6 URL with port)...` | `[a6:2:f:B0:2f:0:D:57]:380whxmjk3528_888Y1e9x` | `a6:2:f:b0:2f::d:57` |
| perl-uri vs java-galimatias | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:380whxmjk3528_888Y1e9x?#q5` | `[a6:2:f:B0:2f:0:D:57]:380whxmjk3528_888Y1e9x` | `a6:2:f:b0:2f::d:57` |
| js-whatwg vs go-net | `...(URL with port)...` | `0𫚳1e65.4.17.3` | `xn--01e65-qp48f.4.17.3:77058479` |
