# Null vs Empty Query Object

**Description:** One parser returns null (no query) while another returns an empty object/dict {} when the URL has no query string or only a fragment delimiter.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib1 (whatwg) vs lib2 (legacy) | `ms-getoffice://https://:X@!;:9-4=796Fy5Q"R1494!TZN?#7` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `adiumxtra77BO8lr:E0Q7195CA@M0p26'#?]}16` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://mi8rA01:9pA4@53.65.2.53297&7WQ24fN853d9r24jP35?#...` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `http://ftp://I6:1sx1[98:Dd:aa:bE:F2:f:29:D3]:80#T` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://http://:h48...&4)W|)h=3Ov;/VI,Nhpd26;&&:{,5#jVG/y` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `dis://xF69ht969LgTO1xgLAf:7@gN...` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `file:////7...~@=hxOl_22q1#?1` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://Қ2...#P88` | `{} (empty object)` | `null` |
| lib1 (whatwg) vs lib2 (legacy) | `http://http://D...?#29:^/b` | `{} (empty object)` | `null` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `%53fe%65%64...?=I"%4Fr:1-%60T08%3D%5B2%21#...` | `[] (empty array)` | `null` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `wÁ³://E5bh56sc...?KÀ½4h3` | `{"K\u00c0\u00bd4h3": ""}` | `null` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `://F2tA0Ἓ/...?2P7-\n\n94\87=#` | `{"2P7-    94\\87": ""}` | `null` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `://S126l3BF4L2S620NgBxnp1552@7...?T#39` | `{"T": ""}` | `null` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `%42%51%6Ds%72p://...?`%3Du;N%36%5F(~*{3/` | `{} (empty dict)` | `{"`=u;N6_(~*{3/": null}` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `//x⍂://&0:95@:904779450...?\n ,󸬛#\n` | `{} (empty dict)` | `{" ,\udba2\udf1b": ""} (key with value)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `OUtelnetiris...?W~\N{*,#71RL` | `{} (empty dict)` | `{"W~\\N{*,": ""}` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `=wtaiz39.50sabout...?...⎩⍊\t#15)57x7` | `{} (empty dict)` | `{"􂋼8⎩⍊": ""}` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `~moziconelsimvnskype://...?7X,1?#􉼌\t` | `{} (empty dict)` | `{"7X,1?": ""}` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `://...?\udbe0\udc5c\ud8ca\udf21*7#4` | `{} (empty dict)` | `{"\udbe0\udc5c\ud8ca\udf21*7": ""}` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `wÁ³://E5bh56sc...?KÀ½4h3` | `{} (empty dict)` | `{"K\u00c0\u00bd4h3": ""}` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `file://https://...?...򳄑61s` | `{} (empty dict)` | `{"򳄑61s": ""}` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `ws://ftp://...?"*[@\! +&P~u@#X0]` | `{} (empty dict)` | `{"\"*[@\\! ": "", "P~u@": ""}` |
| csharp-systemuri vs python-urllib3 | `adiumxtra77BO8lr:E0Q7195CA@M0p26'...?]}` | `{}` | `null` |
| csharp-systemuri vs python-urllib3 | `dis://xF69ht969LgTO1xgLAf:7@gN...#
⧼)...` | `{}` | `null` |
| csharp-systemuri vs python-urllib3 | `ms-getoffice://https://:X@!...?#7|?` | `{}` | `null` |
| csharp-systemuri vs python-urllib3 | `https://kn5189Q03F2o:W...?))1{_(`=&{)~T5B\1d}f` | `{"))1{_(`": [""]}` | `{}` |
| csharp-systemuri vs python-urllib3 | `ftp://oV9u31/?V"00'=.N&7:` | `{}` | `{"V\"00'": [".N"]}` |
| nodejs-url vs perl-uri | `://F2tA0Ἓ/...?2P7- 94\87=` | `null` | `{"2P7-____94\\87": ""}` |
| nodejs-url vs perl-uri | `#?...z4;9r(;HU...&Z4;9r...` | `null` | `{"Z4;9r(;HU36148E.;\u29ea_X": ""}` |
| nodejs-url vs php-parseurl | `://S126l3BF4L2S620NgBxnp1552@7.xn---...?T#39` | `null` | `{"T": ""}` |
| nodejs-url vs php-parseurl | `://櫰󙨱...?A=(9&$!OR{=V9t]V\4}` | `null` | `{"A": "(9", "$!OR{": "V9t]V\\4}"}` |
| python-furl vs python-urllib3 | `ftp://http://:h48...?...&4)W|)h=3Ov...` | `{}` | `null` |
| python-furl vs python-urllib3 | `ws://3Z53>a...?_󟀦Vj` | `{}` | `null` |
| python-furl vs python-urllib3 | `#?...?⍸;Ỏ#DCl` | `{}` | `null` |
| python-furl vs python-urllib3 | `ftp://mi8rA01:9pA4@...?#󼭉...` | `{}` | `null` |
