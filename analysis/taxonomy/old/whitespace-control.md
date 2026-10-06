# Whitespace and Control Characters in Host

**Description:** Whitespace or control characters (tabs, newlines, null bytes) embedded in the host are stripped, replaced, or cause the parser to terminate host extraction at different positions, yielding different host values.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-jdk-uri vs java-spring-mvc | `http://9ov425f8ESpU54 ጷ0ءwd-.K0勸7:65?#` | `9ov425f8ESpU54‚𐀷wd-.K0勸_7` | `9ov425f8ESpU54‚𐀷wd-.K0勸7` |
| java-jdk-uri vs java-spring-mvc | `http://3KHrM77A48u93Oi4	289oWUAN96	]...?#` | `1]p
끨𠸕𑳝]󴵄˩󀢶簞xSJ3s{3pYp3181y}m1i` | `` |
| node-whatwg vs php-league | `http://3KHrM77A48u93Oi4	289oWUAN96	]...?#` | `` | `3KHrM77A48u93Oi4	289oWUAN96	]...` |
| node-whatwg vs php-league | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y󋘂:101L?#` | `	ᇰx8	ᵡ
y󋘂` | `` |
| php-pecl-http vs php-pear-net-url2 | `http://9ov425f8ESpU54‚𐀷�-.K0勸7:65?#` | `9ov425f8ESpU54‚𐀷�-.K0勸_7` | `` |
| php-pecl-http vs php-pear-net-url2 | `https://E294t85@  5E
3⃯볼 wH㣌Ⓠ567&...?#0` | ` 5E__3⃯볼_wH㣌Ⓠ567_&...` | `` |
| php-pecl-http vs php-pear-net-url2 | `https://tÀ¶f7@9.0µ.24.²	_Ⳃ...?#` | `9.0Àµ.24.À²__Ⳃ...` | `` |
| perl-uri vs perl-mojo | `wss://5gPK6D2y@2｡29｡9.3_󼃨
G@℔	^󼢥}...?#` | `6a4X.w04,	B}391752316e5ZVx99M` | `` |
| perl-uri vs perl-mojo | `http://9ov425f8ESpU54‚𐀷�-.K0勸7:65?#` | `9ov425f8ESpU54%E2%80%9A%F4%80%A0%B7%DD%9A-.K0%E5%8B%B8_7` | `` |
| python-stdlib vs python-whatwg | `wss://5gPK6D2y81REN@2｡29｡9.3_...@℔	^󼢥}...⿗U)
󾀷j┐...?#` | `℔	^󼢥}��
󾀷j┐59qXRshi24i1DG6_61h` | `` |
| python-stdlib vs python-whatwg | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y󋘂:101L?#` | `	ᇰX8	ᵡ
Y󋘂:101L"9O뮷...` | `	ᇰX8	ᵡ
Y󋘂` |
| scala-play vs elixir-uri | `wss://5gPK6D2y81REN@2｡29｡9.3_...@℔	^󼢥}...?#` | `℔_^󼢥}��_⿗U)_󾀷j_┐59qXRshi24i1DG6_61h` | `` |
| javascript-whatwg vs javascript-legacy | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b` |
| javascript-whatwg vs javascript-legacy | `wss://5gPK6D2y81REN@2｡29｡9.3_...@℔	^󼢥}...?#` | `...` | `06` |
| javascript-whatwg vs javascript-parse-uri | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4X.w04,	B}391752316e5ZVx99M` |
| javascript-whatwg vs javascript-uri-js | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,%09b%7D391752316e5zvx99m` |
| javascript-whatwg vs javascript-fast-uri | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,	b}391752316e5zvx99m` |
| javascript-whatwg vs javascript-fast-url-parser | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04` | `6a4x.w04,b}391752316e5zvx99m` |
| javascript-whatwg vs javascript-parseuri | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y2:101L"9O?#` | `` | `	ᇰX8	ᵡ
Y2` |
| javascript-whatwg vs javascript-parseuri | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b}391752316e5zvx99m` |
| javascript-whatwg vs javascript-uri-parser | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4X.w04,	B}391752316e5ZVx99M` |
| javascript-whatwg vs javascript-domurl | `http://3KHrM77A48u93Oi4	289oWUAN96	]?#` | `` | `3KHrM77A48u93Oi4	289oWUAN96	]` |
| elixir-uri vs python-urllib3 | `wss://5gPK6D2y81REN446o12@2｡29｡9.3_@⿔	^?#` | `⿔^` | `⿔	^` |
| elixir-uri vs python-urllib3 | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y?#` | `` | `	ᇰX8	ᵡ
Y` |
| whatwg vs python-urllib3 | `wss://5gPK6D2y81REN446o12@2｡29｡9.3_@⿔	^?#` | `⿔^` | `` |
| whatwg vs python-urllib3 | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| go-net vs elixir-uri | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y:101?#` | `	ᇰX8	ᵡ
Y` | `` |
| whatwg vs go-net | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `` |
| whatwg vs go-net | `Ktoolms://Kexy@e5@Q.D:346@Q133Jx3~(R5De'4M3dE?#` | `%15Q133Jx3~(R5De'4M3dE` | `` |
| rust-uriparse vs python-urllib3 | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `3324g845648oko2d9s8j` | `` |
| whatwg vs rust-url | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs python-urllib3 | `ws://R6tBj668463bSfmPR:737VaU02NqLv55OL712@68.38.1.241067	ᨁ	9p?#` | `68.38.1.xn--2410679p-zt38j` | `68.38.1.241067ᨁ9p` |
