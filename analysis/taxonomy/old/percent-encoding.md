# Percent-Encoding in Host

**Description:** Host is returned with percent-encoded sequences by one parser but decoded (or re-encoded) by another

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `` |
| whatwg vs legacy | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` | `` |
| whatwg vs legacy | `data://4444r...@9rM｡H3F574l69.1mg-y...` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `` |
| whatwg vs legacy | `dtn://...@66z򱸇...` | `66z%F2%B1%B8%87%F4%81%97%BE` | `` |
| whatwg vs legacy | `market://E0U񗌘_𧙮♴...` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` | `` |
| whatwg vs legacy | `data://...@9rM｡H3F574l69.1mg-y...` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `` |
| whatwg vs parse-uri | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203󙹨o20O` |
| whatwg vs uri-js | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203%ED%AC%A7%ED%B9%A8o20o` |
| whatwg vs smithy | `ms-virtualtouchpad://...@g𨜇ow?...` | `` | `g%F0%A8%9C%87ow` |
| whatwg vs smithy | `res://McZM8a8Ḋ/...` | `` | `McZM8a8%E1%B8%8A` |
| whatwg vs smithy | `data://...&����+...` | `` | `&%F4%8F%AE%B0+%0C` |
| whatwg vs smithy | `iris.xpc://15S9KⱲ?...` | `` | `15S9K%E2%B1%B2` |
| whatwg vs legacy | `go://5j7TF3XR𛳙
ࣼ⤕vr@2203󦗨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `` |
| whatwg vs legacy | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z��𑟾?#~n\sp` | `66z%F2%B1%B8%87%F4%81%97%BE` | `` |
| whatwg vs legacy | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs legacy | `apt://9KrJFVkX2745kecV0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` | `` |
| whatwg vs legacy | `data://4444r󠏤@9rM｡H3F574l69.1mg-y3𢃟#ㇵ07!2Oun0Ya1692h3~f4u4T?#` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `` |
| whatwg vs legacy | `market://E0U𡲘_퀀1𨃮♴#󢀀01笂m
,I𬋂q@71．80．86.07:3_E37b9bIf_5eKYSp6]2=?#` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` | `` |
| whatwg vs javascript-parse-uri | `go://5j7TF3XR𛳙
ࣼ⤕vr@2203󦗨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203󦗨o20O` |
| whatwg vs javascript-smithy | `vnc://4O8D1m0d8jO:Y8m@72DRD.03dl64983𐳧`B?"~M8=u{Z%` | `` | `72DRD.03dl64983%1B%F4%87%A7%97`B` |
| whatwg vs javascript-smithy | `ms-media-stream-id://G9/../?1g@88.85.85.3602󢃅%"𪳍G6#+?	��?#` | `G9` | `` |
| whatwg vs javascript-smithy | `http://UMt_
?%	xz@78.40.93.68678577FT;u1]0q86CQoz4?#` | `umt_` | `` |
| whatwg vs javascript-smithy | `ms-virtualtouchpad://g𘼇ow?��V[󠃎w⡤⫂~𐴃%𐳂9@[b6:0:ab:91:5:06:aC:3F]:853B35Uc8l96?&��V[󠃎w⡤⫂~𐴃%𐳂9@[b6:0:ab:91:5:06:aC:3F]:853B` | `` | `g%F0%A8%9C%87ow` |
| whatwg vs javascript-uri-js | `http://DQA2d00o4G@󬃣ῤ+󠒰✓,`𐳬𤵚𐸴󠅠򢃦婳	� h@:21f #` | `` | `%ED%AE%B0%ED%B7%A3%E1%BD%A4+%ED%AB%92%ED%BC%B09%E2%9C%93,%60%ED%AF%8D%ED%B7%AC%ED%A1%92%ED%B7%9A%ED%AF%87%ED%B6%B4%ED%AF%81%ED%BE%97%ED%A5%89%ED%BC%A6%E5%AA%B3%09%ED%A9%BD%ED%BE%A5h%40` |
| whatwg vs javascript-uri-js | `ftp://3*@8󥗅YJ@1]p
둈𠈕𐳝]󤕄˩󠂶粞xSJ3s{3pYp3181y}m1i?
#ASE91bL)` | `` | `8%ED%AE%94%ED%B9%85yj%401]p%01%0D%EB%81%A8%ED%A1%83%ED%B8%95%ED%AF%9E%ED%BA%9D]%ED%AE%93%ED%B5%84%CB%A9%0C%ED%AB%82%ED%B2%B6%E7%B0%9Exsj3s%7B3pyp3181y%7Dm1i` |
| whatwg vs javascript-uri-js | `wss://5gPK6D2y81REN446o12피@2｡29｡9.3_��G@⒔	^��}��
'��37234u)
jሏ59qXRshi24i1DG6_61h?#` | `` | `2%EF%BD%A129%EF%BD%A19.3_%ED%AA%82%ED%BD%A8%06%0Dg%40xn--%09%5E%7D%0D%04%0D%0A'37234u)%0Aj%1259qxrshi24i1dg6_61h-xr00ay2l85908itzt0ov8yybhi5nz9745a4mgza` |
| whatwg vs javascript-uri-js | `http://3KHrM77A48u93Oi4	289oWUAN96	]\᾽Ҋ𠣐
]!8󡼷󧇅>9Q:252℃7E%󯴊U058681sy4P8Y79R6|T?#` | `` | `xn--3khrm77a48u93oi4%09289owuan96%09]%5C%0A]!8%3E9q-l69cm604gvf11nbvkzl90c1u` |
| javascript-whatwg vs javascript-legacy | `go://5j7TF3XR@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `` |
| javascript-whatwg vs javascript-legacy | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z򱸇?#~n\sp` | `66z%F2%B1%B8%87%F4%81%97%BE` | `` |
| javascript-whatwg vs javascript-legacy | `data://4444r@9rM｡H3F574l69.1mg-y...` | `9rm%ef%bd%a1h3f574l69.1mg-y%1b3%f1%82%9b%9f` | `` |
| javascript-whatwg vs javascript-legacy | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `9krjfvkx2745kec%ee%9a%a5%e2%ab%a8v0cgy7k8f9ncg-6ay8f0.fp1` | `` |
| javascript-whatwg vs javascript-legacy | `market://E0U񗌘_𧙮♴#...` | `e0u%f1%97%8c%98_%13%f0%a7%99%ae%e2%99%b4` | `` |
| javascript-whatwg vs javascript-deno | `ocfsnewsredis://095978B:@@3김𡝎:6200\?` | `` | `3%EA%B8%A0%F0%A1%8D%8E` |
| javascript-whatwg vs javascript-smithy | `ms-virtualtouchpad://g𘰇ow?@[b6:0:ab:91:5:06:aC:3F]:853?` | `` | `g%F0%A8%9C%87ow` |
| javascript-whatwg vs javascript-smithy | `mmsbolok://R@74𓼿49࠲ 22?` | `74%F3%8D%8D%BF49%E0%A0%B222%0B` | `` |
| javascript-whatwg vs javascript-smithy | `data://97c510596𠑈꺜?慇%@5@Y.0Yl.9--to0845e:864?` | `` | `97c5105%0B%EE%87%AD96%F0%A7%91%88%EA%B8%9C` |
| javascript-whatwg vs javascript-smithy | `dtn://28139JKdI61񑁻}?戧%@36.9.39.639?` | `` | `28139JKdI61%F4%89%99%BB}` |
| javascript-whatwg vs javascript-uri-js | `go://5j7TF3XR@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203%ED%AC%A7%ED%B9%A8o20o` |
| javascript-whatwg vs javascript-uri-js | `ftp://3*@8󥓅YJ@1]p
깨𘱕��]?` | `` | `8%ED%AE%94%ED%B9%85yj%401]p%01%0D%EB%81%A8%ED%A1%83%ED%B8%95%ED%AF%9E%ED%BA%9D]%ED%AE%93%ED%B5%84%CB%A9%0C%ED%AB%82%ED%B2%B6%E7%B0%9Exsj3s%7B3pyp3181y%7Dm1i` |
| whatwg vs legacy | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `` |
| whatwg vs legacy | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs parse-uri | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203󙹨o20O` |
| whatwg vs uri-js | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203%ED%AC%A7%ED%B9%A8o20o` |
| whatwg vs legacy | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z򱸇📁?#~n\sp` | `66z%F2%B1%B8%87%F4%81%97%BE` | `` |
| whatwg vs uri-js | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,%09b%7D391752316e5zvx99m` |
| whatwg vs urijs | `go://5j7TF3XR...@2203󙹨o20O/../A2CqL?#` | `2203󙹨o20O` | `2203%F3%99%B9%A8o20O` |
| whatwg vs urijs | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z򱸇📁?#~n\sp` | `66z%F2%B1%B8%87%F4%81%97%BE` | `66z򱸇📁` |
| whatwg vs urijs | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324G845648oko2d9s8J` |
| whatwg vs domurl | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs domurl | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` |
