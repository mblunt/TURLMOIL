# Userinfo parsing error

**Description:** One parser fails to correctly extract userinfo, returning corrupted or incomplete data

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3󈥰$#I2` | `3SEC8ar3W56860:Ol61` | `00v069}􋤌5{A37689VA3` |
| whatwg vs legacy | `http://xn--848kjrnt@-x576a:1211<𩱊?#` | `xn--848kjrnt` | `00v069}􋤌5{A37689VA3` |
| legacy vs parse_uri | `http://77oPR6l2e3146R7wX1u:nw75@-g.2pEcNOEPp42q0Tf.:9120	|�툶≮🾻ؤ"
72𕄷𑀈T{T512$SAu6x266xwic?#𹀝` | `77oPR6l2e3146R7wX1u:nw75` | `00v069}􋤌5{A37689VA3` |
| legacy vs parse_uri | `wss://p875ἙP|
󳄞7o4@479.za.88-64-bt.xn--673,x7f-c325c?#` | `p875ἙP|
󳄞7o4` | `00v069}􋤌5{A37689VA3` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88` | `3SEC8ar3W56860:Ol61` | `00v069}` |
| whatwg vs uripara | `http://xn--848kjrnt@-x576a:1211<𪛚?#` | `xn--848kjrnt` | `M5524T焈l0j` |
| whatwg vs java-jdk | `%68ttps://01%71&%5AX%44@6᫠9$484R?#43w5%7A` | `01q&ZXD` | `kM37d8329qO9hd%ED%AE%A6%ED%B7%B7%ED%A8%82%ED%B1%86tsJd5iT2Xfyx427V` |
| whatwg (2) vs rust-url (4) | `https://JxUSࣸvT⭇|JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `JxUSࣸvT⭇|JxUSࣸvT⭇` | `JxUSࣸvT⭇` |
| whatwg (2) vs rust-url (4) | `ws://00v069
}􋤌5{A37689VA3@06'"StN7ld4v8.379l1|938#g` | `00v069
}􋤌5{A37689VA3` | `00v069}􋤌5{A37689VA3` |
| whatwg (2) vs rust-url (4) | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5⑿&6-wYv𣿒េh1=Ԁo5H71j}Z55(9@1JLw5x?#` | `0xb8pmKx6k4` | `0xb8pmKx6k4` |
| whatwg (2) vs rust-url (4) | `http://5n	󴈧]𩎯AcT1@29.00.6.78(97217)` | `5n	󴈧]𩎯AcT1` | `5n	󴈧]𩎯AcT1` |
| whatwg (2) vs rust-url (4) | `ventriloI://3Y63NWUY67C3:3v
@7j@7Er0。59z85j18m:50` | `3Y63NWUY67C3:3v` | `3Y63NWUY67C3:3v` |
| whatwg (2) vs rust-url (4) | `ftp://W𪠪⚬󰫸ᓆ%0C𪐝Ŋ2􅽲e3l9H54%37@8%35:003%13)
%29%34%31%36;7q%6FD+%4EHSW3%71Z7mV?#` | `W𪠪⚬󰫸ᓆ%0C𪐝Ŋ2􅽲e3l9H54%37` | `W𪠪⚬󰫸ᓆ%0C𪐝Ŋ2􅽲e3l9H54%37` |
| whatwg (2) vs rust-url (4) | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9` | `JxUSࣸvT⭇` | `JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9` |
| whatwg (2) vs rust-url (4) | `ws://00v069
}􋤌5{A37689VA3@06'"StN7ld4v8.379l1` | `00v069
}􋤌5{A37689VA3` | `00v069
}􋤌5{A37689VA3@06'"StN7ld4v8.379l1` |
| whatwg (2) vs rust-url (4) | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5⑿&6-wYv𣿒េh1=Ԁo5H71j}Z55(9` | `0xb8pmKx6k4` | `0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5⑿&6-wYv𣿒េh1=Ԁo5H71j}Z55(9` |
| whatwg (2) vs rust-url (4) | `http://5n	󴈧]𩎯AcT1@29.00.6.78` | `5n󴈧]𩎯AcT1` | `5n	󴈧]𩎯AcT1` |
| whatwg (2) vs rust-url (4) | `ventriloI://3Y63NWUY67C3:3v
@7j` | `3Y63NWUY67C3:3v
` | `3Y63NWUY67C3:3v` |
| whatwg (2) vs rust-url (4) | `file://085X᥸󲯤4pKi4@W9I579-60L-S99j:64` | `085X᥸󲯤4pKi4` | `085X᥸󲯤4pKi4@W9I579-60L-S99j:64` |
| whatwg (2) vs rust-url (4) | `ws://i%32k58%305%445%39_`%410%0Bᆃ*󻓼
񄳗%5CBYv%68@5%2E%329.71%2E46%3A45` | `i2k5805D59_`A0ᆃ*󻓼
񄳗\BYv\68` | `i%32k58%305%445%39_`%410%0Bᆃ*󻓼
񄳗%5CBYv%68` |
| whatwg (2) vs rust-url (4) | `data://ZH5}+𠍮<덌v8K3u46@[88:9F:b:58:29:e:f4:5D]:1242𩀇1` | `ZH5}+𠍮<덌v8K3u46` | `ZH5}+𠍮<덌v8K3u46@[88:9F:b:58:29:e:f4:5D]:1242𩀇1` |
| whatwg (2) vs rust-url (4) | `wss://7JI6m⓵Cm6@5W｡5B6Mw70:9776В92` | `7JI6m⓵Cm6` | `7JI6m⓵Cm6@5W｡5B6Mw70:9776В92` |
| whatwg (2) vs rust-url (4) | `ftp://3K86qy𩍮􍥹96oT1k5@z9LU2-45.k6:14􃃢򴁈2` | `3K86qy𩍮􍥹96oT1k5` | `3K86qy𩍮􍥹96oT1k5@z9LU2-45.k6:14􃃢򴁈2` |
| whatwg (2) vs rust-url (4) | `ws://%7Au9%48򰂑%4C𢴭8򕁵%09􄠅Ԅ@40.%385%2E%36.%38%34:99383` | `zu9H򰂑L𢴭8򕁵	􄠅Ԅ` | `%7Au9%48򰂑%4C𢴭8򕁵%09􄠅Ԅ` |
| whatwg (2) vs rust-url (4) | `data://3nUoVw3822
g⥇⁲*󛾰@ 9dKV9DL0` | `3nUoVw3822
g⥇⁲*󛾰` | `3nUoVw3822
g⥇⁲*󛾰` |
