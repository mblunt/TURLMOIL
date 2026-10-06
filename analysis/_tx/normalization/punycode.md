# Punycode / IDN Encoding

**Description:** One parser converts internationalized domain names to ACE/punycode (xn--) form while the other returns the Unicode or percent-encoded form.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `telnet://Z4ᾜ4E/../6111D44@00𨣬?#` | `Z4%E1%BE%9C4E` | `xn--z44e-6md7223b` |
| whatwg vs legacy | `unreal://B𪂞gb3gtlD33/...9p1251@8L6..q-.:092?#` | `B%F0%AA%82%9Egb3gtlD33` | `xn--bgb3gtld33-xb95m` |
| whatwg vs legacy | `data://hO𪰯/../⤹\Ⲳ@4~7C435KIw:9UK9\0p0?#` | `hO%F0%AA%B0%AF` | `xn--ho-bw24b` |
| whatwg vs legacy | `data://B8TTO@36.65.0.102452秖𨭂}j6393c3x0Gn783Do14?#` | `36.65.0.102452%E7%A7%96%F0%A8%AD%82}j6393c3x0Gn783Do14` | `36.65.0.xn--102452-ur1p66994a` |
| whatwg vs url-parse | `http://558:767332:@Ug0pl866281hd.Mj7-N𝃧ᇉ⑰?#k` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `ug0pl866281hd.mj7-n𝃧ᇉ⑰` |
| whatwg vs url-parse | `ws://do2ycs037T@1𦓂3⦷8y5/./(28KZ3tq83U3y3lg?#` | `xn--138y5-2x5cz9190b` | `1𦓂3⦷8y5` |
| whatwg vs url-parse | `bolo://0𠲳1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `xn--01e65-qp48f.4.17.3:77058479` | `0𠲳1e65.4.17.3` |
| whatwg vs url-parse | `http://5n	@29.00.6.78(97217)
4w⤴𗮄h⬁Xc?#` | `29.00.6.xn--78(97217)4whxc-bv1k41vgn82z` | `29.00.6.78(97217)4w⤴𗮄h⬁xc` |
| whatwg vs url-parse | `ftp://9𝣔\򉳭4m0h2R84jkVdTKx@[Df:0:Ac:7:7B:d2:1c:d]:2315?#` | `xn--9-ro8w` | `9𝣔` |
| whatwg vs url-parse | `http://jn7Lq惏0?@。93-D。CEsHZE2Ko2v:?#` | `xn--jn7lq0-mm6l` | `jn7lq惏0` |
| whatwg vs url-parse | `http://///1K8jECVgP23Ō?Y@[C:A0:54:B:3:a:86:d8]:7418?#` | `1k8jecvgp23ō` | `xn--1k8jecvgp23-v9b` |
| whatwg vs url-parse | `https://f2eV7J8G!↾/Mh@14:2425?#` | `xn--f2ev7j8g!-yq3e` | `f2ev7j8g!↾` |
| whatwg vs url-parse | `http://T0a␉Rqq/.@7F03h6m0HuVI37sCrXz:1284?#` | `xn--t0arqq-r85c` | `t0a␉rqq` |
| whatwg vs url-parse | `ws://A5F⊭\ૣ$?#` | `xn--a5f-8t2a` | `a5f⊭` |
| legacy vs url-parse | `wss://6:16@-wRt04rzXgf-92I..77ᄧ?#` | `-wrt04rzxgf-92i..77ᄧ` | `-wrt04rzxgf-92i..xn--77-k6n` |
| legacy vs url-parse | `ws://6zKr96Bg00Os8JE313𥱗j`\?#` | `6zkr96bg00os8je313𥱗j`` | `xn--6zkr96bg00os8je313j-tu56u` |
| legacy vs url-parse | `data://97vrV56𠄩⁔{7F󀣁4WMO54T1I6-44c--5。?#` | `xn--97vrv56-vh7c64473b` | `97vrv56𠄩⁔{7f󀣁4wmo54t1i6-44c--5。?#` |
| javascript-whatwg vs javascript-legacy | `telnet://Z4
ᾜ4E/../` | `Z4%E1%BE%9C4E` | `xn--z44e-6md7223b` |
| javascript-whatwg vs javascript-legacy | `unreal://B𪂞gb3gtlD33/...` | `B%F0%AA%82%9Egb3gtlD33` | `xn--bgb3gtld33-xb95m` |
| javascript-whatwg vs javascript-legacy | `data://B8TTO@36.65.0.102452秖𨭂}j6393c3x0Gn783Do14` | `36.65.0.102452%E7%A7%96%F0%A8%AD%82}j6393c3x0Gn783Do14` | `36.65.0.xn--102452-ur1p66994a` |
| javascript-whatwg vs javascript-legacy | `data://hO𪰯/../` | `hO%F0%AA%B0%AF` | `xn--ho-bw24b` |
| javascript-whatwg vs javascript-legacy | `data://B%F0%AA%82%9Egb3gtlD33/` | `B%F0%AA%82%9Egb3gtlD33` | `xn--bgb3gtld33-xb95m` |
| javascript-whatwg vs javascript-parse-uri | `data://jn7Lq懏0/...` | `xn--jn7lq0-mm6l` | `jn7Lq懏0` |
| javascript-whatwg vs javascript-parse-uri | `data://1𦓂3⦷8y5/...` | `xn--138y5-2x5cz9190b` | `1𦭂3⦷8y5` |
| javascript-whatwg vs javascript-parse-uri | `data://29.00.6.78(97217)4w⤴𗮄H⬁Xc/...` | `29.00.6.xn--78(97217)4whxc-bv1k41vgn82z` | `29.00.6.78(97217)4w⤴𧞄H⬁Xc` |
| javascript-whatwg vs javascript-uri-js | `http://558:767332:...@Ug0pl866281hd.Mj7-N𥃧ᇉ⑰` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `ug0pl866281hd.xn--mj7-n-zxvz37ojx87j` |
| javascript-whatwg vs javascript-uri-js | `data://xn--s386nl880-q1aa798f5r08t/...` | `xn--s386nl880-q1aa798f5r08t` | `s%C3%A0%C2%B5%C3%A0%C2%B386nl880...` |
| javascript-whatwg vs javascript-urijs | `http://...@[C:A0:54:B:3:a:86:d8]:7418...@1K8jECVgP23Ō?...` | `1K8jECVgP23Ō` | `xn--1k8jecvgp23-v9b` |
| javascript-whatwg vs javascript-url-parse | `wss://43𥙚?...@g1．Q．.5..--..5oO2ia:7970/...` | `43𥙚` | `xn--43-p909a` |
| javascript-whatwg vs go-net | `data://Tt5喗ᵛi/...` | `Tt5喗ᵛi` | `xn--tt5vi-8t0e` |
| javascript-whatwg vs go-net | `data://PJ4OvFF90T7∌/...` | `PJ4OvFF90T7∌` | `xn--pj4ovff90t7-1e8f` |
| javascript-whatwg vs go-net | `data://43𥙚/...` | `43𥙚` | `xn--43-p909a` |
| javascript-whatwg vs go-net | `data://Acp824KGoH94z4359𢨃/...` | `xn--acp824kgoh94z4359-5f11s` | `Acp824KGoH94z4359𢨃` |
| javascript-whatwg vs go-net | `data://11aT-𦾼)/...` | `11aT-𦾼)` | `xn--11at-)-0y52g` |
| javascript-legacy vs javascript-uri-js | `data://97vrV56�합⁔{7F.../#` | `97vrv56%ED%A1%80%ED%B5%A9%E2%81%94%7B%0B7f%ED%A6%A0%ED%BA%A14wmo54t1i6-44c--5%E3%80%824%09%E1%85%A6b%16%EB%92%B3z!q%E2%98%94%ED%A1%B3%ED%B7%96j9428%5E4j[hhpqz88q2y` | `xn--97vrv56-vh7c64473b` |
| javascript-legacy vs javascript-uri-js | `telnet://Z4ᾜ4E/.../...@00𨣬...#` | `z4%0D%E1%BE%944e` | `xn--z44e-6md7223b` |
| javascript-legacy vs javascript-parse-uri | `wss://6:16@-wRt04rzXgf-92I..77ᄧ?#` | `-wRt04rzXgf-92I..77ᄧ` | `-wrt04rzxgf-92i..xn--77-k6n` |
| javascript-legacy vs javascript-parse-uri | `ws://6zKr96Bg00Os8JE313𡳗j`\6𦄔Ӛ(𢑩뛣Q93c5-:742...` | `6zKr96Bg00Os8JE313𡳗j`\6𦄔Ӛ(𢑩뛣Q93c5-` | `xn--6zkr96bg00os8je313j-tu56u` |
| javascript-whatwg vs python-urllib3 | `http://T0a␉Rqq/.@7F03h6m0...@:21PKL0ut?#` | `t0a␉rqq` | `xn--t0arqq-r85c` |
| javascript-whatwg vs python-urllib3 | `http://ug0pl866281hd.mj7-n𙣧ᇉ⑰/...` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `ug0pl866281hd.mj7-n𙣧ᇉ⑰` |

| javascript-legacy vs go-net | `data://15Ↄ/...` | `15Ↄ` | `xn--15-7su` |
| javascript-legacy vs python-urllib3 | `data://18.4.42.1579ᶿb_675/...` | `18.4.42.1579ᶿb_675` | `18.4.42.xn--1579b_675-n0e2862iyl42a` |
| javascript-legacy vs python-urllib3 | `data://z4ᾔ4e/...` | `z4ᾔ4e` | `xn--z44e-6md7223b` |
| perl-uri vs java-galimatias | `...(URL with IDN host)...` | `xn--9760-cca9yim.6.70034LI959s+8c0M+wd84XqF` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| perl-uri vs java-galimatias | `wss://60cD1k7Gx,@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `xn--9760-cca9yim.6.70034LI959s+8c0M+wd84XqF` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| js-whatwg vs go-net | `...(URL with IDN)...` | `15⅃` | `xn--15-7su` |
| js-whatwg vs go-net | `...(URL with IDN)...` | `Tt5㖗ᵛi` | `xn--tt5vi-8t0e` |
| js-whatwg vs go-net | `...(URL with IDN)...` | `xn--s386nl880-q1aa798f5r08t` | `SÀµÀ³86nl880𩼱` |
| go-net vs rust-url | `...(URL with CJK in host)...` | `43��` | `xn--43-p909a` |
| go-net vs rust-url | `...(URL with modifier letter in host)...` | `Tt5㖗ᵛi` | `xn--tt5vi-8t0e` |
