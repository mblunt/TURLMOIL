# Percent-Encoding Differences

**Description:** One parser percent-encodes characters in the host while the other leaves them decoded, or vice versa.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs url-parse | `go://5j7TF3XR@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `2203󙹨o20o` |
| whatwg vs url-parse | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z򱸇?#` | `66z%F2%B1%B8%87%F4%81%97%BE` | `66z򱸇📾` |
| whatwg vs url-parse | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs url-parse | `telnet://Z4ᾜ4E/../?#` | `Z4%E1%BE%9C4E` | `z4ᾔ4e` |
| whatwg vs url-parse | `unreal://B𪂞gb3gtlD33/...?#` | `B%F0%AA%82%9Egb3gtlD33` | `b𪂞gb3gtld33` |
| whatwg vs url-parse | `market://E0U𑃈_𗥮♴?#` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` | `e0u𑃈_𗥮♠` |
| whatwg vs url-parse | `ms-secondary-screen-setup://0X8E5HV@G77k4t
⛝�쀎悓56D1Є𗞰oA33a2ZL{722/9S6x?#` | `G77k4t%0E%E2%9B%9D%F0%9B%80%8E%E6%82%935%126D1%18%D1%A4%F4%85%AF%A7oA33a2ZL{722` | `g77k4t⛝�쀎悓56d1Ѕ𗞰oa33a2zl{722` |
| whatwg vs url-parse | `data://4444r@9rM｡H3F574l69.1mg-y
3��?#` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `9rm｡h3f574l69.1mg-y3��` |
| whatwg vs url-parse | `Giris.lwzxconicap://q6𯳱⪨/?#` | `q6%F3%BD%A3%B1%E2%AA%A8%1F` | `q6𯳱⪨` |
| whatwg vs url-parse | `Bfishrediss://mX7i7⨍4𘬤񃁁?#` | `mX7i7%E2%A8%8D4%F4%88%AC%A4%F2%B3%8A%81` | `mx7i7⨍4𘬤񃁁` |
| whatwg vs url-parse | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `9krjfvkx2745kec⫨v0cgy7k8f9ncg-6ay8f0.fp1` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` |
| legacy vs url-parse | `ftp://W@8%35:003%13)
%29%34%31%36;7q%6FD+%4EHSW3%71Z7mV?#` | `8` | `8%35:003%13)
%29%34%31%36;7q%6fd+%4ehsw3%71z7mv` |
| legacy vs url-parse | `ftp://Z0@z0ⱽ^%6A0j%619jJt%40U%352kX3%58i.H%72HiG4p%2DT%56:853%23` | `z0ⱽ^%6a0j%619jjt%40u%352kx3%58i.h%72hig4p%2dt%56:853%23` | `z0(` |
| legacy vs url-parse | `http://lKez9 6Dcv35wpcH3@XV.:068%𐁁* ᭞��8Sd4(# 43YD5wh?#` | `xv.:068` | `xv.:068%𐁁* ᭞��8sd4(` |
| javascript-whatwg vs javascript-legacy | `onenote://Dau2@3324G845648oko2d9s8J?` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| javascript-whatwg vs javascript-parse-uri | `https://2203𩩨o20O/...` | `2203%F3%99%B9%A8o20O` | `2203󙹨o20O` |
| javascript-whatwg vs javascript-parse-uri | `data://E0U𑜘_𗥮♴/...` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` | `E0U񗌘_𧙮♴` |
| javascript-whatwg vs javascript-parse-uri | `data://8ttF0y𛥸"` | `8ttF0y%F3%9B%A5%B8"` | `8ttF0y󛥸"` |
| javascript-whatwg vs javascript-parse-uri | `data://hO𪰯` | `hO%F0%AA%B0%AF` | `hO𪰯` |
| javascript-whatwg vs javascript-parse-uri | `data://j96748Wf1c14oqB𔀌/...` | `j96748Wf1c14oqB𤄌󶈛4H` | `j96748Wf1c14oqB%F0%A4%84%8C%F3%B6%88%9B%15%05%05%054H` |
| javascript-whatwg vs javascript-parse-uri | `data://d892-2M8jL50󱷰/...` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` | `d892-2M8jL50𯲏⍐3QJI84Ab5B2P743P` |
| javascript-whatwg vs javascript-parse-uri | `onenote://...@3324G845648oko2d9s8J` | `%043324G845648oko2d9s8J` | `3324G845648oko2d9s8J` |
| javascript-whatwg vs javascript-parse-uri | `data://9KrJFVkX2745kec⫨V0CgY7k8f9NCG/...` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` | `9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1` |
| javascript-whatwg vs javascript-parse-uri | `data://9rM｡H3F574l69.1mg-y/...` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `9rM｡H3F574l69.1mg-y3𠃟` |
| javascript-whatwg vs javascript-parse-uri | `data://Z4ᾜ4E/../` | `Z4%E1%BE%9C4E` | `Z4ᾜ4E` |
| javascript-whatwg vs javascript-parse-uri | `data://d892-2M8jL50𯻏...` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` | `d892-2M8jL50𯲏⍐ 3QJI84Ab5B2P743P` |
| javascript-whatwg vs javascript-uri-js | `https://2203󙹨o20O/...` | `2203%F3%99%B9%A8o20O` | `2203%ED%AC%A7%ED%B9%A8o20o` |
| javascript-whatwg vs javascript-uri-js | `http://...@6a4x.w04,	b}391752316e5zvx99m` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,%09b%7D391752316e5zvx99m` |
| javascript-whatwg vs javascript-uri-js | `ws://...@w8.w1919\n` | `w8.w1919` | `w8.w1919%5Cn` |
| javascript-whatwg vs javascript-uri-js | `data://-j-6.785-.7g6wf2`` | `-j-6.785-.7g6wf2`` | `-j-6.785-.7g6wf2%60` |
| javascript-whatwg vs javascript-uri-js | `data://q6󟒱⪨/...` | `q6%F3%BD%A3%B1%E2%AA%A8%1F` | `q6%ED%AE%B6%ED%B3%B1%E2%AA%A8%1F` |
| javascript-whatwg vs javascript-uri-js | `data://mX7i7⪍4��󢈁/...` | `mX7i7%E2%A8%8D4%F4%88%AC%A4%F2%B3%8A%81` | `mx7i7%E2%A8%8D4%ED%AF%A2%ED%BC%A4%ED%AA%8C%ED%BA%81` |
| javascript-whatwg vs go-net | `data://66z󙷋󡵾/...` | `66z󙷋󡵾` | `66z%F2%B1%B8%87%F4%81%97%BE` |
| javascript-whatwg vs go-net | `data://mX7i7⪍4��󢈁/...` | `mX7i7⪍4��󢈁` | `mX7i7%E2%A8%8D4%F4%88%AC%A4%F2%B3%8A%81` |
| javascript-whatwg vs go-net | `data://B𪂞gb3gtlD33/...` | `B%F0%AA%82%9Egb3gtlD33` | `B𪂞gb3gtlD33` |
| javascript-whatwg vs go-net | `data://X5i20J788V00iY稼/...` | `X5i20J788V00iY%E7%A8%BC` | `X5i20J788V00iY稼` |
| javascript-whatwg vs go-net | `data://15⅃/...` | `15⅃` | `15%E2%85%83` |
| javascript-legacy vs javascript-uri-js | `file://...@xn---a	6-e966c..138830o0insq7ays9q0far?#` | `xn---a%096-e966c..138830o0insq7ays9q0far` | `xn---a6-e966c..138830o0insq7ays9q0far` |
| javascript-legacy vs javascript-uri-js | `file://wz837...@p31-nj.e354K.4.8---9463 \...` | `p31-nj.e354k.4.8---9463` | `p31-nj.e354k.4.8---9463%20%5C%ED%A1%91%ED%B1%B7%E2%A5%BE0%ED%A1%AA%ED%B4%AD` |
| javascript-whatwg vs python-urllib3 | `telnet://Z4ᾜ4E/.../...` | `z4ᾔ4e` | `Z4%E1%BE%9C4E` |
| javascript-whatwg vs csharp-systemuri | `data://297-．5u4-:877?#` | `297-．5u4-` | `297-%EF%BC%8E5u4-` |
| csharp-systemuri vs rust-url | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379` | `9krjfvkx2745kec⫨v0cgy7k8f9ncg-6ay8f0.fp1` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` |
| rust-url vs python-urllib3 | `go://5j7TF3XR🁙@2203𩍨o20O/../A2CqL?#` | `2203𩍨o20o` | `2203%F3%99%B9%A8o20O` |
| rust-url vs python-urllib3 | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z𨋇𑿀?#~n\sp` | `66z𨋇𑿀` | `66z%F2%B1%B8%87%F4%81%97%BE` |
| js-whatwg vs js-urijs | `...@G77k4t...(non-ASCII)...` | `G77k4t%0E%E2%9B%9D%F0%9B%80%8E%E6%82%935%126D1...` | `G77k4t⛝𓀎梓56D1...` |
| js-whatwg vs js-url-parse | `...(non-ASCII host)...` | `V1OJ%F2%86%AF%84%04%02` | `V1OJ��` |
| go-net vs rust-url | `...@66z뢇랾...` | `66z뢇랾` | `66z%F2%B1%B8%87%F4%81%97%BE` |
| go-net vs rust-url | `...@9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1...` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1` | `9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1` |
| go-net vs rust-url | `...@mX7i7⪍4acꓲb3誁...` | `mX7i7⪍4acꓲb3誁` | `mX7i7%E2%A8%8D4%F4%88%AC%A4%F2%B3%8A%81` |
