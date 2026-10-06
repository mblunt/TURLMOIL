# No-Value Key: null vs Empty String

**Description:** For keys without a value (e.g. ?key or ?key=), one parser stores the value as null while another stores it as an empty string "".

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib71 (php-parseurl) vs lib72 (php-spatie) | `)://k...?Fi.5&.G2{84[=6260|4^` | `{"Fi_5": "", "_G2{84_": "6260|4^"} (empty string for no-value key)` | `{"Fi_5": null, "_G2{84_": "6260|4^"} (null for no-value key)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `://X...:R84J@...?D=s{@13-X&N&|-2PV{#5` | `{"D": "s{@13-X", "N": "", "|-2PV{": ""} (empty strings)` | `{"D": "s{@13-X", "N": null, "|-2PV{": null} (nulls)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `sip:////:J142E@:6=\t(3dǶ0?W!!=*:M2e4#7j` | `{"W!!": ["*:M2e4"]} (array value)` | `{"W!!": "*:M2e4"} (string value)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `%53fe%65%64read%79m%73...?=I"%4Fr:1-%60T08%3D%5B2%21` | `{"":["I\"Or:1-`T08=[2!"]} (empty key, array val)` | `{"":"I\"Or:1-`T08=[2!"} (empty key, string val)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `shttp...?{3"&5-672GMU{\=||...{3"&5-672GMU{\=` | `{"{3\"": "", "5-672GMU{\\" : ""} (empty strings)` | `null` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `Sg(nipp...?...51&&s...761...$?+nQ...eᅃ..._c` | `{} (empty - no keys parsed)` | `{"...": null, "\u000b\u001f": null, ...} (nulls for keys without values)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `wss://y21zEU1@S-3n7...?w=1&S"{443=79&L&`^'8` | `{"w": ["1"], "S\"{443": ["79"]} (L and `^'8 omitted - no-value keys ignored)` | `{"w": "1", "S\"{443": "79", "L": "", "`^'8": ""} (empty string for no-value keys)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `acctreloadmagnetboloed2k...?4@*STt&a6=_74lpZ1[4m(6` | `{"a6": ["_74lpZ1[4m(6"]} (no-value key 4@*STt omitted)` | `{"4@*STt": "", "a6": "_74lpZ1[4m(6"} (empty string for no-value key)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `acctreloadmagnet...?4@*STt&a6=_74lpZ1[4m(6` | `{"a6": ["_74lpZ1[4m(6"]} (4@*STt omitted)` | `{"4@*STt": null, "a6": "_74lpZ1[4m(6"} (null for no-value key)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@...` | `{"A_Q09,M78": ["pOn"]} (no-value keys tRHuA,8 etc. omitted)` | `{"tRHuA,8": null, "A_Q09,M78": "pOn", "7K;04k[C0": null, "Il": null, ...: null} (nulls for no-value keys)` |
| js-whatwg vs python-furl | `http:/6s70j7/,z8494wU-?"2/	솀5򘵽𫅴퀏` | `["\"2/\t솀5..."]` | `["\"2/\t솀5..."]` |
| js-whatwg vs python-furl | `wss://6713p0l690n15y78/.1HD:w??⧁ 󴕕 ⡑c` | `["⧁ 󴕕 ⡑c"]` | `["⧁ 󴕕 ⡑c"]` |
| js-whatwg vs python-furl | `rediss://bfl?994)|...3qu252Ss:0^I644[0=\|&7(s\5*=0!!\^&` | `["99...", "7(s\\5*"]` | `["99...", "7(s\\5*", ""]` |
| js-whatwg vs python-furl | `ftp://oV9u31/../?V"00'=.N&7:` | `["V\"00'", "7:"]` | `["V\"00'", "7:"]` |
| js-whatwg vs python-furl | `popenpgp4fpr://:9@??𠘛` | `["𠘛"]` | `["𠘛"]` |
| js-whatwg vs python-furl | `crid://HE7N16Uk/?􋚈Ḍ⓶E` | `["􋚈Ḍ⓶E"]` | `["􋚈Ḍ⓶E"]` |
| js-whatwg vs python-furl | `file:///2y6490y..?*40DfV` | `["*40DfV"]` | `["*40DfV"]` |
| js-whatwg vs python-furl | `wss://?2R4X󾙑7}` | `["2R4X󾙑7}"]` | `["2R4X󾙑7}"]` |
| php-spatie vs python-urllib3 | `://X񧅠:R84J@.?D=s{@13-X&N&|-2PV{` | `["D", "N", "|-2PV{"]` | `["D"]` |
| php-spatie vs python-urllib3 | `)://k⭕iD1?Fi.5&.G2{84[=6260|4^` | `["Fi_5", "_G2{84_"]` | `[".G2{84["]` |
| php-spatie vs python-urllib3 | `stunbitcoinl...?12Zq13S&n.L83a'45=P5]95o0:3` | `["12Zq13S", "n_L83a'45"]` | `["n.L83a'45"]` |
| php-spatie vs python-urllib3 | `udp://...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `["tRHuA,8", "A_Q09,M78", "7K;04k_C0", "Il", "|__@\"2:O~}e;WTI^A264H"]` | `["A_Q09,M78"]` |
| php-parseurl vs php-spatie | `://X񜭠:R84J@....?D=s{@13-X&N&|-2PV{#5|D=s{@13-X&N&|-2PV{` | `{"D":"s{@13-X", "N":"", "|-2PV{":""}` | `{"D":"s{@13-X", "N":null, "|-2PV{":null}` |
| php-parseurl vs php-spatie | `)://k⭕iD1...?Fi.5&.G2{84[=6260|4^` | `{"Fi_5":"", "_G2{84_":"6260|4^"}` | `{"Fi_5":null, "_G2{84_":"6260|4^"}` |
| php-parseurl vs php-spatie | `𨌧JTxmlrpc.beepudp://...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"tRHuA,8":"", "A_Q09,M78":"pOn", "7K;04k_C0":"", "Il":"", "|__@\"2:O~}e;WTI^A264H":""}` | `{"tRHuA,8":null, "A_Q09,M78":"pOn", "7K;04k_C0":null, "Il":null, "|__@\"2:O~}e;WTI^A264H":null}` |
| php-parseurl vs php-spatie | `stunbitcoinlXmms...?12Zq13S&n.L83a'45=P5]95o0:3#` | `{"12Zq13S":"", "n_L83a'45":"P5]95o0:3"}` | `{"12Zq13S":null, "n_L83a'45":"P5]95o0:3"}` |
| php-parseurl vs php-spatie | `𞲀ms-godlna-playsinglestun...?&-i|m-&15==#S7+JA7P|&-i|m-&15==` | `{"-i|m-":"", "15":"="}` | `{"-i|m-":null, "15":"="}` |
| php-parseurl vs php-spatie | `://8r4RJ4WunSK8Vk4:...?	8?9=7Dv3_bL+-&6=`=_A&t8\#kJU4` | `{"_8?9":"7Dv3_bL -", "6":"`=_A", "t8\\":""}` | `{"_8?9":"7Dv3_bL -", "6":"`=_A", "t8\\":null}` |
| php-parseurl vs php-spatie | `wtaiggTunrealdrmadium...facetime://...?$:Y=^a_u9r2i6{&3}!"=ch&{8,S0=~"&ry_K2&rM:[&J6m&4+xf52=C~*75h_Nn9)88&~A=|80-`(~}Q+` | `{"$:Y":"^a_u9r2i6{", "3}!\"":"ch", "{8,S0":"~\"", "ry_K2":"", "rM:_":"", "J6m":"", "4_xf52":"C~*75h_Nn9)88", "~A":"|80-`(~}Q "}` | `{"ry_K2":null, "rM:_":null, "J6m":null}` |
| php-parseurl vs php-spatie | `Á³mÁ³:/À¯...?7À¸[&v9Y!=@8#` | `{"7\u00c0\u00b8_":"", "v9Y!":"@8"}` | `{"7\u00c0\u00b8_":null, "v9Y!":"@8"}` |
| python-furl vs python-yarl | `http:/%252F%2552v%2535%25320O4IM5%2539.43.2%2537.8%255F6O1%2535?%0C%25315%253F` | `{"%315%3F": null}` | `{"%315%3F": ""}` |
| python-furl vs python-yarl | `http:/\/\b8v89b6D:0q6k$|@P3KM2.G.j9-vcy5-b-.:?599/` | `{"599/": null}` | `{"599/": ""}` |
| python-furl vs python-yarl | `?F?"W:74~s_N` | `{"F?\"W:74~s_N": null}` | `{"F?\"W:74~s_N": ""}` |
| python-furl vs python-yarl | `?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"tRHuA,8": null, "A_Q09,M78": "pOn", "7K;04k[C0": null, "Il": null, "|[ @\"2:O~}e;WTI^A264H": null}` | `{"tRHuA,8": "", "A_Q09,M78": "pOn", "7K;04k[C0": "", "Il": "", "|[ @\"2:O~}e;WTI^A264H": ""}` |
| python-furl vs python-yarl | `?'W0^'\28'.5a~dD31=w41_n8&0` | `{"'W0^'\\28'.5a~dD31": "w41_n8", "0": null}` | `{"'W0^'\\28'.5a~dD31": "w41_n8", "0": ""}` |
| python-furl vs python-yarl | `?+).=&q2J"0&5)u` | `{"+).": "", "q2J\"0": null, "5)u": null}` | `{"+).": "", "q2J\"0": "", "5)u": ""}` |
| python-furl vs python-yarl | `?($4PDY),Z=%6D2%33&%38&%3D=%7B%23pP%77` | `{"($4PDY),Z": "%6D2%33", "%38": null, "%3D": "%7B%23pP%77"}` | `{"($4PDY),Z": "%6D2%33", "%38": "", "%3D": "%7B%23pP%77"}` |
| python-furl vs python-yarl | `?$&spP00&r1&7{"6$.p={p&^` | `{"$": null, "spP00": null, "r1": null, "7{\"6$.p": "{p", "^": null}` | `{"$": "", "spP00": "", "r1": "", "7{\"6$.p": "{p", "^": ""}` |
| python-furl vs python-httpx | `?8m84:` | `{"8m84:": null}` | `{"8m84:": ""}` |
| python-furl vs python-httpx | `?{+|I+` | `{"{+|I": null}` | `{"{+|I": ""}` |
| python-furl vs python-httpx | `?{&s05u")&c="+&{` | `{"{":null,"s05u\")":null,"c":"\" "}` | `{"{":"","s05u\")":"","c":"\" "}` |
| python-furl vs python-httpx | `?%277{%23` | `{"%277{%23": null}` | `{"%277{%23": ""}` |
| python-yarl vs python-furl | `?%315%3F` | `{"%315%3F": ""}` | `{"%315%3F": null}` |
| python-yarl vs python-furl | `?599/` | `{"599/": ""}` | `{"599/": null}` |
| python-yarl vs python-furl | `?@|138{⓫HX` | `{"@|138{\u24eb\u0017HX": ""}` | `{"@|138{\u24eb\u0017HX": null}` |
| python-yarl vs python-furl | `?F?"W:74~s_N` | `{"F?\"W:74~s_N": ""}` | `{"F?\"W:74~s_N": null}` |
| python-yarl vs python-furl | `?򉉁?K\𡯚}m7*O7` | `{"...": ""}` | `{"...": null}` |
| python-yarl vs python-furl | `?x^`N7~7G።0` | `{"x^`N7~7G\u13620": ""}` | `{"x^`N7~7G\u13620": null}` |
| python-yarl vs python-furl | `?%%330%5%42`Ӳl%%32%33ࣱ` | `{"%%330%5%42`\u04f2l%%32%33\u08f1": ""}` | `{"%%330%5%42`\u04f2l%%32%33\u08f1": null}` |
| python-yarl vs python-furl | `?ບ6켯Mn1FCuv539Q!UOCc9mN4ᆕ8}‾` | `{"...": ""}` | `{"...": null}` |
