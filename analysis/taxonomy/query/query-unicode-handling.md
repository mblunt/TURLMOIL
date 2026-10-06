# Query unicode handling

**Description:** Whatwg percent-encodes unicode; legacy preserves or mangles it.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `À%09p𥢋˃Z` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `%22U䗪` |
| whatwg vs node-url | `unknown` | `?%22U%E4%97%AA` | `%22U䕧` |
| whatwg vs node-url | `unknown` | `?%E2%99%B7` | `?♧` |
| whatwg vs posix | `http://ftp://3Z28�ﾐ⒕801 55jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>𸆥⬤󽔇𘆥Su(6t25J0iwxw21j30]?` | `?%E2%99%B7` | `?♧` |
| whatwg vs posix | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gԆ�9𝇪87⊕M�？?` | `?1?%F3%AC%B5%8B4?&1?%F3%AC%B5%8B4?` | `?1?��4?&1?��4?` |
| whatwg vs go | `http://ftp://3Z28󶀄❍80155jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>𧨥⬤򧓧𘳕Su(6t25J0iwxw21j30]?♧#"_0Z3` | `?%E2%99%B7` | `?♧` |
| whatwg vs legacy | `https://0a48?07g10s@.60.-0Q614��?#` | `?07g10s@.60.-0Q614%F2%B9%A8%84?` | `?07g10s@.60.-0Q614��?` |
| whatwg vs legacy | `data://9m4?0!󻣁?nZ@[3:bc:Cd:A:A2:ac:C:D]:2434#` | `?0!%F3%A7%BB%91?nZ@[3:bc:Cd:A:A2:ac:C:D]:2434` | `?0!󻣁?nZ@[3:bc:Cd:A:A2:ac:C:D]:2434` |
| whatwg vs legacy | `http://ftp://3Z28􌃄♕�80155jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>��⬤􌳇𨇫a(6t25J0iwxw21j30]?♯#"_0Z3` | `?%E2%99%B7` | `?♯` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gզ𝲘9⟕M󰒔?1?􌵋4?&1?􌵋4?` | `?1?%F3%AC%B5%8B4?&1?%F3%AC%B5%8B4?` | `1?􌵋4?&1?􌵋4?` |
| radix (3) vs whatwg (4) | `ws://A5F∌\ꫣ$ .N��(‥
8?��gFIE372k14j.q63K-y-2ug-dn1YM:383�ufffd085dE3&\822Fru,7BqK?#` | `?�gFIE372k14j.q63K-y-2ug-dn1YM:383�085dE3&\822Fru,7BqK?` | `?�gFIE372k14j.q63K-y-2ug-dn1YM:383�085dE3&\822Fru,7BqK?` |
| legacy vs ada | `http://tB9maq36Xi3W0@93.59.72.404v𨶜&񽳀J@2mX0R2'5(023p?=66a2DgM` | `?=66%0Ca2DgM` | `=66a2DgM` |
| legacy vs ada | `http://ftp://3Z28򆇄❕80155jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>𦠥⬤򅒇𠣵Su(6t25J0iwxw21j30]?♷#"_0Z3` | `?%E2%99%B7|` | `♷` |
| legacy vs ada | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gբ𐦬�뙘񸗄?1?󺿦b4?&1?󺿦b4?
?1?󺿦b4?&1?󺿦b4?` | `?1?%F3%AC%B5%8B4?&1?%F3%AC%B5%8B4?` | `1?󺿦b4?&1?󺿦b4?` |
| legacy vs ada | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2𩶄Ԕ6377723lG8J6O0u)!82?#` | `?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2%E7%B8%B46377723lG8J6O0u)!82?` | `W2mqD[2:C:Ee:C:FB:F8:6:1f]:2𩶄Ԕ6377723lG8J6O0u)!82?` |

