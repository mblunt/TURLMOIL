# Key Ordering Difference

**Description:** Parsers return the same query keys and values but in a different order, reflecting differences in internal data structure ordering (insertion order vs. sorted, etc.).

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| python-urllib3 vs python-yarl | `https://ftp://X:X11D@Qz10.:?+1g2:=u7&,@zs/9N-+246%5C70&113&l=_&3~nE-5=2%220A` | `["113", " 1g2:", ",@zs/9N- 246\\70", "l", "3~nE-5"]` | `[" 1g2:", ",@zs/9N- 246\\70", "113", "l", "3~nE-5"]` |
| python-urllib3 vs python-yarl | `data://229:/...?76Tv=)E_54&2=_9` | `["76Tv", "2"]` | `["76Tv", "2"]` |
| js-whatwg vs python-yarl | `ms-project://..?795|Jk=o32E1(xJ5l&6=+4E]5` | `["795|Jk", "6"]` | `["795|Jk", "6"]` |
| js-whatwg vs python-yarl | `data://..?i􀭧9?4~w_=@!1y4,qb&5` | `["i\udbc2\udf679?4~w_", "5"]` | `["i\udbc2\udf679?4~w_", "5"]` |
| python-urllib3 vs python-yarl | `did://..?鰟Fp19v900RCXpq0𩯃3󯩲𨨨81_{...}\X;=Z&x1&=-=7h0&0` | `["0", "鰟Fp19v...", "x1", ""]` | `["鰟Fp19v...", "x1", "", "0"]` |
| rust-url vs python-urllib3 | `rediss://...?994)|...[0=\|&7(s\5*=0!!\^&` | `["7(s\\5*", "99...[0"]` | `["99...[0", "7(s\\5*"]` |
| rust-url vs python-urllib3 | `data://229:/...?76Tv=)E_54&2=_9` | `["2", "76Tv"]` | `["76Tv", "2"]` |
| rust-url vs python-urllib3 | `im://...?\u2a83\u00c0\u00ac=...&\u00c0\u00bd~;{2....=/4y5.L_1` | `["\u00c0\u00bd~...", "\u2a83\u00c0\u00ac"]` | `["\u2a83\u00c0\u00ac", "\u00c0\u00bd~..."]` |
| rust-url vs python-urllib3 | `h16...?C\u232bsb...=C],&A=Hk55&`53=.1C!\9-i}` | `["A", "C\u232b...", "`53"]` | `["C\u232b...", "A", "`53"]` |
| rust-url vs python-urllib3 | `ws://...?K<0K...8{:=')&,2+\"[AU=$"4Z@[[0B&{=C` | `[",2+\\\"[AU", "K<0K...{:", "{"]` | `["K<0K...{:", ",2+\\\"[AU", "{"]` |
| rust-url vs python-urllib3 | `wss://...?I,|T(=w"Q&6*=g` | `["6*", "I,|T("]` | `["I,|T(", "6*"]` |
| rust-url vs python-urllib3 | `ms-settings-bluetooth://...?I,|T(=w"Q&6*=g` | `["6*", "I,|T("]` | `["I,|T(", "6*"]` |
| go-net vs python-urllib3 | `https://W1263k499AmTFS982I5:b@.-.JB5-1i5461<∞a6󼠾?==[5y9)Ni(]1)0&qobS.}h+=eo7778@=''v&|~=I&^526R(077=7K&#.Tw5E` | `{"":["=[5y9)Ni(]1)0"], "^526R(077":["7K"], "qobS.}h ":["eo7778@=''v"], "|~":["I"]}` | `{"":["=[5y9)Ni(]1)0"], "qobS.}h ":["eo7778@=''v"], "|~":["I"], "^526R(077":["7K"]}` |
| go-net vs python-urllib3 | `ms-settings-cloudstorage{...?%svnms-enrollmentgeov-event://...?-l(8R2]F}\JS+5\}=7]0E^Db/L` | `{"-l(8R2]F}\\JS 5\\}":["7]0E^Db/L"], "1X/i7J!|v":["8p"]}` | `{"1X/i7J!|v":["8p"], "-l(8R2]F}\\JS 5\\}":["7]0E^Db/L"]}` |
| go-net vs python-urllib3 | `ms-settings-bluetooth://file://xY0Z98A:@9g7...?I,|T(=w"Q&6*=g#4|` | `{"6*":["g"], "I,|T(":["w\"Q"]}` | `{"I,|T(":["w\"Q"], "6*":["g"]}` |
| go-net vs python-urllib3 | `ws://mTVN8vT5B3C:dp@65B?{=V&'8=ip7/&6d'646]#|` | `{"'8":["ip7/"], "6d'646]":[""], "{":["V"]}` | `{"{":["V"], "'8":["ip7/"]}` |
| rust-url vs python-urllib3 | `data://229:...?76Tv=)E_54&2=_9#YNg` | `{"2":["_9"], "76Tv":[")E_54"]}` | `{"76Tv":[")E_54"], "2":["_9"]}` |
| rust-url vs python-urllib3 | `data://ftp://:11A@0.69.2.2:8...?0=]A01=j&0&#1'zP` | `{"0":["]A01=j", ""]}` | `{"0":["]A01=j"]}` |
| go-net vs python-urllib3 | `?($4PDY),Z=%6D2%33&%38&%3D=%7B%23pP%77` | `{"%38": [""], "%3D": ["%7B%23pP%77"], "($4PDY),Z": ["%6D2%33"]}` | `{"($4PDY),Z": ["%6D2%33"], "%3D": ["%7B%23pP%77"]}` |
| go-net vs python-urllib3 | `?==[5y9)Ni(]1)0&qobS.}h+=eo7778@=''v&|~=I&^526R(077=7K&` | `{"": ["=[5y9)Ni(]1)0"], "^526R(077": ["7K"], "qobS.}h ": ["eo7778@=''v"], "|~": ["I"]}` | `{"": ["=[5y9)Ni(]1)0"], "qobS.}h ": ["eo7778@=''v"], "|~": ["I"], "^526R(077": ["7K"]}` |
| go-net vs python-urllib3 | `?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A` | `{ " 1g2:": ["u7"], ",@zs/9N- 246\\70": [""], "113": [""], "3~nE-5": ["2\"0A"], "l": ["_"]}` | `{" 1g2:": ["u7"], "l": ["_"], "3~nE-5": ["2\"0A"]}` |
| rust-url vs elixir-uri | `?w=1&S"{443=79&L&`^'8` | `{"L": [""], "S\"{443": ["79"], "`^'8": [""], "w": ["1"]}` | `{"L": "", "S\"{443": "79", "`^'8": "", "w": "1"}` |
| rust-url vs elixir-uri | `?7(s\5*=0!!\^&99...644[0=\|` | `{"7(s\\5*": ["0!!\\^"], "99...": ["\\|"]}` | `{"7(s\\5*": "0!!\\^", "99...": "\\|"}` |
| python-furl vs python-urllib3 | `https://W1263k499AmTFS982I5...?==[5y9)...&qobS.}h+=eo7778@=''v&|~=I&^526R(077=7K&` | `{"qobS.}h ": ["eo7778@=''v"], "|~": ["I"], "^": ["526R(077"], "7K": [""]}` | `{"": ["=[5y9)Ni(]1)0"], "qobS.}h ": ["eo7778@=''v"], "|~": ["I"], "^526R(077": ["7K"]}` |
