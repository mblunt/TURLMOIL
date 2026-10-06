# Semicolon as Query Parameter Separator

**Description:** Some parsers (e.g. Perl's URI, older CGI libraries) treat semicolons (`;`) as alternative parameter separators equivalent to `&`, splitting the query string on `;` in addition to `&`, while others treat `;` as a literal character within a key or value.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| perl-uri vs python-urllib3 | `ft%2570://%2577...?5%2561;%2526=2jN3%252Bw%2536cn;6/%2526%2538%255B=qi898(f%255B23` | `["5%61", "%26", "6/%26%38%5B"]` | `["5%61;%26"]` |
| perl-uri vs python-urllib3 | `://I:I...?[V17?e';j(_U=i9A&_=5` | `["[V17?e'", "j(_U", "_"]` | `["[V17?e';j(_U", "_"]` |
| perl-uri vs python-urllib3 | `nntpsK[?v[rmi://...?v[rmi://...;%5E&&5o]=Y-H|9Q,B` | `["v[rmi://...", "", "^", "", "5o]", ...]` | `["5o]"]` |
| perl-uri vs python-urllib3 | `udp://...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&` | `["7K", "04k[C0", "tRHuA,8", "A_Q09,M78", "Il", ...]` | `["A_Q09,M78"]` |
| perl-uri vs python-urllib3 | `udp://...?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `["7K", "04k[C0", "tRHuA,8", "A_Q09,M78", "Il", "|[ @\"2:O~}e", "WTI^A264H"]` | `["A_Q09,M78"]` |
| perl-uri vs python-urllib3 | `da%74a://...?}7=]=22_A;9q45|^!&+~=54o1hJ7^{,_=9&7p6]m&"^58=04;-8fDv25&@cqNb=^` | `["}7", "9q45|^!", "+~", "\"^58", "04", "-8fDv25&@cqNb"]` | `["}7", "+~", "\"^58"]` |
| perl-mojo-url vs perl-uri | `://I:I...?[V17?e';j(_U=i9A&_=5` | `["[V17?e'", "j(_U", "_"]` | `["[V17?e';j(_U", "_"]` |
| python-yarl vs python-urllib3 | `nntpsK[?v[rmi://hr0:3i뵡:2m<Ɨ⋷(⫼H𽔈⣮z9K0(?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `["v[rmi://hr0:3i\f\ubd61:2m<\f...", "m7", ";", "^", "", "5o]"]` | `["5o]"]` |
| php-parseurl vs python-urllib3 | `nntpsK[?v[rmi://hr0:3i뵡:2m<Ɨ⋷(⫼H𽔈⣮z9K0(?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `["v_rmi://hr0:3i_\ubd61:2m_<_..._z9K0(?s_}", "m7", ";", "^", "5o]"]` | `["5o]"]` |
| perl-uri vs python-urllib3 | `://I:I񅵞➋y0@12.73.15.9:87z NP5Ἓ4V?[V17?e';j(_U=i9A&_=5#` | `{"[V17?e'": null, "_": "5", "j(_U": "i9A"}` | `{"[V17?e';j(_U": ["i9A"], "_": ["5"]}` |
| perl-uri vs python-urllib3 | `𨌧JTxmlrpc.beepudp://62Fmd5O6C5kj651k699:otq
􉙿4􈬻⋾H:91F5po2iyxt207L033`4?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WT` | `{"04k[C0": null, "7K": null, "A_Q09,M78": "pOn", "Il": null, "WTI^A264H": null, "tRHuA,8": null, "|[ @\"2:O~}e": null}` | `{"A_Q09,M78": ["pOn"]}` |
| perl-uri vs python-urllib3 | `ft%2570://%2577𨥗񶍋%2530⢲𶊦%253F,♈%2572UekRA%2535.61%252E%2530.11{?5%2561;%2526=2jN3%252Bw%2536cn;6/%2526%2538%255B=qi898(f` | `{"%26": "2jN3%2Bw%36cn", "5%61": null, "6/%26%38%5B": "qi898(f%5B23"}` | `{"5%61;%26": ["2jN3%2Bw%36cn;6/%26%38%5B=qi898(f%5B23"]}` |
| perl-uri vs python-urllib3 | `nntpsK[?v[rmi://hr0:3i뵡:2m
<Ɨ⋷(⫼H𽔈⣮z9K0(?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `{"" :[null,null,null], "5o]":"Y-H|9Q,B", "^":null, "m7":null, "v[rmi://hr0:3i...":null}` | `{"5o]":["Y-H|9Q,B"]}` |
| perl-uri vs python-urllib3 | `ms-infopath7psyc𴗜://2򦿯4/..$d᣸⨦@7Sy3.5ta-.t	􋆫񉡹PspA0}2cyK2Q19IDlw1?5;B9"{-0]s[&]x&[H=|#Y80` | `{"5": null, "B9\"{-0]s[": null, "[H": "|", "]x": null}` | `{"[H": ["|"]}` |
| perl-uri vs python-urllib3 | `coapcalltomsrpswssM𼵀://95639Yl:17B896.00.93.52:04V%KQPqD3B03TP|u65Z6:zIm0?/(\=(0[[;&/( \=(0[[;#?` | `{"" :null, "/(\\" :["(0[[","(0[["]}` | `{"/(\\":["(0[[;","(0[[;"]}` |
| perl-uri vs python-urllib3 | `<ymsgÁ²mailtÁ¯...?=@=VS_k!;PÀ±eU`&À¹4=r#㮝` | `{"" :"@=VS_k!", "P\u00c0\u00b1eU`":null, "\u00c0\u00b94":"r"}` | `{"":["@=VS_k!;P\u00c0\u00b1eU`"], "\u00c0\u00b94":["r"]}` |
| perl-uri vs python-urllib3 | `crid<barion᧫H...?𤑇𐑠26𦆁5Iu3峀*0*2􊡇:@Y-1W．-3UNkW-40hsr6882576᪡X⌐B:󺲑	?PEp(8@=&i[6;['-[+6~7=&IPo=78d19#Q0` | `{"IPo":"78d19", "['-[ 6~7":"", "i[6":null, "...?PEp(8@":""}` | `{"IPo":["78d19"]}` |
| python-urllib3 vs python-yarl | `nntpsK[?v[rmi://hr0:3i뵡:2m<Ɨ⋷(⫼H?s_}&m7&;&^&&5o]=Y-H|9Q,B` | `{"5o]": ["Y-H|9Q,B"]}` | `{"v[rmi://hr0:3i\f\ubd61:2m<\f\u0197\u22f7(\u2afcH\ud8b5\udd08\u28ee\fz9K0(?s_}": "", "m7": "", ";": "", "^": "", "": "", "5o]": "Y-H|9Q,B"}` |
| python-furl vs python-urllib3 | `?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"tRHuA,8": null, "A_Q09,M78": "pOn", "7K;04k[C0": null, "Il": null, "|[ @\"2:O~}e;WTI^A264H": null}` | `{"A_Q09,M78": ["pOn"]}` |
| python-furl vs python-urllib3 | `nntpsK[?v[rmi://...&m7&;&^&&5o]=Y-H|9Q,B` | `{"v[rmi://...]: null, "m7": null, ";": null, "^": null, "": null, "5o]": "Y-H|9Q,B"}` | `{"5o]": ["Y-H|9Q,B"]}` |
| python-furl vs python-urllib3 | `?9N=*")&40_[*"T$s=g&_}B{3^n&]+=-&)6` | `{"9N": "*\")", "40_[*\"T$s": "g", "_}B{3^n": null, "] ": "-", ")6": null}` | `{"9N": ["*\")"], "40_[*\"T$s": ["g"], "] ": ["-"]}` |
| python-furl vs python-urllib3 | `?@9}=v9m6(!o_[53;U==\,&7&^(};dp5*563c3-`g=R&&EgJ=yk&!\2('&kcO~+~H7$={_j=Z+`9!9` | `{"@9}": "v9m6(!o_[53;U==\\,", "7": null, "^(};dp5*563c3-`g": "R", "": null, "EgJ": "yk", "!\\2('": null, "kcO~ ~H7$": "{_j=Z `9!9"}` | `{"@9}": ["v9m6(!o_[53;U==\\,"], "^(};dp5*563c3-`g": ["R"], "EgJ": ["yk"], "kcO~ ~H7$": ["{_j=Z `9!9"]}` |
| perl-uri vs python-urllib3 | `?[V17?e';j(_U=i9A&_=5` | `{"[V17?e'": null, "_": "5", "j(_U": "i9A"}` | `{"[V17?e';j(_U": ["i9A"], "_": ["5"]}` |
| perl-uri vs python-urllib3 | `?tRHuA,8&A_Q09,M78=pOn&7K;04k[C0&Il&|[+@"2:O~}e;WTI^A264H` | `{"04k[C0": null, "7K": null, "A_Q09,M78": "pOn", "Il": null, "WTI^A264H": null, "tRHuA,8": null, "|[ @\"2:O~}e": null}` | `{"A_Q09,M78": ["pOn"]}` |
| perl-uri vs python-urllib3 | `?5%61;%26=2jN3%2Bw%36cn;6/%26%38%5B=qi898(f%5B23` | `{"%26": "2jN3%2Bw%36cn", "5%61": null, "6/%26%38%5B": "qi898(f%5B23"}` | `{"5%61;%26": ["2jN3%2Bw%36cn;6/%26%38%5B=qi898(f%5B23"]}` |
| perl-uri vs python-urllib3 | `?v[rmi://...&m7&;&^&&5o]=Y-H|9Q,B` | `{"": [null, null, null], "5o]": "Y-H|9Q,B", "^": null, "m7": null, "v[rmi://...z9K0(?s_}": null}` | `{"5o]": ["Y-H|9Q,B"]}` |
| perl-uri vs python-urllib3 | `?ZJ*]1$%38"%34=S%77_%6F0%65%26&%282_=59;;%40...` | `{"": null, "%282_": "59", "%40 ...": null, "ZJ*]1$%38\"%34": "S%77_%6F0%65%26"}` | `{"ZJ*]1$%38\"%34": ["S%77_%6F0%65%26"], "%282_": ["59;;%40..."]}` |
| perl-uri vs python-urllib3 | `?5;B9"{-0]s[&]x&[H=|` | `{"5": null, "B9\"{-0]s[": null, "[H": "|"}` | `{"[H": ["|"]}` |
| perl-uri vs python-urllib3 | `?=@=VS_k!;PÀ±eU`&À¹4=r` | `{"": "@=VS_k!", "PÀ±eU`": null, "À¹4": "r"}` | `{"": ["@=VS_k!;PÀ±eU`"], "À¹4": ["r"]}` |
| perl-uri vs python-urllib3 | `?\y&U=!ti2YO`{;=I&;M6w,0)b@=G1V'1&"vq=711`d10:&2@:/P4!N91e_'=,,48` | `{"U": "!ti2YO`{", "": ["I", null], "M6w,0)b@": "G1V'1", "\"vq": "711`d10:", "2@:/P4!N91e_'": ",,48", "\\y": null}` | `{"U": ["!ti2YO`{;=I"], ";M6w,0)b@": ["G1V'1"], "\"vq": ["711`d10:"], "2@:/P4!N91e_'": [",,48"]}` |
