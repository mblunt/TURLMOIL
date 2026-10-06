# Case Folding

**Description:** One parser lowercases the host (WHATWG-style normalization) while the other preserves the original case.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqo𖪿914crJ@-7zZ54:827
?5𞿠ὄ𝗈82J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs legacy | `beshare://2406TUm7F68SmK2m3a/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs legacy | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `3324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs legacy | `acap://05窊򶩏P@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV?#` | `i4oh44ho008i3fosf.13010z1)av50l7txfuz213lv` | `I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` |
| whatwg vs legacy | `jar://70odWU9.66:7AzV33629mAxq3Dn@52.6.7Dm0t6/E3g{^0R4I6?#` | `52.6.7dm0t6` | `52.6.7Dm0t6` |
| whatwg vs legacy | `iris.xpc://ub239@9Ao0o7M4?#` | `9ao0o7m4` | `9Ao0o7M4` |
| whatwg vs legacy | `otpauth://uw49@9cVDJ86M298V48?#9` | `9cvdj86m298v48` | `9cVDJ86M298V48` |
| whatwg vs legacy | `jabberXsieveIms-getofficeTsmsnihgmodempms-settings-wifi://98hIAuC60ZeFJep0N04/../8DFW1TJ--6-.-s8M.-51..7L2:58?#` | `98hiauc60zefjep0n04` | `98hIAuC60ZeFJep0N04` |
| whatwg vs legacy | `openpgp4fpr://8G/.BUx34@[1d:9:4:f:8:D:Ec:6D]?#` | `8g` | `8G` |
| whatwg vs legacy | `coaps://G7y2)j7@05.15.63.9517_AjZzlS#` | `05.15.63.9517_ajzzls` | `05.15.63.9517_AjZzlS` |
| whatwg vs legacy | `hxxps://5N7QEk1J5o4/;` | `5n7qek1j5o4` | `5N7QEk1J5o4` |
| whatwg vs legacy | `content://3IrRU/嫿12@r.x3:6319T9?` | `3irru` | `3IrRU` |
| whatwg vs legacy | `ms-virtualtouchpad://oh641F/...?` | `oh641f` | `oh641F` |
| whatwg vs legacy | `unreal://894HBW/../480@30.01.9.16:4?#` | `894hbw` | `894HBW` |
| whatwg vs legacy | `data://fzqjL?@637d5.a-wBj.` | `fzqjl` | `fzqjL` |
| whatwg vs legacy | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴6377723lG8J6O0u)!82?#` | `0ph.` | `0pH.` |
| whatwg vs legacy | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~e,0i2IX@1j36y_82.Fv#` | `1j36y_82.fv` | `1j36y_82.Fv` |
| whatwg vs legacy | `data://ZH5}+<v8K3u46@[88:9F:b:58:29:e:f4:5D]:1242@Zg4)7t8y288$8Ko03?#` | `zg4)7t8y288$8ko03` | `Zg4)7t8y288$8Ko03` |
| whatwg vs legacy | `ptd25p` | `ptd25p` | `PTD25p` |
| whatwg vs legacy | `chrome://00NV9l99@dP~`Wj3l6317761?#` | `dp~` | `dP~`Wj3l6317761` |
| whatwg vs url-parse | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#` | `.8agd-.64.z64.091.e` | `.8agD-.64.z64.091.E` |
| whatwg vs url-parse | `data://V1OJ��
#^;V#2@Q42:96?#` | `v1oj%f2%86%af%84%04%02` | `v1oj��` |
| whatwg vs url-parse | `data://8ttF0y𓦸
"?@0.33-t55?#` | `8ttf0y%f3%9b%a5%b8"` | `8ttf0y𓦸"` |
| whatwg vs url-parse | `acap://05@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV?#` | `i4oh44ho008i3fosf.13010z1)av50l7txfuz213lv` | `I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` |
| legacy vs rust-url | `data://PTD25p#@?` | `PTD25p` | `ptd25p` |
| legacy vs rust-url | `unreal://894HBW/../?#` | `894HBW` | `894hbw` |
| javascript-whatwg vs javascript-legacy | `lastfm://vQ931tsj0/../dhqo` | `vQ931tsj0` | `vq931tsj0` |
| javascript-whatwg vs javascript-legacy | `beshare://2406TUm7F68SmK2m3a/...Q` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| javascript-whatwg vs javascript-legacy | `iris.xpc://...@9Ao0o7M4` | `9Ao0o7M4` | `9ao0o7m4` |
| javascript-whatwg vs javascript-legacy | `otpauth://...@9cVDJ86M298V48` | `9cVDJ86M298V48` | `9cvdj86m298v48` |
| javascript-whatwg vs javascript-legacy | `onenote://...@1j36y_82.Fv` | `1j36y_82.Fv` | `1j36y_82.fv` |
| javascript-whatwg vs javascript-legacy | `jar://...@52.6.7Dm0t6` | `52.6.7Dm0t6` | `52.6.7dm0t6` |
| javascript-whatwg vs javascript-legacy | `data://Zg4)7t8y288$8Ko03` | `Zg4)7t8y288$8Ko03` | `zg4)7t8y288$8ko03` |
| javascript-whatwg vs javascript-legacy | `content://3IrRU/` | `3IrRU` | `3irru` |
| javascript-whatwg vs javascript-legacy | `hxxps://5N7QEk1J5o4/` | `5N7QEk1J5o4` | `5n7qek1j5o4` |
| javascript-whatwg vs javascript-legacy | `acap://...@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` | `i4oh44ho008i3fosf.13010z1)av50l7txfuz213lv` | `I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` |
| javascript-whatwg vs javascript-legacy | `data://ptd25p#@...` | `ptd25p` | `PTD25p` |
| javascript-whatwg vs javascript-legacy | `data://fzqjL?` | `fzqjL` | `fzqjl` |
| javascript-whatwg vs javascript-legacy | `openpgp4fpr://8G/.` | `8G` | `8g` |
| javascript-whatwg vs javascript-legacy | `unreal://894HBW/` | `894hbw` | `894HBW` |
| javascript-whatwg vs javascript-legacy | `coaps://...@05.15.63.9517_AjZzlS` | `05.15.63.9517_AjZzlS` | `05.15.63.9517_ajzzls` |
| javascript-whatwg vs javascript-legacy | `jabberXsieve://98hIAuC60ZeFJep0N04/` | `98hIAuC60ZeFJep0N04` | `98hiauc60zefjep0n04` |
| javascript-whatwg vs javascript-legacy | `ms-settings-lock://0pH.` | `0pH.` | `0ph.` |
| javascript-whatwg vs javascript-parse-uri | `lastfm://vQ931tsj0/../` | `hrl49V3Q50` | `hrl49v3q50` |
| javascript-whatwg vs javascript-parse-uri | `beshare://...` | `z9i6z786v06` | `Z9I6Z786V06` |
| javascript-whatwg vs javascript-parse-uri | `wss://...@f..7S1j-2..dO6-B-In:8` | `f..7s1j-2..do6-b-in` | `f..7S1j-2..dO6-B-In` |
| javascript-whatwg vs javascript-parse-uri | `otpauth://...` | `44M` | `44m` |
| javascript-whatwg vs javascript-parse-uri | `ms-settings-cellular://...` | `0.JM18` | `0.jm18` |
| javascript-whatwg vs javascript-parse-uri | `jar://...` | `0xp298i3w4677703l0n` | `0XP298i3w4677703l0n` |
| javascript-whatwg vs javascript-parse-uri | `content://...` | `vkb8n8cf03s89` | `vKb8N8Cf03S89` |
