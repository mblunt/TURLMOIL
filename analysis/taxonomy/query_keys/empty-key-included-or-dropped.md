# Empty Key Included or Dropped

**Description:** When a query string contains a delimiter that produces an empty key name (e.g. `?&foo=1`, `?foo&&bar=1`, or `?=val`), some parsers include the empty string `""` as a key while others silently drop it.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs python-urllib3 | `w%73://O0%6An%76...?&Nq=Grs%39` | `["", "Nq"]` | `["Nq"]` |
| elixir-uri vs python-urllib3 | `w%73://O0%6An%76...?&Nq=Grs%39` | `["", "Nq"]` | `["Nq"]` |
| javascript-whatwg vs python-urllib3 | `redisspkcs11...?o&=|)p,&o` | `["", "o"]` | `[""]` |
| wss://...?;9.914}@7Qy=)&;iR*X[k=!...&-&M4=B...]886[&=&;qL1... | `wss://...?...&-&M4=B...]886[&=&;qL1...` | `["-", "M4", "", ";qL1", ...]` | `["M4", ";qL1", ...]` |
| rust-url vs python-urllib3 | `wss://...?...&&R4eV9F;v=&...` | `["R4eV9F;v", ...]` | `[...]` |
| javascript-whatwg vs python-urllib3 | `ftp://oV9u31/../...?V"00'=.N&7:##g7W9dh+1` | `["V\"00'", "7:"]` | `["V\"00'"]` |
| php-spatie vs python-urllib3 | `wss://...?...&=&;qL1...` | `["...", "", "..."]` | `["..."]` |
| rust-url vs python-urllib3 | `data://ftp://:11A@0.69.2.2:8...?0=]A01=j&0&` | `["0"]` | `["0"]` |
| perl-uri vs python-urllib3 | `w%73://O0%6An%76278Ku%369i3%7A76%352t%40𥪰%6C%0A:%3229%79%3Fᕱ%6F,192%42%34R6A378;e%5DXMo%5B6?&Nq=Grs%39#搜ཡ烜%0D𠪳%0B` | `{"":null, "Nq":"Grs9"}` | `{"Nq":["Grs9"]}` |
| perl-uri vs python-urllib3 | `𞲀ms-godlna-playsinglestun...?&-i|m-&15==#S7+JA7P` | `{"":null, "-i|m-":null, "15":"="}` | `{"15":["="]}` |
| perl-uri vs python-urllib3 | `nntpsK[?v[rmi://hr0:3i뵡:2m...?v[rmi://hr0:3i...z9K0(?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `{"":[null,null,null], "5o]":"Y-H|9Q,B", "^":null, "m7":null}` | `{"5o]":["Y-H|9Q,B"]}` |
| perl-uri vs python-urllib3 | `Dۖ򡃓newsiconmsrps...?=u#|` | `{"":"u"}` | `{"":["u"]}` |
| go-net vs python-urllib3 | `https://ftp://X:X11D@Qz10.:3d5315Y1qH86(2dVSK96?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A#-28,9|` | `{",@zs/9N- 246\\70":[""], "113":[""], "3~nE-5":["2\"0A"], " 1g2:":["u7"], "l":["_"]}` | `{",@zs/9N- 246\\70":["..."]}` |
| go-net vs python-urllib3 | `𤔉⒈af%2573ocf%2573...?($4PDY),Z=%256D2%2533&%2538&%253D=%257B%2523pP%2577` | `{"%38":[""], "%3D":["%7B%23pP%77"], "($4PDY),Z":["%6D2%33"]}` | `{"($4PDY),Z":["%6D2%33"], "%3D":["%7B%23pP%77"]}` |
| go-net vs python-urllib3 | `data://92Ul1857:8C@:/...?JV=13B&1KD76_6!d(39,&N=A&m|nb/7.G6u=}#t0v847]` | `{"1KD76_6!d(39,":[""], "JV":["13B"], "N":["A"], "m|nb/7.G6u":["}"]}` | `{"JV":["13B"], "N":["A"], "m|nb/7.G6u":["}"]}` |
| go-net vs python-urllib3 | `//&8z39.50rstream+...?8V7=`s&==Lh^Z78` | `{"":["=Lh^Z78"], "8V7":["`s"]}` | `{"8V7":["`s"], "":["=Lh^Z78"]}` |
| python-urllib3 vs python-yarl | `w%73://O0%6An%76278?&Nq=Grs9` | `{"Nq": ["Grs9"]}` | `{"": "", "Nq": "Grs9"}` |
| python-httpx vs python-urllib3 | `?'W0^'\28'.5a~dD31=w41_n8&0` | `{"'W0^'\\28'.5a~dD31": "w41_n8", "0": ""}` | `{"'W0^'\\28'.5a~dD31": ["w41_n8"]}` |
| python-httpx vs python-urllib3 | `?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A` | `{"+1g2:": "u7", ",@zs/9N-+246\\70": "", "113": "", "l": "_", "3~nE-5": "2\"0A"}` | `{"+1g2:": ["u7"], "l": ["_"], "3~nE-5": ["2\"0A"]}` |
| php-parseurl vs python-urllib3 | `?=I"%4Fr:1-%60T08%3D%5B2%21` | `[]` | `{"":["I\"Or:1-`T08=[2!"]}` |
| php-parseurl vs python-urllib3 | `?w=1&S"{443=79&L&`^'8` | `{"w": "1", "S\"{443": "79", "L": "", "`^'8": ""}` | `{"w": ["1"], "S\"{443": ["79"]}` |
| php-parseurl vs python-urllib3 | `?&Nq=Grs9` | `{"Nq": "Grs9"}` | `{"Nq": ["Grs9"]}` |
| csharp-systemuri vs python-urllib3 | `?;9.914}@7Qy=)&;iR*X[k=!.*x7s8:2=&-&M4=B"]886[&=&;qL1&5wo`9@J=2&~MI,=$-&I+1:4` | `{";9.914}@7Qy": [")"], ";iR*X[k": ["!.*x7s8:2="], "M4": ["B\"]886["], "": [""], "5wo`9@J": ["2"], "~MI,": ["$-"]}` | `{";9.914}@7Qy": [")"], ";iR*X[k": ["!.*x7s8:2="], "M4": ["B\"]886["], "5wo`9@J": ["2"], "~MI,": ["$-"]}` |
| csharp-systemuri vs python-urllib3 | `?PJ=0&*Q=t+oT8&&R4eV9F;v=&D1]^y+:'W='k'u!&` | `{"PJ": ["0"], "*Q": ["t oT8"], "R4eV9F;v": [""], "D1]^y :'W": ["'k'u!"]}` | `{"PJ": ["0"], "*Q": ["t oT8"], "D1]^y :'W": ["'k'u!"]}` |
| ruby-uri vs python-urllib3 | `?9Pq6&&{|1hj` | `{"9Pq6": "", "": "", "{|1hj": ""}` | `{}` |
| ruby-uri vs python-urllib3 | `?.m2~;=&D'1#6vr3` | `{"": "", ".m2~": null, "D'1#6vr3": null}` | `{}` |
| csharp-systemuri vs python-urllib3 | `?~.850=H&.&!h_IB,]5{=@&N2472:4II=_1&D=-d'i8`0C3~S^` | `{}` | `{"~.850": ["H"], "!h_IB,]5{": ["@"], "N2472:4II": ["_1"], "D": ["-d'i8`0C3~S^"]}` |
| csharp-systemuri vs python-urllib3 | `?))1{_(`=&{)~T5B\1d}f` | `{"))1{_(`": [""]}` | `{}` |
| go-net vs php-parseurl | `?;9.914}@7Qy=)&;iR*X[k=!.*x7s8:2=&-&M4=B"]886[&=&;qL1&5wo`9@J=2&~MI,=$-` | `{";9.914}@7Qy": [")"], ";iR*X[k": ["!.*x7s8:2="], "M4": ["B\"\]886["], "": [""], "5wo`9@J": ["2"], "~MI,": ["$-"]}` | `{";9.914}@7Qy": [")"], ";iR*X[k": ["!.*x7s8:2="], "M4": ["B\"\]886["], "5wo`9@J": ["2"], "~MI,": ["$-"]}` |
| go-net vs php-parseurl | `?MIሩ^6*jj47t.B=&n($|=kQ` | `{"MI\u1229^6*jj47t.B": [""], "n($|": ["kQ"]}` | `{"n($|": ["kQ"]}` |
| python-ada-url vs python-urllib3 | `?'^5ME`9H94:+O55Ek&9=95u7c&Sq` | `{"'^5ME`9H94: O55Ek": [""], "9": ["95u7c"], "Sq": [""]}` | `{"'^5ME`9H94: O55Ek": null, "9": "95u7c", "Sq": null}` |
| rust-url vs python-urllib3 | `?1Zx7o,z~27!(*g&` | `{"1Zx7o,z~27!(*g": [""]}` | `{}` |
| rust-url vs python-urllib3 | `?V"00'=.N&7:` | `{"V\"00'": [".N"], "7:": [""]}` | `{"V\"00'": [".N"]}` |
| rust-url vs python-urllib3 | `?W!!=*:M2e4` | `{"W!!": ["*:M2e4"]}` | `{"W!!": "*:M2e4"}` |
| python-ada-url vs python-urllib3 | `?wss://…?'^5ME`9H94:+O55Ek&9=95u7c&Sq` | `{"'^5ME`9H94: O55Ek": [""], "9": ["95u7c"], "Sq": [""]}` | `{"9": ["95u7c"]}` |
| python-furl vs python-urllib3 | `dateuUkt?75(&a://oC7g49QR@...+...` | `{"75(": [""], "a://oC7g49QR@...: ...": [""]}` | `{}` |
| python-furl vs python-urllib3 | `ws://ftp://...?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A` | `{"+1g2:": ["u7"], "l": ["_"], "3~nE-5": ["2\"0A"], ...}` | `{"+1g2:": ["u7"], "l": ["_"], "3~nE-5": ["2\"0A"]}` |
| python-furl vs python-urllib3 | `wss://...?⧁ 󴕕 ⡑c` | `{"⧁ 󴕕 ⡑c": [""]}` | `{}` |
| python-furl vs python-urllib3 | `file://...?蝭`c25࠾` | `{"蝭`c25࠾": [""]}` | `{}` |
