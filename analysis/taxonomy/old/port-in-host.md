# Port Number in Host Field

**Description:** The port number is included in the host field by one parser instead of being separated into a dedicated port field.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs url-parse | `callto://P+...@70.87.66.78:522 m?#4` | `` | `70.87.66.78:522 m` |
| whatwg vs url-parse | `https://T15ZsDCQx8340D71B49...@77.77.7.9:6...` | `` | `77.77.7.9:6鉁⩡鉇ᰏa硪76gcxfrgn6}4iyi[d76` |
| whatwg vs url-parse | `vemmi://kM37d8329qO9hd...@69vS9427mjPMWj0)1:808tFL4MkQ?#` | `` | `69vs9427mjpmwj0)1:808tfl4mkq` |
| whatwg vs url-parse | `https://11139j078uW1j8.-4A:83563Pt84b64938v1xuQ44x7?#` | `` | `11139j078uw1j8.-4a:83563pt84b64938v1xuq44x7` |
| whatwg vs url-parse | `data://z308V2H89C6IVs670N2...@52.34.61.48:...` | `` | `52.34.61.48:⸉6⦻���8t949548yrbpju9d,6a` |
| whatwg vs url-parse | `wss://2dCf58OlY:@...@...:101L"9O...` | `` | `ᇰx8ᵡyﱠ2:101l"9o묷�7�f𧛘` |
| whatwg vs url-parse | `http://01𢉞07@[76:d:7e:8:6E:3c:5:a]:494...` | `` | `[76:d:7e:8:6e:3c:5:a]:494󯻣0!dl5⓺3c1` |
| whatwg vs url-parse | `wss://5WS81r673vEMCn...@5bP97a1K:9814A...` | `` | `5bp97a1k:9814a⇡px*С󠃅8⨪%,⏐␒𣜰�2𢈃` |
| whatwg vs url-parse | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63...` | `71-h59w-o` | `` |
| whatwg vs url-parse | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs url-parse | `z39.50s://437"@--C80YG:4427H54?#` | `` | `--c80yg:4427h54` |
| whatwg vs url-parse | `afs://7%4FdpND`3%4Cs@L:5F}GVG%35%713%35%60Nv65O%74%2AF4?%23` | `` | `l:5f}gvg%35%713%35%60nv65o%74%2af4` |
| whatwg vs legacy | `ftp://Kds2CYszhi8H67d𬃚 Qtjf@08.61.1.95:76?#` | `` | `08.61.1.95:76` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3𘖰$#I2` | `99.01.1.20:88` | `` |
| whatwg vs legacy | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63/Jchz3zh8jlOCB682cyu?#` | `71-h59w-o` | `71-h59w-o:63` |
| whatwg vs legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs legacy | `wss://0QJ:68@35006-kA:8175"W1FF503J0ba5pZP8k4=?#$;6` | `` | `35006-ka:8175` |
| whatwg vs legacy | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751}Ḥ𐋕✉	󧷆󣳉󡳐󢳆⠠	{G?#i2` | `` | `k9-2kr23.u.c.1s272-:751` |
| whatwg vs legacy | `file://6LF707:3a1@j:28> 𨃚
��8RhV8H[k8q983SUR-3?#` | `` | `j:28` |
| whatwg vs legacy | `bolo://0𣪳1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| whatwg vs deno | `mms://7l90:\M5.i91-E3-4328c.-3g:𐳰
#÷愛𐳬` | `7l90` | `` |
| whatwg vs deno | `itms://K4537u7Si:17zDx56o@ED042W.4d75mMABc:5\XF=𥉰U:L蚣墀>;򢣸◀𢗈5B18Z5f82(I86m1lhu2?#I` | `ED042W.4d75mMABc` | `` |
| whatwg vs deno | `dns://0mYmZcW5G830d0v248p8@60.9.9.5:913\~9N6OYy6C6U69f17qh?#` | `` | `60.9.9.5` |
| whatwg vs deno | `data://9W08𛥦臺\不Ea24fry@6．52．61.99:290\1v164a1a7\eg1?#` | `` | `6%EF%BC%8E52%EF%BC%8E61.99` |
| whatwg vs javascript-url-parse | `callto://P+��bo��0
@70.87.66.78:522 	m?#4` | `` | `70.87.66.78:522 m` |
| whatwg vs javascript-url-parse | `resource://r5f2J41k4󥗥✙
<1@2v9-bC6.1.52uZ6C-lo:05:w↸?#` | `2v9-bc6.1.52uz6c-lo` | `2v9-bc6.1.52uz6c-lo:05:w↸` |
| whatwg vs javascript-url-parse | `file://mRd810U5154Pf7d8Ro3:9@95.0.12.65:9󨃍=4Y09e672l!340]2C5S7?#` | `95.0.12.65:9󨃍=4y09e672l!340]2c5s7` | `` |
| whatwg vs javascript-url-parse | `vemmi://kM37d8329qO9hd󨂧��tsJd5iT2Xfyx427V@69vS9427mjPMWj0)1:808tFL4MkQ?#` | `` | `69vs9427mjpmwj0)1:808tfl4mkq` |
| whatwg vs javascript-url-parse | `data://z308V2H89C6IVs670N2󰧀𤴇>³󢳲𦓾 1E@52.34.61.48:⌉	6⦻󧃼󯴛8t949548yRBpjU9D,6a?#` | `` | `52.34.61.48:⌉	6⦻󧃼󯴛8t949548yrbpju9d,6a` |
| whatwg vs javascript-url-parse | `z39.50s://437"@--C80YG:4427H54?#` | `` | `--c80yg:4427h54` |
| javascript-whatwg vs javascript-legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14...?` | `5ghx.3n2u6p4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| javascript-whatwg vs javascript-legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7` | `.8agd-.64.z64.091.e` | `.8agd-.64.z64.091.e:1478` |
| javascript-whatwg vs javascript-legacy | `ircsw://5OW:3Ua7KU76091@71-h59w-o:63/J?#` | `71-h59w-o` | `71-h59w-o:63` |
| javascript-whatwg vs javascript-legacy | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751}J?#` | `` | `k9-2kr23.u.c.1s272-:751` |
| javascript-whatwg vs javascript-legacy | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95:76` |
| javascript-whatwg vs javascript-deno | `im://603M98,!so5u3@648.iRL7jv-41d93q5u:85\?` | `` | `648.iRL7jv-41d93q5u` |
| javascript-whatwg vs javascript-deno | `ms-visio://9Zj5r9D@1---d:3\VrCMlD?` | `` | `1---d` |
| javascript-whatwg vs javascript-deno | `fle://f5Fx3Z8L1@-S9gK:798\?` | `` | `-S9gK` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCBE@5gHx.3n2u6P4401.-7l:048/;14[gՆ987⢕M?1?&1?` | `5gHx.3n2u6P4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| whatwg vs legacy | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63/Jchz3zh8jlOCB682cyu?#` | `71-h59w-o` | `71-h59w-o:63` |
| whatwg vs legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs legacy | `bolo://0𫚳1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| whatwg vs legacy | `http://77oPR6l2e3146R7wX1u:nw75@-g.2pEcNOEPp42q0Tf.:9120 |` | `` | `-g.2pecnoepp42q0tf.:9120` |
| whatwg vs legacy | `wss://0QJ:68@35006-kA:8175"W1FF503J0ba5pZP8k4=?#$;6` | `` | `35006-ka:8175` |
| whatwg vs url-parse | `resource://r5f2J41k4@2v9-bC6.1.52uZ6C-lo:05:w?#` | `2v9-bc6.1.52uz6c-lo:05:w↸` | `` |
| whatwg vs url-parse | `https://11139j078uW1j8.-4A:83563Pt84b64938v1xuQ44x7?#` | `` | `11139j078uw1j8.-4a:83563pt84b64938v1xuq44x7` |
| whatwg vs url-parse | `wss://5WS81r673vEMCn@5bP97a1K:9814A?#` | `` | `5bp97a1k:9814a⇡px*ԡ󣏅8⨪%,⿐␒󐅰󑃂4𠀃` |
| whatwg vs urijs | `resource://r5f2J41k4@2v9-bC6.1.52uZ6C-lo:05:w?#` | `` | `2v9-bC6.1.52uZ6C-lo:05:w↸` |
| whatwg vs url-parse | `vemmi://kM37d8329qO9hd@69vS9427mjPMWj0)1:808tFL4MkQ?#` | `` | `69vs9427mjpmwj0)1:808tfl4mkq` |
| whatwg vs parseuri | `https://11139j078uW1j8.-4A:83563Pt84b64938v1xuQ44x7?#` | `` | `11139j078uW1j8.-4A` |
