# Fullwidth Character Normalization

**Description:** Fullwidth Unicode characters (e.g. fullwidth period ．U+FF0E) are normalized to ASCII equivalents by some parsers but not others

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-url | `keyparc://l95314s9@2．87．39．99:32206\󞹭[󿿏2I'u9042G2k$K.FI0"c?.󬁍\#nMclF` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| javascript-whatwg vs rust-url | `data://8yF1󺺉⁕2yUI9M4A7X2vNrR39t8@8｡42｡1｡6:202\\!315329gfI?#` | `` | `8%EF%BD%A142%EF%BD%A11%EF%BD%A16` |
| javascript-whatwg vs rust-url | `data://A5S68ⓘ84@3C-B6｡54mj:6887\6P912087KQ$hc4F43?` | `` | `3C-B6%EF%BD%A154mj` |
| javascript-whatwg vs rust-url | `ocfsnewsredis://095978B:@!@爨z<A|5Ị􆪴@3긠𡍎:6200\0ffT/...a692906BfnpQ4!R?q#l𦍩#38󶾯#7亽,&|&⧭W#P` | `` | `3%EA%B8%A0%F0%A1%8D%8E` |
| javascript-whatwg vs rust-url | `data://9W08񡧦臺\不Ea24fry@6．52．61.99:290\1v164a1a7\eg1?#` | `6%EF%BC%8E52%EF%BC%8E61.99` | `` |
| javascript-whatwg vs rust-url | `iax://741r028．5．6.49:672\)􁳕:;
7P{s7~3N63.)1Tw95MP?#L` | `741r028%EF%BC%8E5%EF%BC%8E6.49` | `` |
| javascript-whatwg vs rust-url | `edcoapcidms-settings-notificationsdropms-powerpoint://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7\A44e14;2vr813M899'?#/[6$0` | `5%EF%BD%A193%EF%BD%A195.48` | `` |
| whatwg vs legacy | `bolo://0𫚳1e65.4.17.3:77058479/...` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| whatwg vs deno | `keyparc://l95314s9@2．87．39．99:32206...` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| whatwg vs deno | `iax://741r028．5．6.49:672...` | `` | `741r028%EF%BC%8E5%EF%BC%8E6.49` |
| whatwg vs smithy | `wss://5gPK6D2y81REN446o12픐@2｡29｡9.3_...` | `` | `2%EF%BD%A129%EF%BD%A19.3_...` |
| whatwg vs smithy | `edcoap...://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7...` | `` | `5%EF%BD%A193%EF%BD%A195.48` |
| whatwg vs smithy | `data://...@3C-B6｡54mj:6887...` | `` | `3C-B6%EF%BD%A154mj` |
| whatwg vs deno | `keyparc://l95314s9@2．87．39．99:32206\[2I'u9042G2k$K.FI0"c?.` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| whatwg vs deno | `iax://741r028．5．6.49:672\)𗕕:;
7P{s7~3N63.)1Tw95MP?#L` | `` | `741r028%EF%BC%8E5%EF%BC%8E6.49` |
| whatwg vs deno | `edcoapcidms-settings-notificationsdropms-powerpoint://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7\A44e14;2vr813M899'?#/[6$0` | `` | `5%EF%BD%A193%EF%BD%A195.48` |
| whatwg vs deno | `data://9W08𛥦臺\\\u4e0dEa24fry@6．52．61.99:290\1v164a1a7\eg1?#` | `` | `6%EF%BC%8E52%EF%BC%8E61.99` |
| whatwg vs javascript-parse-uri | `ftp://T1b8k1D0⇀�� b ^{󠃳󣔮mz1W16@84｡04.61.80:5449𐡕Xඪ󧄔%[/𒄐맲牓q64x7Vw5Y06dU75C.11?#~5#` | `` | `84｡04.61.80` |
| whatwg vs javascript-parse-uri | `wss://5gPK6D2y81REN446o12피@2｡29｡9.3_��G@⒔	^��}��
'��󮀀37234󓣎u)
󨊷j┏59qXRshi24i1DG6_61h?#` | `` | `2｡29｡9.3_��G@⒔	^��}��
'��󮀀37234󓣎u)
󨊷j┏59qXRshi24i1DG6_61h` |
| whatwg vs javascript-url-parse | `wss://5gPK6D2y81REN446o12피@2｡29｡9.3_��G@⒔	^��}��
'��37234u)
jሏ59qXRshi24i1DG6_61h?#` | `` | `⒔^��}��'��37234u)
jሏ59qxrshi24i1dg6_61h` |
| whatwg vs javascript-url-parse | `ftp://T1b8k1D0⇀���� b ^{󠃳󥀮��mz1W16@84｡04.61.80:5449𐱕Xݨ󧃔%[/𒄐닲牓q64x7Vw5Y06dU75C.11?#~5#` | `` | `84｡04.61.80:5449𐱕xݨ󧃔%[` |
| whatwg vs javascript-url-parse | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `` | `5．90．55.47:177257836qh1okh` |
| whatwg vs javascript-fast-url-parser | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `` | `5.90.55.47` |
| whatwg vs javascript-fast-url-parser | `ftp://T1b8k1D0⇀���� b ^{󠃳󥀮��mz1W16@84｡04.61.80:5449𐱕Xݨ󧃔%[/𒄐닲牓q64x7Vw5Y06dU75C.11?#~5#` | `` | `84.04.61.80` |
| whatwg vs javascript-fast-url-parser | `://bta73Fi6nawqa8NrV5k:A47L6zVg@2w7P-2079q91m5G。 7d3:64 H009198HYpF25-82f16?#4J5*N<` | `` | `2w7p-2079q91m5g.7d3` |
| javascript-whatwg vs javascript-deno | `keyparc://l95314s9@2．87．39．99:32206\?` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| javascript-whatwg vs javascript-deno | `iax://741r028．5．6.49:672\?` | `` | `741r028%EF%BC%8E5%EF%BC%8E6.49` |
| javascript-whatwg vs javascript-deno | `data://9W08@6．52．61.99:290\?` | `` | `6%EF%BC%8E52%EF%BC%8E61.99` |
| javascript-whatwg vs javascript-deno | `http://3H35MD6E3O59@7。 67.88.221?` | `7.67.88.xn--2214-2ec87815j` | `` |
| javascript-whatwg vs javascript-deno | `data://A5S68@3C-B6｡ 54mj:6887\?` | `` | `3C-B6%EF%BD%A154mj` |
| javascript-whatwg vs javascript-deno | `edcoapcidms://i26j2DO270D@5｡93｡95.48:7\?` | `` | `5%EF%BD%A193%EF%BD%A195.48` |
| whatwg vs deno | `keyparc://l95314s9@2．87．39．99:32206\?` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| whatwg vs deno | `iax://741r028．5．6.49:672\)` | `` | `741r028%EF%BC%8E5%EF%BC%8E6.49` |
| whatwg vs smithy | `ms-virtualtouchpad://g𨜇ow?@[b6:0:ab:91:5:06:aC:3F]:853B35Uc8l96?#` | `` | `g%F0%A8%9C%87ow` |
| whatwg vs deno | `data://3C-B6｡54mj:6887\6P912087KQ$hc4F43?` | `` | `3C-B6%EF%BD%A154mj` |
| whatwg vs deno | `edcoapcidms-settings-notificationsdropms-powerpoint://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7\A44e14;2vr813M899'?#/[6$0` | `` | `5%EF%BD%A193%EF%BD%A195.48` |
| whatwg vs fast-uri | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `` | `5．90．55.47` |
| whatwg vs parseuri | `ftp://T1b8k1D0@84｡04.61.80:5449?#~5#` | `` | `84｡04.61.80` |
| whatwg vs fast-uri | `ftp://T1b8k1D0@84｡04.61.80:5449?#~5#` | `` | `84｡04.61.80` |
| whatwg vs parseuri | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `5．90．55.47` | `` |
| whatwg vs jsuri | `market://E0U𑽘_𗩮♤#󴣴 01筂m,I󱻂72q@71．80．86.07:3_E37b9bIf_5eKYSp6]2=?#` | `` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` |
| whatwg vs jsuri | `data://4444r@9rM｡40xvr?#` | `` | `9rM%EF%BD%A1H3F574l69.1mg-y3퀊�#ㇵ` |
| whatwg vs go-net | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `` | `5．90．55.47` |
| whatwg vs go-net | `ftp://T1b8k1D0@84｡04.61.80:5449?#~5#` | `` | `84｡04.61.80` |
| whatwg vs rust-url | `keyparc://l95314s9@2．87．39．99:32206\...#nMclF` | `` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99` |
| whatwg vs rust-url | `edcoapcidms-settings-notificationsdropms-powerpoint://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7\...` | `5%EF%BD%A193%EF%BD%A195.48` | `` |
| whatwg vs rust-url | `data://9W08@6．52．61.99:290\...?#` | `6%EF%BC%8E52%EF%BC%8E61.99` | `` |
| whatwg vs rust-url | `data://8yF1@8｡42｡1｡6:202\...?#` | `` | `8%EF%BD%A142%EF%BD%A11%EF%BD%A16` |
| python-urllib-parse vs python-furl | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `5.90.55.47` | `` |
| python-urllib-parse vs python-furl | `ftp://T1b8k1D0@84｡04.61.80:5449...?#~5#` | `84.4.61.80` | `` |
