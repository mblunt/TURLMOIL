# No-Value Key Dropped vs Kept

**Description:** When a query parameter has no `=` sign (e.g. `?foo&bar=1`), some parsers (e.g. PHP's parse_str) retain `foo` as a key with an empty string value, while others (e.g. Python's urllib3) silently drop the key entirely.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| php-parseurl vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I󺕂mZ0L4㛹@&V"PE7Xq=eUv{!c&0&3?w=1&S"{443=79&L&`^'8#𖆌` | `["w", "S\"{443", "L", "`^'8"]` | `["w", "S\"{443"]` |
| php-parseurl vs python-urllib3 | `nntpsK[?v[rmi://hr0:3i뵡:2m<Ɨ⋷(⫼H𽔈⣮z9K0(?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `["v_rmi://...", "m7", ";", "^", "5o]"]` | `["5o]"]` |
| php-parseurl vs python-urllib3 | `://X񜭠:R84J@.񷍰񦸥P|弄?D=s{@13-X&N&|-2PV{#5` | `["D", "N", "|-2PV{"]` | `["D"]` |
| php-parseurl vs python-urllib3 | `wtaiggTunrealdrmadiumxtra4xmlrpc.beep₧⪤ms-useractivityset1XdntpD󽦃hcpsmbfacetime://W6k9xc1Z1f:Qa@Ss.K7i68Srd.ee08-C-`0y&3` | `["$:Y", "3}!\"", "{8,S0", "ry_K2", "rM:_", "J6m", "4_xf52", "~A"]` | `["$:Y", "3}!\"", "{8,S0", "4 xf52", "~A"]` |
| php-parseurl vs python-urllib3 | `𢪮godlna-playsinglestunsdppl;sessionopaquelocktoken;3𧬯://L0'8M:5812342VO2@𨦮393☇
zE8:52O⊊'699r4I43B9\6051k9977?&-i|m-&15==` | `["-i|m-", "15"]` | `["15"]` |
| php-parseurl vs python-urllib3 | `file://https://gbc9r6p7h.29OisZ5eYa0-q2:7]
⤞B?_2~3-=+}|&!6ZC#h3dD` | `["_2~3-", "!6ZC"]` | `["_2~3-"]` |
| php-parseurl vs python-urllib3 | `劖R􃙂|	marketsmsnim://4z12332e8iv21M6ESrI:Sq447E@[Aa:Ce:d:b:E:1:B:F]:􊲛󷟑},6Ô𠠬{R91u&Ct7~?22=08_'p-yQ2TVi&7!|o&ZSE5&[@=^` | `["22", "7!|o", "ZSE5"]` | `["22", "[@"]` |
| php-parseurl vs python-urllib3 | `://m:81O6ugt3bgnxK65ej@nmX-Y1006.3kkT9173.:71536968⍯󲵊𛾽􅫂􈂌 󷲧8󴠝?r&[8-"$&󞧜ᙯ` | `["r", "\udb3a\udddc\u166f"]` | `[]` |
| js-whatwg vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I󺕂mZ0L4㛹@&V"PE7Xq=eUv{!c&0&3?w=1&S"{443=79&L&`^'8#𖆌` | `["w", "S\"{443", "L", "`^'8"]` | `["w", "S\"{443"]` |
| js-whatwg vs python-urllib3 | `wss://􌿩N4@37.7.59.40:/./138򀫸􍝧 񎢮
	󵳾𮫖;/%󾢷5󱠛	)?'^5ME`9H94:+O55Ek&9=95u7c&Sq#Hc` | `["9", "'^5ME`9H94:+O55Ek", "Sq"]` | `["9"]` |
| js-whatwg vs python-urllib3 | `ftp://http://X:X11D@Qz10.:3d5315Y1qH86(2dVSK96?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A#-28,9` | `["113", " 1g2:", ",@zs/9N- 246\\70", "l", "3~nE-5"]` | `[" 1g2:", "l", "3~nE-5"]` |

| rust-url vs python-urllib3 | `wss://..?w=1&S"{443=79&L&`^'8` | `["w", "S\"{443", "L", "`^'8"]` | `["w", "S\"{443"]` |
| python-furl vs python-urllib3 | `https://..?+1g2:=u7&,@zs/9N-+246%5C70&113&l=_&3~nE-5=2%220A` | `[" 1g2:", ",@zs/9N- 246\\70", "113", "3~nE-5", "l"]` | `[" 1g2:", "l", "3~nE-5"]` |
| rust-url vs python-urllib3 | `wss://..?'^5ME`9H94:+O55Ek&9=95u7c&Sq` | `["'^5ME`9H94: O55Ek", "9", "Sq"]` | `["9"]` |
| rust-url vs python-urllib3 | `ftp://...?V"00'=.N&7:` | `["7:", "V\"00'"]` | `["V\"00'"]` |
| rust-url vs python-urllib3 | `wss://..?PJ=0&*Q=t+oT8&&R4eV9F;v=&D1]^y+:'W='k'u!&` | `["PJ", "*Q", "R4eV9F;v", "D1]^y :'W"]` | `["PJ", "*Q", "D1]^y :'W"]` |
| rust-url vs python-urllib3 | `ftp://...?m0.`1\B=u2V&BH=T!M,&5:6D.4Av7A0B=;4&[=Q&t&1_d7T$07&KW,=3&/&` | `["m0.`1\\B", "BH", "5:6D.4Av7A0B", "[", "t", "1_d7T$07", "KW,", "/"]` | `["m0.`1\\B", "BH", "5:6D.4Av7A0B", "[", "KW,"]` |
| rust-url vs python-urllib3 | `wss://..?;9.914}@7Qy=)&;iR*X[k=!.*x7s8:2=&-&M4=B"]886[&=&;qL1&5wo`9@J=2&~MI,=$-&` | `[";9.914}@7Qy", ";iR*X[k", "-", "M4", "", ";qL1", "5wo`9@J", "~MI,"]` | `[";9.914}@7Qy", ";iR*X[k", "M4", "5wo`9@J", "~MI,"]` |
| perl-uri vs python-urllib3 | `file://TxY3r33q6k1...?Fd9-=+`VLc"i&6{~YK0=9${` | `{"6{~YK0":"9${", "Fd9-":" `VLc\"i"}` | `{"Fd9-":[" `VLc\"i"], "6{~YK0":["9${"]}` |
| perl-uri vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I...?w=1&S"{443=79&L&`^'8#` | `{"L":null, "S\"{443":"79", "`^'8":null, "w":"1"}` | `{"w":["1"], "S\"{443":["79"]}` |
| perl-uri vs python-urllib3 | `://X񜭠:R84J@....?D=s{@13-X&N&|-2PV{#5` | `{"D":"s{@13-X", "N":null, "|-2PV{":null}` | `{"D":["s{@13-X"]}` |
| perl-uri vs python-urllib3 | `acctreloadmagnetboloed2k...?4@*STt&a6=_74lpZ1[4m(6` | `{"4@*STt":null, "a6":"_74lpZ1[4m(6"}` | `{"a6":["_74lpZ1[4m(6"]}` |
| perl-uri vs python-urllib3 | `)://k⭕iD1...?Fi.5&.G2{84[=6260|4^` | `{".G2{84[":"6260|4^", "Fi.5":null}` | `{".G2{84[":["6260|4^"]}` |
| perl-uri vs python-urllib3 | `://r𪏻22=A㸅...?CS7-[8NzQ0=k닆􋒭` | `{"CS7-[8NzQ0":"k닆"}` | `{"CS7-[8NzQ0":["k닆"]}` |
| perl-uri vs python-urllib3 | `//...?u=*6&}a_t/9)#26v)2[` | `{"u":"*6", "}a_t/9)":null}` | `{"u":["*6"]}` |
| perl-uri vs python-urllib3 | `wss://...?'^5ME`9H94:+O55Ek&9=95u7c&Sq#Hc` | `{"'^5ME`9H94: O55Ek":null, "9":"95u7c", "Sq":null}` | `{"9":["95u7c"]}` |
| perl-uri vs python-urllib3 | `Á³mÁ³:/À¯...?7À¸[&v9Y!=@8#` | `{"7\u00c0\u00b8[":null, "v9Y!":"@8"}` | `{"v9Y!":["@8"]}` |
| perl-uri vs python-urllib3 | `ydictZiaxi...?{9$59$5=8i3&)x&+r4UnX9_&$@_󾤚4` | `{")x":null, "$@_...": null, " r4UnX9_":null, "{9$59$5":"8i3"}` | `{"{9$59$5":["8i3"]}` |
| elixir-uri vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I...?w=1&S"{443=79&L&`^'8#` | `{"L":"", "S\"{443":"79", "`^'8":"", "w":"1"}` | `{"w":["1"], "S\"{443":["79"]}` |
| elixir-uri vs python-urllib3 | `://X...?D=s{@13-X&N&|-2PV{#5` | `{"D":"s{@13-X", "N":"", "|-2PV{":""}` | `{"D":["s{@13-X"]}` |
| elixir-uri vs python-urllib3 | `)://k⭕iD1...?Fi.5&.G2{84[=6260|4^` | `{".G2{84[":"6260|4^", "Fi.5":""}` | `{".G2{84[":["6260|4^"]}` |
| elixir-uri vs python-urllib3 | `w%73://...?&Nq=Grs%39#` | `{"":""}, "Nq":"Grs9"}` | `{"Nq":["Grs9"]}` |
| javascript-whatwg vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I...?w=1&S"{443=79&L&`^'8#` | `{"w":"1", "S\"{443":"79", "L":"", "`^'8":""}` | `{"w":["1"], "S\"{443":["79"]}` |
| javascript-whatwg vs python-urllib3 | `ftp://oV9u31...?V"00'=.N&7:##g7W9dh+1` | `{"V\"00'":".N", "7:":""}` | `{"V\"00'":[".N"]}` |
| javascript-whatwg vs python-urllib3 | `data://?...?SF=4F&IOr$7Y8F#v01)` | `{"...?SF":"4F", "IOr$7Y8F":""}` | `{"...?SF":["4F"]}` |
| javascript-whatwg vs python-urllib3 | `wss://...?'^5ME`9H94:+O55Ek&9=95u7c&Sq#Hc` | `{"9":"95u7c", "'^5ME`9H94: O55Ek":"", "Sq":""}` | `{"9":["95u7c"]}` |
| rust-url vs python-urllib3 | `wss://y21zEU1@S-3n7-V6I...?w=1&S"{443=79&L&`^'8#` | `{"L":[""], "S\"{443":["79"], "`^'8":[""], "w":["1"]}` | `{"w":["1"], "S\"{443":["79"]}` |
| rust-url vs python-urllib3 | `wss://...?'^5ME`9H94:+O55Ek&9=95u7c&Sq#Hc` | `{"'^5ME`9H94: O55Ek":[""], "9":["95u7c"], "Sq":[""]}` | `{"9":["95u7c"]}` |
| rust-url vs python-urllib3 | `ftp://oV9u31...?V"00'=.N&7:##` | `{"7:":[""], "V\"00'":[".N"]}` | `{"V\"00'":[".N"]}` |
| rust-url vs python-urllib3 | `https://ftp://X...?+1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A` | `{",@zs/9N- 246\\70":[""], "113":[""], "3~nE-5":["2\"0A"], " 1g2:":["u7"], "l":["_"]}` | `{",@zs/9N- 246\\70":["..."]}` |
| rust-url vs python-urllib3 | `ws5E4EAvpfH:SZg@H78r...?1$P&pai5B3Ur58XEI?,0;8&[=~4!#g/.` | `{"1$P":[""], "[":["~4!"], "pai5B3Ur58XEI?,0;8":[""]}` | `{"[":["~4!"]}` |
| rust-url vs python-urllib3 | `ws://llsZe81f73Ex68IZPV1+a1>...?PJ=0&*Q=t+oT8&&R4eV9F;v=&D1]^y+:'W='k'u!&#E36in` | `{"*Q":["t oT8"], "D1]^y :'W":["'k'u!"], "PJ":["0"], "R4eV9F;v":[""]}` | `{"PJ":["0"], "*Q":["t oT8"], "D1]^y :'W":["'k'u!"]}` |
| python-urllib3 vs python-yarl | `? ,󺬛` | `{}` | `{", \udbaa\udf1b": ""}` |
| python-urllib3 vs python-yarl | `?W` | `{}` | `{"W\uda8e\udddc": ""}` |
| python-urllib3 vs python-yarl | `?2P7- 94\87=` | `{}` | `{"2P7- \f 94\\87": ""}` |
| python-urllib3 vs python-yarl | `?`=u;N6_(~*{3/` | `{}` | `{"`=u;N6_(~*{3/": ""}` |
| python-urllib3 vs python-yarl | `?W~\N{*,` | `{}` | `{"W~\\N{*,": ""}` |
| python-urllib3 vs python-yarl | `?.95p87%FE` | `{}` | `{".\u008895p87%FE": ""}` |
| python-urllib3 vs python-yarl | `?7X,1?` | `{}` | `{"7X,1?": ""}` |
| python-urllib3 vs python-yarl | `?5覶 Z` | `{}` | `{"\uf2165\u89b6 Z": ""}` |
