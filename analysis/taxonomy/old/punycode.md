# Punycode / IDN Encoding

**Description:** Internationalized domain names are encoded to punycode (xn--) by one parser but left as Unicode by another

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `wss://...@xn---a6-e966c..138830o0insq7ays9q0far?` | `` | `xn---a6-e966c..138830o0insq7ays9q0far` |
| whatwg vs legacy | `ws://...xn--6zkr96bg00os8je313j...` | `` | `xn--6zkr96bg00os8je313j-tu56u` |
| whatwg vs legacy | `data://...@xn--97vrv56...4473b` | `` | `xn--97vrv56-vh7c64473b` |
| whatwg vs legacy | `bolo://0𫚳1e65.4.17.3:77058479/...` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| whatwg vs smithy | `ws://c6F9𓚗/...` | `xn--c6f9-t973a` | `` |
| whatwg vs smithy | `file://9⁽⋀?...` | `xn--9(-vqv` | `` |
| whatwg vs smithy | `wss://63l0s5rᶻ6S171at1｡4c4-7｡7xCJ.82qwE-4J...` | `63l0s5rz6s171at1.4c4-7.7xcj.82qwe-4j` | `` |
| whatwg vs smithy | `ftp://8LL烛?...` | `xn--8ll-k67g` | `` |
| whatwg vs smithy | `file://0b뷻?...` | `xn--0b-212j` | `` |
| whatwg vs deno | `ws://c6F9𓚗/...` | `xn--c6f9-t973a` | `` |
| whatwg vs deno | `wss://Ddz441H0h5q5C&...` | `xn--ddz441h0h5q5c&0z-ks2n` | `` |
| whatwg vs deno | `http://m3H05UM8155𳂊...` | `xn--m3h05um8155h-8703t` | `` |
| whatwg vs legacy | `bolo://0𣪳1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| whatwg vs legacy | `ws://0𣔶3ᴱÀ¢V5Á°@zÁ­:59=6󛫑⩌􏧩@𙼫Á°O𞕚'⭁󦓃󡃞#6hs󣒽	Á´?#` | `` | `xn--o-fea9q6959zwq9b` |
| whatwg vs legacy | `wss://6:16@-wRt04rzXgf-92I..77ᄧ?#` | `` | `-wrt04rzxgf-92i..xn--77-k6n` |
| whatwg vs legacy | `ws://6zKr96Bg00Os8JE313𠃗j`\6𦐔Ӛ(𢓩룣Q93c5-:742CK5;599[ffliYi9Za=9?#` | `` | `xn--6zkr96bg00os8je313j-tu56u` |
| whatwg vs legacy | `data://97vrV56𠄩⁔{7F򨈡WMO54T1I6-44c--5。ᅦ듳z!Q☔𜷖j9428^4J[hhpQz88q2Y?#` | `` | `xn--97vrv56-vh7c64473b` |
| whatwg vs deno | `ws://c6F9𓺩7/...}󦲬竷#0.;i98º@n1FL6Po:226⌤GJq344(tj.2E603ED`1?O` | `xn--c6f9-t973a` | `` |
| whatwg vs deno | `http://m3H05UM8155󣂊
H/@3.02/..56.12:947?` 	:3󡳘
-#\c#` | `xn--m3h05um8155h-8703t` | `` |
| whatwg vs deno | `ws://vV2U6Rp027y𐃸`96J9NX5m7FLQ44r2QI@F.-x.60DⓤၳF?#` | `f.-x.xn--60duf-k59c` | `` |
| whatwg vs javascript-smithy | `wss://63l0s5rᵻ6S171at1｡4c4-7｡7xCJ.82qwE-4J:443?󡧻!%!4~9\2&05roqa"H7tk4h?#8:U5` | `63l0s5rz6s171at1.4c4-7.7xcj.82qwe-4j` | `` |
| whatwg vs javascript-smithy | `file://44792|file://9⁽⋀?'8y@x1-e--y1p2t20:830~.󢓘 𢓒吚󠃥𤔄%󠅜95LzoI1XD8W57HJl4734��紺#"KC` | `xn--9(-vqv` | `` |
| whatwg vs javascript-fast-url-parser | `go://5j7TF3XR𐳙
ࣼ⤕​40xvr@2203󡩨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `xn--2203o20o-mm076d` |
| whatwg vs javascript-fast-url-parser | `http://558:767332:��@Ug0pl866281hd.Mj7-N��᱉⓳?#k` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `ug0pl866281hd.xn--mj7-n-zxvz37ojx87j` |
| whatwg vs javascript-fast-url-parser | `file://fPe2󨃮󨂎0
95iZ󨆻3。+ 6。3E56-N6N9N3510D。a:94]^XvGi9H5x476LbI58~8W?#` | `` | `xn--fpe20-sb711cntn` |
| javascript-whatwg vs javascript-legacy | `bolo://0𫚳1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `` | `xn--01e65-qp48f.4.17.3:77058479` |
| javascript-whatwg vs javascript-legacy | `ws://0𣖶ᴱÀ¢V5Á°@zÁ­:59=6@𩜫Á°O𦅚'⭁?#6hs` | `` | `xn--o-fea9q6959zwq9b` |
| javascript-whatwg vs javascript-legacy | `7Ys74i9Rau41R:56❾s?1redis://e7w69055Kzcp` | `` | `xn--56s-4u6a` |
| javascript-whatwg vs javascript-legacy | `file://2:k26sQ2jJc4522@xn---a	6-e966c..138830o0insq7ays9q0far?#` | `` | `xn---a6-e966c..138830o0insq7ays9q0far` |
| javascript-whatwg vs javascript-legacy | `wss://6:16@-wRt04rzXgf-92I..77ᄧ?#` | `` | `xn--77-k6n` |
| javascript-whatwg vs javascript-legacy | `ws://6zKr96Bg00Os8JE313𡡗j`\6𦈔Ӛ(𢑩Q93c5-:742?` | `` | `xn--6zkr96bg00os8je313j-tu56u` |
| javascript-whatwg vs javascript-legacy | `data://97vrV56𠅩⁔{7F񸊡4WMO54T1I6-44c--5。4	ᅦb뒳z!Q?` | `` | `xn--97vrv56-vh7c64473b` |
| javascript-whatwg vs javascript-deno | `ws://c6F9𓣗/...@n1FL6Po:226?` | `xn--c6f9-t973a` | `` |
| javascript-whatwg vs javascript-deno | `ws://vV2U6Rp027y@F.-x.60DⓤჳF?#` | `f.-x.xn--60duf-k59c` | `` |
| javascript-whatwg vs javascript-deno | `ws://Ddz441H0h5q5C&
0ZႾ#k@[9:Cc:C:B:Bb:b0:C:f9]?` | `xn--ddz441h0h5q5c&0z-ks2n` | `` |
| javascript-whatwg vs javascript-deno | `http://m3H05UM8155𣂊
H/@3.02/..56.12:947?` | `xn--m3h05um8155h-8703t` | `` |
| javascript-whatwg vs javascript-deno | `ms-settings://xn--c	{-g675b/⬋3M47:8095/?` | `xn--c{-g675b` | `` |
| javascript-whatwg vs javascript-deno | `wss://63l0s5rᶻ6S171at1｡4c4-7｡7xCJ.82qwE-4J:443?` | `63l0s5rz6s171at1.4c4-7.7xcj.82qwe-4j` | `` |
| javascript-whatwg vs javascript-smithy | `file://9❵⋀?'8y@x1-e--y1p2t20:830?` | `xn--9(-vqv` | `` |
| javascript-whatwg vs javascript-smithy | `ftp://8LL烛	?@6:6204321773?` | `xn--8ll-k67g` | `` |
| javascript-whatwg vs javascript-smithy | `ftp://8asnc4894u6O员?@3.37.9.950504?` | `xn--8asnc4894u6o-y11u` | `` |
| whatwg vs legacy | `ws://c6F9𓚗/...}󶮌竏#0.;i98º@n1FL6Po:226⌬GJq344(tj.2E603ED`1?O|0󱾄.U` | `xn--c6f9-t973a` | `` |
| whatwg vs legacy | `http://m3H05UM8155𳂊H/@3.02/..56.12:947?` :3񧞘-#\c#` | `xn--m3h05um8155h-8703t` | `` |
| whatwg vs legacy | `ws://Ddz441H0h5q5C&0ZႾ#k@[9:Cc:C:B:Bb:b0:C:f9]굗9685M⧚⋀b4X󭈂v?#XNaA86'u2e60` | `xn--ddz441h0h5q5c&0z-ks2n` | `` |
| whatwg vs legacy | `file://xn---a6-e966c..138830o0insq7ays9q0far?#` | `` | `xn---a6-e966c..138830o0insq7ays9q0far` |
| whatwg vs smithy | `file://8LL烛?𑣽%⤲S⧃ 䄥+좟9x6T4Vd5J2368CA4qR5@6:6204321773w"n0+]49r5781?#` | `xn--8ll-k67g` | `` |
| whatwg vs smithy | `http://7。67.88.221Ʋ𲩕4?46⟼oX77#I@o57` | `7.67.88.xn--2214-2ec87815j` | `` |
| whatwg vs deno | `ws://vV2U6Rp027y`96J9NX5m7FLQ44r2QI@F.-x.60DⓤႳF?#` | `f.-x.xn--60duf-k59c` | `` |
| whatwg vs urijs | `http://558:767332:@Ug0pl866281hd.Mj7-N󡳧ᯉ⑰?#k` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `ug0pl866281hd.xn--mj7-n-zxvz37ojx87j` |
| whatwg vs urijs | `ws://do2ycs037T@1𪝒3⦷ 8y5/./(28KZ3tq83U3y3lg?#` | `xn--138y5-2x5cz9190b` | `1𪝒3⦷8y5` |
