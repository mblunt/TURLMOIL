# Plus Sign Decoded as Space in Keys

**Description:** Some parsers decode '+' as a space character in query key names (application/x-www-form-urlencoded behavior), while others leave '+' as a literal plus sign.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib86 (python-urllib3) vs lib88 (python-furl) | `://F2tA0.../...?2P7-+%0C+94\87=#` | `{} (empty - key not parsed)` | `{"2P7- \f 94\\87": ""} (+ decoded as space)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `Sg(nipp...?...8P?+nQ`8...` | `{"..._8P?__nQ`8__e...": ""} (+ decoded as spaces)` | `null (key ignored)` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `ms-searchadiumxtr...?x^`N7~7G።0` | `{"x^`N7~7G።0": ""} (+ not decoded)` | `null` |
| lib71 (php-parseurl) vs lib72 (php-spatie) | `...://\G:h60D@...?_+򬜻###97@` | `{"__򬜻": ""} (+ decoded as space)` | `null` |
| python-urllib3 vs python-yarl | `hcpnmvn xmlrpc.beep...?N]b2*+0=y]v|&,D=(` | `["N]b2* 0", ",D"]` | `["N]b2* 0", ",D"]` |
| python-urllib3 vs python-yarl | `://353d3uH86..?2RQ19:]$=0&` +&d55*+c'qO9c-=1&Z=C5"v4E2^` | `["2RQ19:]$", "d55* c'qO9c-", "Z"]` | `["2RQ19:]$", "`+", "d55* c'qO9c-", "Z"]` |
| python-urllib3 vs python-yarl | `GS..tns://..?񹤔y+^4(!=79` | `["񹤔y ^4(!"]` | `["񹤔y ^4(!"]` |
| python-urllib3 vs python-yarl | `stun..?@9}=v9m6(!o_[53;U==\,&7&^(};dp5*563c3-`g=R&&EgJ=yk&!\2('&kcO~+~H7$={_j=Z+`9!9` | `["@9}", "^(};dp5*563c3-`g", "EgJ", "kcO~ ~H7$"]` | `["@9}", "7", "^(};dp5*563c3-`g", "", "EgJ", "!\\2('", "kcO~ ~H7$"]` |
| go-net vs python-urllib3 | `,tur%6EKa%61ak%65y%70%61%72%63p%61para%7Az%69k.../m%73-%77o%72%64...?&%60%37^2%2A+=;/%35&3%49=|%5B.2Q112...` | `{"`7^2* ":[";\/5"], "3I":["..."]}` | `{"`7^2*+":[";\/5"], "3I":["..."]}` |
| python-furl vs python-urllib3 | `?_+򬜻` | `{"_ \uda71\udf3b": null}` | `{}` |
| python-furl vs python-urllib3 | `?2R򕐃1a?+` | `{"2R\uda15\udc031a? ": null}` | `{}` |
| python-furl vs python-urllib3 | `?⧁ 󴕕+⡑c` | `{"⧁ 󴕕 ⡑c": null}` | `{}` |
| python-urllib3 vs python-furl | `?{G+473=UP~M&_]L10='140y4(0^\\O3*&25C7u` | `{"{G 473": ["UP~M"], "_]L10": ["'140y4(0^\\\\O3*"]}` | `{"{G 473": "UP~M", "_]L10": "'140y4(0^\\\\O3*", "25C7u": null}` |
| python-furl vs python-urllib3 | `?@[8C:fb:4:D:d3:de:Ef:16]1+Ǒ⏗354]3𫋨Z3}f⤢01Ⴇ?3⛭8`2I` | `{"@[8C:fb:4:D:d3:de:Ef:16]1 \u01d1\u23d7354]3\b\ud86c\udee8Z\u000b3}f\u292201\u10a7?3\u26ed8`2I": null}` | `{}` |
| python-furl vs python-urllib3 | `?:@L󲫆g:75󊪲ꁖ,i$fLn25MjLkL?+𴡬񊅨+H` | `{":@L\udb8a\udec6g:75\udaea\udeb2\ua056,i$fLn25MjLkL?\u0011 \ud892\udc6c\ud8e8\udd68 H": null}` | `{}` |
| python-urllib3 vs python-furl | `?5n*`+)6+8[+=W2&]0&k}6:!-]=--W/((^H@3|g},4@&2=MP55E,` | `{"5n*` )6 8[ ": ["W2"], "k}6:!-]": ["--W/((^H@3|g},4@"], "2": ["MP55E,"]}` | `{"5n*` )6 8[ ": "W2", "]0": null, "k}6:!-]": "--W/((^H@3|g},4@", "2": "MP55E,"}` |
| ruby-addressable vs python-urllib3 | `?...+TNb6SQ8g!5LS241=4I3J/3m` | `{"J}\\owser-extension...+TNb6SQ8g!5LS241": "4I3J/3m"}` | `{"J}\\owser-extension... TNb6SQ8g!5LS241": ["4I3J/3m"]}` |
| ruby-addressable vs python-urllib3 | `?yK2Ps1f8TC8XP:41...."+N=wT:` | `{"yK2Ps1f8TC8XP:41...\".+N": "wT:"}` | `{"yK2Ps1f8TC8XP:41...\". N": ["wT:"]}` |
| elixir-uri vs python-urllib3 | `?_+򬜻` | `{"_ \uda71\udf3b": ""}` | `{}` |
| elixir-uri vs python-urllib3 | `?'^5ME`9H94:+O55Ek&9=95u7c&Sq` | `{"'^5ME`9H94: O55Ek": "", "9": "95u7c", "Sq": ""}` | `{"9": ["95u7c"]}` |
| elixir-uri vs python-urllib3 | `?	8?9=7Dv3_bL+-&6=`=_A&t8\` | `{"	8?9": "7Dv3_bL -", "6": "`=_A", "t8\\": ""}` | `{"8?9": ["7Dv3_bL -"], "6": ["`=_A"]}` |
| ruby-addressable vs python-urllib3 | `?wsCQr3M4...\udb95\udfa9...+6-5\\` | `{";==7$": ...}` | `{";==7$": [...]}` |
| ruby-addressable vs perl-uri | `?Fd9-=+`VLc"i&6{~YK0=9${` | `{"Fd9-": "+`VLc\"i", "6{~YK0": "9${"}` | `{"6{~YK0": "9${", "Fd9-": " `VLc\"i"}` |
| ruby-addressable vs perl-uri | `?8_7a=9&h^(^=+H.9` | `{"8_7a": "9", "h^(^": "+H.9"}` | `{"8_7a": "9", "h^(^": " H.9"}` |
| ruby-addressable vs perl-uri | `?9"dG6z=~+w`0(*]g&...` | `{"9\"dG6z": "~ w`0(*]g", ...}` | `{"9\"dG6z": "~ w`0(*]g", ...}` |
| python-ada-url vs php-parseurl | `?'^5ME`9H94:+O55Ek&9=95u7c&Sq` | `{"'^5ME`9H94: O55Ek": [""], "9": ["95u7c"], "Sq": [""]}` | `{"'^5ME`9H94:_O55Ek": "", "9": "95u7c", "Sq": ""}` |
| python-furl vs python-urllib3 | `?+1g2:=u7 (plus sign prefix in key)` | `{" 1g2:": ["u7"]}` | `{" 1g2:": ["u7"]}` |
| python-ada-url vs php-parseurl | `wss://...?⧁ 󴕕+⡑c` | `{"⧁ 󴕕 ⡑c": [""]}` | `{"⧁_󴕕_⡑c": ""}` |
