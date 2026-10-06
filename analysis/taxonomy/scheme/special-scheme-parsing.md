# Special scheme parsing differences

**Description:** One parser recognizes and preserves special schemes (e.g., wss, ldaps) while the other treats them as non-special or substitutes alternative schemes

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `wss://5j99330G>􎘦7kH":<𦻨⚖↜Ⴐ45_lE ?𥄡2l?3{5Z2p&𥄡2l?3{5Z2p` | `wss:` | `ws:` |
| whatwg vs legacy | `wss://5j99330G>􎘦7kH":<𦻨⚖↜Ⴐ45_lE ?𥄡2l?3{5Z2p&𥄡2l?3{5Z2p` | `wss:` | `file:` |
| whatwg vs legacy | `wss://5j99330G>􎘦7kH":<𦻨⚖↜Ⴐ45_lE ?𥄡2l?3{5Z2p&𥄡2l?3{5Z2p` | `wss:` | `ftp:` |
| whatwg vs legacy | `ldaps:À¯/Sv3À·1gQ:⚼@d1a9l9286fÀ±p.qtÁ´À².-:7󡛂94aÀ»'À£㧣8GZH7kÀ²lÁ³H9Rk4KLÀ³-Á­?#` | `ldaps:` | `ws:` |
| whatwg vs legacy | `ldaps:À¯/Sv3À·1gQ:⚼@d1a9l9286fÀ±p.qtÁ´À².-:7󡛂94aÀ»'À£㧣8GZH7kÀ²lÁ³H9Rk4KLÀ³-Á­?#` | `ldaps:` | `file:` |
| whatwg vs deno | `mms://7l90:\M5.i91-E3-4328c.-3g:􃑰#÷혭󾲤` | `mms:` | `ndict:` |
| whatwg vs deno | `mms://7l90:\M5.i91-E3-4328c.-3g:􃑰#÷혭󾲤` | `mms:` | `callto:` |
| whatwg vs deno | `ws://c6F9�ퟷ/...}󾣌総#0.;i98ººn1FL6Po:226⌼GJq344(tj.2E603ED`1?O|0􈿌.U` | `ws:` | `ndict:` |
| whatwg vs deno | `ws://c6F9�ퟷ/...}󾣌総#0.;i98ººn1FL6Po:226⌼GJq344(tj.2E603ED`1?O|0􈿌.U` | `ws:` | `callto:` |
| whatwg vs smithy | `ws://05?838f9kl043c43Lh@[7C:f:1e:8E:a0:ba:FF:d]h605𪶔%'339/26831V4R8p8a7[V5kA1C%8􃀼5bj`&838f9kl043c43Lh@[7C:f:1e:8E:a0:ba:` | `ws:` | `a:` |
| whatwg vs smithy | `ftp://N3i7:J7j688.48.50.5:7114604327169�@8?	ℸ�┮%67��桐�⪿�	
	�&	ℸ�┮%67��桐�⪿�	
	�#s|H` | `ftp:` | `a:` |
| whatwg vs legacy | `wss://5j99330G>󆥦` | `wss:` | `ws:` |
| whatwg vs legacy | `wss://5j99330G>󆥦` | `wss:` | `file:` |
| whatwg vs legacy | `wss://5j99330G>󆥦` | `wss:` | `ftp:` |
| whatwg vs legacy | `ldaps:¯/Sv3·1gQ:⚼@d1a9l9286f±p.qt´².-:7𪦂` | `ldaps:` | `ws:` |
| whatwg vs legacy | `ldaps:¯/Sv3·1gQ:⚼@d1a9l9286f±p.qt´².-:7𪦂` | `ldaps:` | `file:` |
| uripara vs php-http | `wss://5j99330G>𲀦 7kH":<񹭸≪↜Ꮠ 45_lE ?񹂡 2l?
3{5Z2p&񹂡 2l?
3{5Z2p` | `wss:` | `file:` |
| uripara vs ada | `ws://0��ᴱÀ¢V5Á°@zÁ­:59=6񻆱⩌🺉@񩣫 Á°O򁒚'⭁����♣#6hs񆳽	À´?#` | `ws:` | `file:` |
| php-http vs ada | `wss://p875ᴙP|
� 7o4@479.za.88-64-bt.xn--673,x7f-c325c?#` | `wss:` | `http:` |
| uripara vs node | `%68ttps://01%71&%5AX%44@6� 9$484R?#43w5%7A` | `%68ttps:` | `]%47te%6CnetXm%6Fdem:` |
| whatwg vs jsprim | `sLopenpgp4fpraFQ7://2W21SCB` | `sLopenpgp4fpraFQ7:` | `slopenpgp4fprafq7:` |
| whatwg vs jsprim | `ventriloI://3Y63NWUY67C3` | `ventriloI:` | `ventriloi:` |
| whatwg vs jsprim | `7Ys74i9Rau41R:56` | `7Ys74i9Rau41R:` | `7ys74i9rau41r:` |
| whatwg vs jsprim | `redissNpalmfm://0` | `redissNpalmfm:` | `redissnpalmfm:` |
| whatwg vs jsprim | `BBiris://X9HW` | `bbiris:` | `BBiris:` |
| whatwg vs legacy | `wss://yNk4103A` | `wss` | `wss:` |
| whatwg vs legacy | `https://JxUS` | `https` | `https:` |
| whatwg vs legacy | `soldatpwid://` | `soldatpwid` | `soldatpwid:` |
| whatwg vs legacy | `ws://hrl49V3Q50` | `ws` | `ws:` |
| whatwg vs legacy | `lastfm://vQ931tsj0` | `lastfm:` | `lastfm` |
