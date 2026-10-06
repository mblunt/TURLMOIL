# Dot in Key Name Replaced

**Description:** Some parsers (notably PHP's parse_str) replace dots and spaces in key names with underscores, while others preserve the original dot characters.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib71 (php-parseurl) vs lib72 (php-spatie) | `)://k...?Fi.5&.G2{84[=6260|4^` | `{"Fi_5": "", "_G2{84_": "6260|4^"} (dots replaced with underscores by PHP parse_str)` | `{"Fi.5": null, ".G2{84[": "6260|4^"} (dots preserved)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `://D0W2...?F...?Q?+𦁷8Y#C6b` | `{"F..._Q?_𦁷8_Y": ""} (dots → underscores)` | `null` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `...?G.Xh:5(w&` | `{"G.Xh:5(w": null} (dot kept by furl)` | `missing key (urllib3 drops it?)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `...?Z4;9r(;HU36148E.;X&Z4;9r(;HU36148E.;X` | `{"Z4;9r(;HU36148E_;_X": ""} (dot+space→underscore)` | `null` |
| php-parseurl vs python-urllib3 | `)://k⯕iD1󯟴_5ªℿ:
􉙚󲫿N+𠧗𤽖 붙𥓫♋�d?Fi.5&.G2{84[=6260|4^` | `["Fi_5", "_G2{84_"]` | `[".G2{84["]` |
| php-parseurl vs python-urllib3 | `timessagecvst⠔祚石wtaiturnsresource8(+𡓭Ἔ\
��$?yK2Ps1f8TC8XP:41񫲌G--5-1.7331-wg4.]\^$53󵎣". N=wT:&==J6c2.ꕺ3/#6` | `["yK2Ps1f8TC8XP:41..._7331-wg4_]..."]` | `["yK2Ps1f8TC8XP:41....7331-wg4.]...", ""]` |
| php-parseurl vs python-urllib3 | `stunbitcoinlXmms󱷭://nd474LU5065Od8:@[d:9e:0:d:b:DB:4:c]:E		n 뵙�0A$2if984732068p3AYs?12Zq13S&n.L83a'45=P5]95o0:3#` | `["12Zq13S", "n_L83a'45"]` | `["n.L83a'45"]` |
| js-whatwg vs php-parseurl | `data://http://^;􍿉𝠯"H86K
6$*􃼫02.15.70.41:v07𮀽;:?^1v3.5$(=`"4Q.#6Rd` | `["^1v3.5$("]` | `["^1v3_5$("]` |
| php-parseurl vs python-urllib3 | `http://: b񣓤@B.yEz45B:2_C0}z6e5d@x0pb~i!xk3?.8#9` | `["_8"]` | `[".8"]` |
| php-parseurl vs python-yarl | `data://http://^;...?^1v3.5$(=`"4Q.` | `["^1v3_5$("]` | `["^1v3.5$("]` |
| php-parseurl vs python-yarl | `timessagecvst...?yK2Ps1f8TC8XP:41...1.7331-wg4.]\^$53...". N=wT:` | `["yK2Ps1f8TC8XP:41...1_7331-wg4_]..."]` | `["yK2Ps1f8TC8XP:41...1.7331-wg4.]..."]` |
| php-parseurl vs python-urllib3 | `timessage...?yK2Ps1f8TC8XP:41...G--5-1.7331-wg4.]\^$53...+N=wT:&==J6c2.` | `"yK2Ps1f8TC8XP:41...G--5-1_7331-wg4_]\\^$53...\"__N"` | `"yK2Ps1f8TC8XP:41...G--5-1.7331-wg4.]\\^$53...\". N"` |
| php-parseurl vs python-urllib3 | `data://http://^;...?^1v3.5$(=`"4Q.` | `"^1v3_5$("` | `"^1v3.5$("` |
| php-parseurl vs python-urllib3 | `)://k...?Fi.5&.G2{84[=6260|4^` | `"Fi_5", "_G2{84_"` | `".G2{84["` |
| php-spatie vs python-urllib3 | `stunbitcoinlXmms...?12Zq13S&n.L83a'45=P5]95o0:3` | `["12Zq13S", "n_L83a'45"]` | `["n.L83a'45"]` |
| php-parseurl vs python-urllib3 | `://I:I...?[V17?e';j(_U=i9A&_=5` | `["_"]` | `["_"]` |
| php-parseurl vs python-urllib3 | `?Fi.5&.G2{84[=6260|4^` | `{"Fi_5": "", "_G2{84_": "6260|4^"}` | `{".G2{84[": ["6260|4^"]}` |
| php-parseurl vs python-urllib3 | `?yK2Ps1f8TC8XP:41...&.+N=wT:` | `{"yK2Ps1f8TC8XP:41...": "", "__N": "wT:"}` | `{"yK2Ps1f8TC8XP:41...": ["wT:"]}` |
| php-parseurl vs python-urllib3 | `?Z4;9r(;HU36148E.;⧪X` | `{"Z4;9r(;HU36148E_;⧪_X": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?2P7-  94\87=` | `{"2P7-____94\\87": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?䅘\;⎸⬼˲8⩾򠡨X74.26.5.62:s2񀃺?` | `{"䅘\\;⎸⬼_˲_8⩾򠡨_X74_26_5_62:s2񀃺?": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?\Àª*5` | `{"\\Àª_*_5": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?_ ,󺬛` | `{"__,󺬛": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?^1v3.5$(=`"4Q.` | `{"^1v3_5$(": "`\"4Q."}` | `{"^1v3.5$(": ["`\"4Q."]}` |
| php-parseurl vs python-urllib3 | `?12Zq13S&n.L83a'45=P5]95o0:3` | `{"12Zq13S": "", "n_L83a'45": "P5]95o0:3"}` | `{"n.L83a'45": ["P5]95o0:3"]}` |
| php-parseurl vs python-urllib3 | `?4".ILeB` | `{"4\"_ILeB": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?Z4;9r(;HU36148E.;⧪_X` | `{"Z4;9r(;HU36148E_;⧪_X": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?nZEO.w` | `{"nZEO_w": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?\-.=p$|CJ&` | `{"\\-_": "p$|CJ"}` | `{"\\-.": ["p$|CJ"]}` |
| php-parseurl vs python-urllib3 | `?:5.189O9.nm43D3...?3` | `{"|:5_189O9_nm43D3...": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?:035␡.&'뗹]񶝬薵` | `{"|:035␡_": "", "'\ub5f9]_\udb99\udf6c___\u85b5_": ""}` | `{}` |
| rust-url vs php-parseurl | `?^1v3.5$(=`"4Q.` | `{"^1v3.5$(": ["`\"4Q."]}` | `{"^1v3_5$(": "`\"4Q."}` |
| rust-url vs php-parseurl | `?Z4;9r(;HU36148E.;⧪_X&Z4;9r(;HU36148E.;⧪_X` | `{"Z4;9r(;HU36148E.;⧪_X": ["", ""]}` | `{"Z4;9r(;HU36148E_;⧪_X": ""}` |
| rust-url vs php-parseurl | `?"2/	솀5...` | `{"\"2/\uc1805...": [""]}` | `{"\"2/_\uc1805..._": ""}` |
| perl-uri vs php-parseurl | `?Fd9-=+`VLc"i&6{~YK0=9${` | `{"6{~YK0": "9${", "Fd9-": " `VLc\"i"}` | `{"Fd9-": " `VLc\"i", "6{~YK0": "9${"}` |
