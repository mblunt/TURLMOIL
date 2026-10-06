# Bracket Notation in Key Name Mangled

**Description:** Some parsers (notably PHP's parse_str) interpret `[` in query key names as PHP-style array bracket notation, stripping or transforming the bracket portion, while others treat `[` as a literal character and preserve it in the key name.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| php-parseurl vs python-urllib3 | `򗗣GaimawunrealturnsTchromeK⛏촭jWQ9://B7o14752tREp@@[cb:e3:FD:7:F:C2:F:F]:47⌵7򅼂(/80~HAC`g505!4W1jD6?[(_5=2"7T95G&L:=i/*$1/#` | `["L:"]` | `["[(_5", "L:"]` |
| php-parseurl vs python-urllib3 | `://I:I񅵞➋y0@12.73.15.9:87z NP5Ἓ4V?[V17?e';j(_U=i9A&_=5#` | `["_"]` | `["[V17?e';j(_U", "_"]` |
| php-parseurl vs python-urllib3 | `://r𪏻22=A㸅
񠨗򳧴W7󖗐᫉97740Y61923750236yT:04813750547􉡫Ϭ2B|O[0G7nD02Dh9tN6K?CS7-[8NzQ0=k닆􋒭` | `["CS7-_8NzQ0"]` | `["CS7-[8NzQ0"]` |
| php-parseurl vs python-urllib3 | `ms-infopath7psyc𴗜://2򦿯4/..$d᣸⨦@7Sy3.5ta-.t	􋆫񉡹PspA0}2cyK2Q19IDlw1?5;B9"{-0]s[&]x&[H=|#Y80` | `["5;B9\"{-0]s_", "]x"]` | `[["H"]` |
| php-parseurl vs python-urllib3 | `⎖aptmailserverturnsubmitFms-useractivitysetN⳻ms-settings-airplanemode򕮕cxmpp𥺊imsrpsms-sttoverlay://:wj࠱⦙
󺓣:8177𙻨󰲷𦬞񢹂I02"88` | `["9N", "40__*\"T$s", "_}B{3^n", "]_", ")6"]` | `["9N", "40_[*\"T$s", "] "]` |
| php-parseurl vs python-urllib3 | `劖R􃙂|	marketsmsnim://4z12332e8iv21M6ESrI:Sq447E@[Aa:Ce:d:b:E:1:B:F]:􊲛󷟑},6Ô𠠬{R91u&Ct7~?22=08_'p-yQ2TVi&7!|o&ZSE5&[@=^` | `["22", "7!|o", "ZSE5"]` | `["22", "[@"]` |
| php-parseurl vs python-urllib3 | `//wss://5A>x𢑗Y
ELO..93A0-.e:8p$naD󤮺O0Y2789B4j5O{rI1a14?_=W3&*=3.K_9K4]&7[9PIpS='%Jh1` | `["_", "*", "7_9PIpS"]` | `["_", "*", "7[9PIpS"]` |
| php-parseurl vs python-urllib3 | `ftp://http://12L3:X13v9n06sII@65.45.9.9P潀34󺷼h𧋶'8K+G2)v0kZ87a8o4{:o?f20[5*|23rNI=(cxO_&#=` | `["f20_5*|23rNI"]` | `["f20[5*|23rNI"]` |
| php-parseurl vs python-urllib3 | `;:5_[c:5:E:C3:33:C:b:Be]:234"1mQ;◼?5n*`+)6+8[+=W2&]0&k}6:!-]=--W/((^H@3|g},4@&2=MP55E,` | `["5n*`_)6_8__", "]0", "k}6:!-]", "2"]` | `["5n*` )6 8[ ", "k}6:!-]", "2"]` |
| php-parseurl vs python-urllib3 | `𨌧JTxmlrpc.beepudp://62Fmd5O6C5kj651k699:otq
􉙿4􈬻⋾H:91F5po2iyxt207L033`4?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WT` | `["tRHuA,8", "A_Q09,M78", "7K;04k_C0", "Il", "|__@..."]` | `["A_Q09,M78"]` |
| php-parseurl vs python-yarl | `𩴧GaimawunrealturnsTchromeK⛏촭jWQ9://B7o14752tREp@@[cb:e3:FD:7:F:C2:F:F]:47⌵...?[(_5=2"7T95G&L:=i/*$1/` | `["L:"]` | `["[(_5", "L:"]` |
| php-parseurl vs python-yarl | `data://http://^;...?^1v3.5$(=`"4Q.` | `["^1v3_5$("]` | `["^1v3.5$("]` |
| php-parseurl vs javascript-whatwg | `GaimawunrealturnsTchromeK...?[(_5=2"7T95G&L:=i/*$1/` | `["L:"]` | `["[(_5", "L:"]` |
| php-spatie vs python-urllib3 | `ws://3sI52lm9EKS134v20ZY?"*[@\!+&P~u@` | `["\"*_@\\!_", "P~u@"]` | `["\"*[@\\! ", "P~u@"]` |
| php-parseurl vs python-urllib3 | `://I:I...?[V17?e';j(_U=i9A&_=5` | `["_"]` | `["[V17?e';j(_U", "_"]` |
| php-spatie vs python-urllib3 | `nntpsK[?v[rmi://...&;&^&&5o]=Y-H|9Q,B` | `["v_rmi://...", "m7", ";", "^", "5o]"]` | `["5o]"]` |
| php-parseurl vs python-urllib3 | `?[(_5=2"7T95G&L:=i/*$1/` | `{"L:": "i/*$1/"}` | `{"[(_5": ["2\"7T95G"], "L:": ["i/*$1/"]}` |
| php-parseurl vs python-urllib3 | `?=I"%4Fr:1-%60T08%3D%5B2%21` | `[]` | `{"":["I\"Or:1-`T08=[2!"]}` |
| php-parseurl vs python-urllib3 | `?{3"&5-672GMU{\=` | `{"{3\"": "", "5-672GMU{\\":""}}` | `{}` |
| php-parseurl vs python-urllib3 | `?[V17?e';j(_U=i9A&_=5` | `{"_": "5"}` | `{"[V17?e';j(_U": ["i9A"], "_": ["5"]}` |
| php-parseurl vs python-urllib3 | `?[(_5=2"7T95G&L:=i/*$1/` | `{"L:": "i/*$1/"}` | `{"[(_5": ["2\"7T95G"], "L:": ["i/*$1/"]}` |
| php-parseurl vs python-urllib3 | `?CS7-[8NzQ0=k닆􋒭` | `{"CS7-_8NzQ0": "k\ub2c6\udbed\udcad"}` | `{"CS7-[8NzQ0": ["k\ub2c6\udbed\udcad"]}` |
| php-parseurl vs python-urllib3 | `?4@*STt&a6=_74lpZ1[4m(6` | `{"4@*STt": "", "a6": "_74lpZ1[4m(6"}` | `{"a6": ["_74lpZ1[4m(6"]}` |
| php-parseurl vs python-urllib3 | `?f20[5*|23rNI=(cxO_&` | `{"f20_5*|23rNI": "(cxO_"}` | `{"f20[5*|23rNI": ["(cxO_"]}` |
| php-parseurl vs python-urllib3 | `?7À¸[&v9Y!=@8` | `{"7\u00c0\u00b8_": "", "v9Y!": "@8"}` | `{"v9Y!": ["@8"]}` |
| php-parseurl vs python-urllib3 | `?22=08_'p-yQ2TVi&7!|o&ZSE5&[@=^` | `{"22": "08_'p-yQ2TVi", "7!|o": "", "ZSE5": ""}` | `{"22": ["08_'p-yQ2TVi"], "[@": ["^"]}` |
| php-parseurl vs python-urllib3 | `?[&3n"'` | `{"3n\"'": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?9N=*")&40_[*"T$s=g&_}B{3^n&]+=-&)6` | `{"9N": "*\")", "40__*\"T$s": "g", "_}B{3^n": "", "]_": "-", ")6": ""}` | `{"9N": ["*\")"], "40_[*\"T$s": ["g"], "] ": ["-"]}` |
| rust-url vs php-parseurl | `?^I[񿜑92^ᵒD鶙` | `{"^I\u000b[\ud9bd\udf1192^\u1d52D\u9d99": [""]}` | `{"^I__\ud9bd\udf1192^\u1d52D\u9d99": ""}` |
| rust-url vs php-parseurl | `?wss://...⧁ 󴕕+⡑c` | `{"⧁ 󴕕 ⡑c": [""]}` | `{"⧁_󴕕_⡑c": ""}` |
| rust-url vs php-parseurl | `?...99...644[0=\|...` | `{"99...�...644[0": ["\\|"]}` | `{"99...�...644_0": "\\|"}` |
