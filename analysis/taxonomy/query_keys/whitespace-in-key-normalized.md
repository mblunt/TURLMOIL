# Whitespace/Control Characters in Keys Normalized

**Description:** Some parsers (notably PHP's parse_str) replace whitespace and control characters (tabs, newlines, carriage returns) in key names with underscores, while others preserve the literal characters.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib71 (php-parseurl) vs lib73 (php-laminas) | `://F2tA0.../...?2P7-\n\n94\87=#` | `{"2P7-____94\\87": ""} (tabs/newlines \u000c\r → underscores)` | `{"2P7-\f\r_94\\87": ""} (control chars preserved literal)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `=wtaiz39.50sabout...?...⎩⍊\t#` | `{"key_": ""} (tab→underscore)` | `{"key\t": ""} (tab preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `...ms-whiteboard...?Z4;9r...E.;⧪X&Z4;9r...E.;⧪X` | `{"Z4;9r...E_;_X": ""} (\f→underscore)` | `{"Z4;9r...E_\fX": ""} (\f preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `http:/6s70j7/...?"2/\t...` | `{"\"2/_..._": ""} (tabs→underscores, trailing newline→underscore)` | `{"\"2/\t...\n": ""} (tab and newline kept)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `//ms-helpmsrp0pres://...?䅘\;⎸⬼\n˲\n8...?` | `{"key_˲_8...": ""} (\r\n→underscores)` | `{"key\r˲\n8...": ""} (CR and newline preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `appdata://...?\\⠪\n*5#` | `{"\\Àª_*_5": ""} (newline→underscore)` | `{"\\Àª\n*\f5": ""} (newline and \f preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `...?...95\t...\r...` | `key with tabs/CRs replaced by underscores` | `key with literal \t and \r` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `...?...K\nⓣ#...?...\f...Y` | `{"..._Y": ""} (\x02→underscore)` | `{".....\x02Y": ""} (control char preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `v...ms-settings-wifi://...?\r9...ℙD\r#ll9` | `{"_9...ℙD_": ""} (CRs→underscores)` | `{"\r9...ℙD\r": ""} (CRs preserved)` |
| lib71 (php-parseurl) vs lib73 (php-laminas) | `<ᶹ://W...?..._\u000b...` | `{"_...": ""} (\u000b→underscore)` | `{"\u000b...": ""} (control char preserved)` |
| js-whatwg vs php-parseurl | `http:/6s70j7/,z8494wU-􍃻<~3Pm70B2r^488B?"2/	솀5򘵽𫅴퀏
` | `["\"2/\t솀..."]` | `["\"2/_솀..._"]` |
| js-whatwg vs php-parseurl | `ftp://file://:𦛮@4Xoi
j@695"D&96.1.5.64:2201򀍷/}lKeL+52G2bQ43k6M46U?󶊾𭜀𣶠z󼪟
 ❓- l򇉡𢗬` | `["󶊾... ❓- l..."]` | `["󶊾...____❓-_l..."]` |
| php-parseurl vs python-yarl | `//x⍂://&0:95@:904779450
A&|2PLy-oi,iw6j2449M5d?
 ,󺜛#
` | `["__,󺜛"]` | `[" ,󺜛"]` |
| php-parseurl vs python-yarl | `ftp://file://:𦛮@4Xoi
j@695"D&96.1.5.64:2201򀍷/}lKeL+52G2bQ43k6M46U?󶊾𭜀𣶠z󼪟
 ❓- l򇉡𢗬` | `["󶊾...____❓-_l..."]` | `["󶊾... ❓- l..."]` |
| php-parseurl vs python-yarl | `Sg(nippsnihsubmitCdpp...dntpvrm...?...-9E6do-3558Lw064-51&&s	761...@5oogo5V'8P? nQ`8eᅃ...` | `["󯷔-9E6do-3558Lw064-51", "__", "s_761..."]` | `["󯷔-9E6do-3558Lw064-51", "\u000b\u001f", "s761..."]` |
| php-parseurl vs python-yarl | `//x⍂://&0:95@:?\n ,󺜛` | `["__,󺜛"]` | `[" ,󺜛"]` |
| php-parseurl vs python-yarl | `://F2tA0?2P7- \n\t 94\87=` | `["2P7-____94\\87"]` | `["2P7- \f 94\\87"]` |
| php-parseurl vs python-yarl | `ftp://file://?\udb98\udebe...\u001c\u0017 \u2753- l\ud9dc\ude61...` | `["\udb98\udebe...____\u2753-_l..."]` | `["\udb98\udebe...\u001c\u0017 \u2753- l..."]` |
| php-parseurl vs python-yarl | `://030v3Q/../?5覶 Z` | `["覶_Z"]` | `["覶 Z"]` |
| php-parseurl vs python-yarl | `v ms-settings-wifi://...?\n9񄗠㫑ℙD\n` | `["_9񄗠㫑ℙD_"]` | `["9񄗠㫑ℙD"]` |
| php-parseurl vs python-urllib3 | `? ,󺬛` | `{"__,\udbaa\udf1b": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?2P7-  94\87=` | `{"2P7-____94\\87": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?䅘\;⎸⬼˲ 8⩾...X74.26.5.62:s2?` | `{"䅘\\;⎸⬼_˲_8⩾...X74_26_5_62:s2?": ""}` | `{}` |
| php-parseurl vs python-furl | `?􂋼8⎩⍊	` | `{"􂋼8⎩⍊_": ""}` | `{"􂋼8⎩⍊	": null}` |
| php-parseurl vs python-urllib3 | `?2R򕐃1a? ` | `{"2R\uda15\udc031a?_": ""}` | `{}` |
| php-parseurl vs python-urllib3 | `?"2/솀5򘵽𫅴퀏	` | `{"\"2/_\uc1805\uda23\udd7d\ud86c\udd74\ud00f_": ""}` | `{}` |
| perl-uri vs php-parseurl | `?2P7-  94\87=` | `{"2P7- \f\r 94\\87": ""}` | `{"2P7-____94\\87": ""}` |
| perl-uri vs php-parseurl | `?򮊑JH26@EQA-HJ6tVy:92...95	t`)9...` | `{"...95	t`)9...": ""}` | `{"...95_t`_)9...": ""}` |
| perl-uri vs php-parseurl | `?"2/	솀5...` | `{"\"2/	\uc1805...": ""}` | `{"\"2/_\uc1805..._": ""}` |
| rust-url vs php-parseurl | `?󶊾𭜀... ❓- l...` | `{"󶊾... ❓- l...": [""]}` | `{"󶊾...____❓-_l...": ""}` |
| rust-url vs php-parseurl | `?994)|�...644[0=\|&7(s\5*=0!!\^` | `{"994)|�...644[0": ["\\|"], "7(s\\5*": ["0!!\\^"]}` | `{"99___4)|�...644_0": "\\|", "7(s\\5*": "0!!\\^"}` |
| rust-url vs php-parseurl | `?	B𫋯
6` | `{"B𫋯6": [""]}` | `{"_B𫋯_6": ""}` |
| go-net vs php-parseurl | `?⧁ 󴕕 ⡑c` | `{"⧁ 󴕕 ⡑c": [""]}` | `{"⧁_󴕕_⡑c": ""}` |
| go-net vs php-parseurl | `?"*[@\! +&P~u@` | `{"\"*[@\\! ": [""], "P~u@": [""]}` | `{"\"*_@\\!_": "", "P~u@": ""}` |
| go-net vs php-parseurl | `? 1g2:=u7&,@zs/9N-+246\70&113&l=_&3~nE-5=2"0A` | `{" 1g2:": ["u7"], ",@zs/9N- 246\\70": [""], "113": [""], "l": ["_"], "3~nE-5": ["2\"0A"]}` | `{"1g2:": "u7", ",@zs/9N-_246\\70": "", "113": "", "l": "_", "3~nE-5": "2\"0A"}` |
| go-net vs php-parseurl | `?+).=&q2J"0&5)u` | `{ ")." : [""], "5)u": [""], "q2J\"0": [""]}` | `{")_": "", "q2J\"0": "", "5)u": ""}` |
| nodejs-url vs php-parseurl | `?2P7-  94\87=` | `{"2P7- \f\r 94\\87": ""}` | `{"2P7-____94\\87": ""}` |
| nodejs-url vs php-parseurl | `?yK2Ps1f8TC8XP:41񛲌G--5-1.7331-wg4.` | `{"yK2Ps1f8TC8XP:41񛲌G--5-1.7331-wg4.": ""}` | `{"yK2Ps1f8TC8XP:41񛲌G--5-1_7331-wg4_": ""}` |
| nodejs-url vs php-parseurl | `?"*[@\! +&P~u@` | `{"\"*[@\\! ": [null]}` | `{"\"*_@\\!_": ""}` |
| nodejs-url vs php-parseurl | `?v[rmi://hr0:3i뵡:2m...` | `{"v[rmi://hr0:3i\f\ubd61:2m": [null]}` | `{"v_rmi://hr0:3i_\ubd61:2m_<_...": ""}` |
| python-ada-url vs php-parseurl | `?'^5ME`9H94:+O55Ek&9=95u7c&Sq (with + decoded as space)` | `{"'^5ME`9H94: O55Ek": [""], "9": ["95u7c"], "Sq": [""]}` | `{"'^5ME`9H94:_O55Ek": "", "9": "95u7c", "Sq": ""}` |
| python-ada-url vs php-parseurl | `?^I[񿜑92^...` | `{"^I[񿜑92^ᵒD鶙": [""]}` | `{"^I__񿜑92^ᵒD鶙": ""}` |
| python-ada-url vs php-parseurl | `?􇣃l񪙻𩜞sh􏌄Z-2|'` | `{"􇣃l񪙻𩜞sh􏌄Z-2|'": [""]}` | `{"_􇣃l񪙻_𩜞sh􏌄Z-2|'": ""}` |
| python-ada-url vs php-parseurl | `?"2/	솀5...` | `{"\"2/솀5...": [""]}` | `{"\"2/_솀5..._": ""}` |
