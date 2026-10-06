# Duplicate Key: Array vs String

**Description:** When the same key appears multiple times in the query string, one parser stores values as an array while another keeps only one value as a string.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib1 (whatwg) vs lib2 (legacy) | `bolofilesystem.://?A.@:r/1...BO2j@=1/...m2&A.@:r/1...BO2j@=1/...m2#` | `{"A.@:r.../1...BO2j@": "1/...m2"} (single string)` | `{"A.@:r.../1...BO2j@": ["1/...m2", "1/...m2"]} (array)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `sip:////:J142E@:6=\t(3dǶ0?W!!=*:M2e4#7j` | `{"W!!": ["*:M2e4"]} (array for duplicate)` | `{"W!!": "*:M2e4"} (single string)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `acctreloadmagnetboloed2k...?4@*STt&a6=_74lpZ1[4m(6` | `{"a6": ["_74lpZ1[4m(6"]} (array)` | `{"4@*STt": null, "a6": "_74lpZ1[4m(6"} (string)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `|...ldap...?:/R=^@*u#7O00Z5` | `{":/R...": ["^@*u"]} (array)` | `{":/R...": "^@*u"} (string)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `...?[(_5=2"7T95G&L:=i/*$1/` | `{"[(_5": ["2\"7T95G"], "L:": ["i/*$1/"]} (arrays)` | `{"[(_5": "2\"7T95G", "L:": "i/*$1/"} (strings)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"A_Q09,M78": ["pOn"]} (array)` | `{"tRHuA,8": null, "A_Q09,M78": "pOn", ...} (string + extra keys)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `wss://y21zEU1@S-3n7-V6I...?w=1&S"{443=79&L&`^'8` | `{"w": ["1"], "S\"{443": ["79"]} (arrays)` | `{"w": "1", "S\"{443": "79", "L": "", "`^'8": ""} (strings + extra keys)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `sip:////:J142E@:...?W!!=*:M2e4` | `{"W!!": ["*:M2e4"]} (array)` | `{"W!!": "*:M2e4"} (string)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `...?4@*STt&a6=_74lpZ1[4m(6` | `{"a6": ["_74lpZ1[4m(6"]} (array, misses first key)` | `{"4@*STt": "", "a6": "_74lpZ1[4m(6"} (strings, includes no-value key)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `...?:/R...=^@*u#7O00Z5` | `{":/R...": ["^@*u"]} (array)` | `{":/R...": "^@*u"} (string)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `...?...5n*`+)6+8[+=W2&]0&k}6:!-]=--W/...&2=MP55E,` | `{"5n*` )6 8[ ": ["W2"], "k}6:!-]": ["--W/..."], "2": ["MP55E,"]} (arrays)` | `{"5n*` )6 8[ ": "W2", "]0": "", "k}6:!-]": "--W/...", "2": "MP55E,"} (strings + extra key)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `ht%74p%73://...?9=4%66%40%23V%31f` | `{"9": ["4f@#V1f"]} (array)` | `{"9": "4f@#V1f"} (string)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `wtai...facetime://...?$:Y=^a_u9r2i6{&3}!"=ch&{8,S0=~"&ry_K2&rM:[&J6m&4+xf52=C~*75h_Nn9)88&~A=|80-`(~}Q+` | `{"$:Y": ["^"], "3}!\"": ["ch"], "{8,S0": ["~\""], "4 xf52": ["C~*75h_Nn9)88"], "~A": ["|80-`(~}Q "]} (arrays)` | `{"$:Y": "^", ... "ry_K2": "", "rM:[": "", "J6m": "", "4 xf52": "C~*75h_Nn9)88", "~A": "|80-`(~}Q "} (strings + extra keys)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `...GaimawunrealturnsT...?[(_5=2"7T95G&L:=i/*$1/` | `{"[(_5": ["2\"7T95G"], "L:": ["i/*$1/"]} (arrays)` | `{"[(_5": "2\"7T95G", "L:": "i/*$1/"} (strings)` |
| php-parseurl vs python-urllib3 | `://櫰󙨱񝅷uy

𠓠∛⡏𖨐38𨄷MH4&,6r7355t9|-ye9E?A=(9&$!OR{=V9t]V\4}#` | `["A", "$!OR{"]` | `["A", "$!OR{"]` |
| php-parseurl vs python-urllib3 | `w%73://O0%6An%76278Ku%369i3%7A76%352t%40𥚰%6C%0A:%3229%79%3Fᅱ%6F,192%42%34R6A378;e%5DXMo%5B6?&Nq=Grs%39#搸ྱ炜%0D𠪳%0B` | `["Nq"]` | `["Nq"]` |
| php-parseurl vs python-urllib3 | `%257B:%252F/%256E𤴓឴몍􂚱6%2531⭆𐴫@3j1%2561%254F%2538m%2533-Z%252D36G9-%25369.:G;6%251C43k񴺣%257E?ZJ*]1$%2538"%2534=S%2577_%25` | `["ZJ*]1$%38\"%34", "%282_"]` | `["ZJ*]1$%38\"%34", "%282_"]` |
| js-whatwg vs python-urllib3 | `sip:////:J142E@:ῃ6=	(3dǶ0?W!!=*:M2e4#7j` | `["W!!"]` | `["W!!"]` |
| js-whatwg vs python-urllib3 | `data://http://^;􍿉𝠯"H86K
6$*􃼫02.15.70.41:v07𮀽;:?^1v3.5$(=`"4Q.#6Rd` | `["^1v3.5$("]` | `["^1v3.5$("]` |
| js-whatwg vs python-urllib3 | `https://ftp://X:X11D@Qz10.:3d5315Y1qH86(2dVSK96?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A#-28,9` | `[" 1g2:", "l", "3~nE-5"]` | `[" 1g2:", "l", "3~nE-5"]` |
| js-whatwg vs python-urllib3 | `bolofilesystem.://?A.@:r⟐/1𤟛BO2j@=1/@;9t177S556<╋𒂟Iޭ/𡁧򊋔󅀩m2&A.@:r⟐/1𤟛BO2j@=1/@;9t177S556<╋𒂟Iޭ/𡁧򊋔󅀩m2#` | `["A.@:r⟐/1..."]` | `["A.@:r⟐/1...", "A.@:r⟐/1..."]` |
| rust-url vs js-whatwg | `wss://..?w=1&S"{443=79&L&`^'8` | `["w", "S\"{443", "L", "`^'8"]` | `["w", "S\"{443", "L", "`^'8"]` |
| rust-url vs js-whatwg | `sip:////:J142E@:?W!!=*:M2e4` | `["W!!"]` | `["W!!"]` |
| rust-url vs js-whatwg | `da%74a://..?}7=]=22_A;9q45&+~=54o1hJ7^{,_=9%267p6]m&"^58=04;-8fDv25&@cqNb=^` | `["}7", "+~", "\"^58"]` | `["}7", "+~", "\"^58"]` |
| python-urllib3 vs python-yarl | `file://https://gbc9r6p7h.?_2~3-=+}|&!6ZC` | `["_2~3-"]` | `["_2~3-", "!6ZC"]` |
| python-urllib3 vs python-yarl | `%53fe%65%64read%79m%73-...?=I"%4Fr:1-%60T08%3D%5B2%21` | `[""]` | `[""]` |
| python-urllib3 vs python-yarl | `da%74a://..?}7=]=22_A;9q45&+~=54o1hJ7&"^58=04` | `["}7", "+~", "\"^58"]` | `["}7", "+~", "\"^58"]` |
| php-spatie vs python-urllib3 | `://橰񩫡򍾷uy?A=(9&$!OR{=V9t]V\4}` | `["A", "$!OR{"]` | `["A", "$!OR{"]` |
| php-spatie vs python-urllib3 | `%53fe%65%64...?=I"%4Fr:1-%60T08%3D%5B2%21` | `[""]` | `[""]` |
| php-spatie vs python-urllib3 | `da%74a://...?}7=]=22_A;9q45&+~=54o1hJ7^{,_=9%267p6]m&"^58=04;-8fDv25&@cqNb=^` | `["}7", "+~", "\"^58"]` | `["}7", "+~", "\"^58"]` |
| php-spatie vs python-urllib3 | `wss://...?[(_5=2"7T95G&L:=i/*$1/` | `["L:"]` | `["L:"]` |
| python-urllib3 vs python-yarl | `file://...?_2~3-=+}|&!6ZC` | `["_2~3-", "!6ZC"]` | `["_2~3-"]` |
| python-urllib3 vs python-yarl | `sip://...?W!!=*:M2e4` | `["W!!"]` | `["W!!"]` |
| javascript-whatwg vs python-urllib3 | `mongodb://...?FR4'06iEj"7$|="U(=@R!55c_8t!/]59` | `["FR4'06iEj\"7$|"]` | `["FR4'06iEj\"7$|"]` |
| javascript-whatwg vs python-urllib3 | `data://...?ZJ*]1$%2538"%2534=S%2577_%256F0%2565%2526&%25282_=59;;%2540...` | `["ZJ*]1$%38\"%34", "%282_"]` | `["ZJ*]1$%38\"%34", "%282_"]` |
| go-net vs python-urllib3 | `data://ftp://:11A@0.69.2.2:8...'?0=]A01=j&0&#1'zP` | `{"0":["]A01=j", ""]}` | `{"0":["]A01=j"]}` |
| elixir-uri vs python-urllib3 | `𨌧JTxmlrpc.beepudp://...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"$:Y":"^a_u9r2i6{", "3}!\"":"ch", "4 xf52":"C~*75h_Nn9)88", "J6m":"", "rM:[": "", "ry_K2":"", "{8,S0":"~\"", "~A":"|80-`(~}Q "}` | `{"$:Y":["^"], "3}!\"":["ch"], "4 xf52":["C~..."], "~A":["|"]}` |
| elixir-uri vs python-urllib3 | `file://TxY3r33q6k1...?Fd9-=+`VLc"i&6{~YK0=9${` | `{"6{~YK0":"9${", "Fd9-":" `VLc\"i"}` | `{"Fd9-":[" `VLc\"i"], "6{~YK0":["9${"]}` |
| elixir-uri vs python-urllib3 | `://I:I...?[V17?e';j(_U=i9A&_=5#` | `{"[V17?e';j(_U":"i9A", "_":"5"}` | `{"[V17?e';j(_U":["i9A"], "_":["5"]}` |
| javascript-whatwg vs python-urllib3 | `sip:////:J142E@:...(3dǶ0?W!!=*:M2e4#7j` | `{"W!!":"*:M2e4"}` | `{"W!!":["*:M2e4"]}` |
| javascript-whatwg vs python-urllib3 | `ws://ws://40n93J2mrl:uL@...?IU',!0=B#8"` | `{"IU',!0":"B"}` | `{"IU',!0":["B"]}` |
| javascript-whatwg vs python-urllib3 | `ms-excel7:GS99h-C6:890
?8_7a=9&h^(^=+H.9#Z` | `{"8_7a":"9", "h^(^":" H.9"}` | `{"8_7a":["9"], "h^(^":[" H.9"]}` |
| javascript-whatwg vs python-urllib3 | `bolofilesystem.://?A.@:r⟐/1...m2&A.@:r⟐/1...m2#|` | `{"A.@:r⟐/1...@":"1/@;9t177S556<..m2"}` | `{"A.@:r⟐/1...@":["1/@;9t177S556<..m2", "1/@;9t177S556<..m2"]}` |
| python-urllib3 vs python-yarl | `?[(_5=2"7T95G&L:=i/*$1/` | `{"[(_5": ["2\"7T95G"], "L:": ["i/*$1/"]}` | `{"[(_5": "2\"7T95G", "L:": "i/*$1/"}` |
| python-urllib3 vs python-yarl | `?FR4'06iEj"7$|="U(=@R!55c_8t!/]59` | `{"FR4'06iEj\"7$|": ["\"U(=@R!55c_8t!/]59"]}` | `{"FR4'06iEj\"7$|": "\"U(=@R!55c_8t!/]59"}` |
| python-urllib3 vs python-yarl | `?9=4f@#V1f` | `{"9": ["4f@#V1f"]}` | `{"9": "4f@#V1f"}` |
| python-urllib3 vs python-yarl | `?W!!=*:M2e4` | `{"W!!": ["*:M2e4"]}` | `{"W!!": "*:M2e4"}` |
| python-urllib3 vs python-yarl | `?:/RÀ½=^@*u` | `{":/R\u00c0\u00bd": ["^@*u"]}` | `{":/R\u00c0\u00bd": "^@*u"}` |
| python-urllib3 vs python-yarl | `?=I"Or:1-`T08=[2!` | `{"":["I\"Or:1-`T08=[2!"]}` | `{"": "I\"Or:1-`T08=[2!"}` |
| python-httpx vs python-urllib3 | `?9=4f@#V1f` | `{"9": "4f@#V1f"}` | `{"9": ["4f@#V1f"]}` |
