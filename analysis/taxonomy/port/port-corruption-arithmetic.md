# Port corruption or arithmetic difference

**Description:** Port values differ by arithmetic operations or truncation, suggesting extraction error or modulo/overflow handling differences.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| legacy (1) vs rust-url (4) | `data://DFWPX07Bs61MfVwD02𙛋𨢡��(@2༤▪hK7sS72@[8c:8A:6B:9:cc:18:Dc:3]:73?#` | `73` | `8` |
| legacy (1) vs rust-url (4) | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...sF8o4v3102WWeFtk9HP?` | `52` | `3` |
| legacy (1) vs rust-url (4) | `ws://5v1580U75fWU415bwp2𩃭;𒚥𖪡𞠗≳��
leN@[4:2:72:f7:3:Ca:94:e]:54?#` | `54` | `2` |
| legacy (1) vs rust-url (4) | `http://Eh3F3JCqZ4l6@[6:4:D:6F:ce:25:a:4C]:70
?#fy` | `70` | `4` |
| legacy (1) vs rust-url (4) | `ws://BTyHJCzXKCBt1a🷔<𣣓ZfCd@[E:5:7:3:9F:d:bE:b]:586/!1LXN9FE5E29:i+wYA79?` | `586` | `5` |
| whatwg (2) vs rust-url (4) | `http://I3q8912G8b🿄^\u0027ʇ@[a7:16:2A:1E:fE:D:3B:8]:3  E1n27S1$9IULq&[Ll91#` | `16` | `3` |
| whatwg (2) vs rust-url (4) | `wss://8k484X0h98𩒎
௯উঃGy@[9D:4F:D:5D:4:99:A:5]:43"v*409uBX252g8Xx3Ak?#` | `4` | `43` |
| whatwg (2) vs rust-url (4) | `ftp://030XoF5Y1KaFJ0Gk42d𩖩870i140y@[Bc:04:cF:Fa:1:bC:78:8162]:767^Ox}n)_gaczgXN2M?#` | `04` | `767` |
| go-net (3) vs rust-url (4) | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...sF8o4v3102WWeFtk9HP?#` | `52` | `3` |
| go-net (3) vs rust-url (4) | `message://84094JvqGv5078104K7\13g@[24:6b:cE:8:6:3d:eF:C2]:5?🲾?D##` | `5` | `6` |
| rust-url (4) vs node (5) | `data://DFWPX07Bs61MfVwD02𡓔A𠒁�ꢏ(@2🗤▪ോ஌இS72@[8c:8A:6B:9:cc:18:Dc:3]:73?#` | `73` | `8` |
| rust-url (4) vs node (5) | `ws://gC!🳅
"\ud809�\ud983q@[9f:9f:1:D0:4:d:d8:B]:9680?#` | `9` | `9680` |
| rust-url (4) vs node (5) | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...sF8o4v3102WWeFtk9HP?#` | `3` | `52` |
| legacy vs rust-url | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...sF8o4v3102WWeFtk9HP?#` | `52` | `3` |
| legacy vs rust-url | `http://49t1hw52PPM*0|4T@[01:46:94:Ba:cB:eb:4D:51]:2/..760929h205fy0PAK7475yb?` | `2` | `46` |
| legacy vs rust-url | `wss://0OK4f6B	`}򴊫
e6X@[57:3:3e:CA:38:9:8:Fd]:1983?~514T	3􄾥᫞򈔙*⨦Ա/#Վ󶕩3"#` | `3` | `1983` |
| legacy vs rust-url | `ws://k778℧
1m8wF@[DD:5:1:A0:dc:5:AD:8]:191/󃁍󳂥09|32Hk9O4045A?#󼣤 ` | `191` | `5` |
| legacy vs rust-url | `data://Kqtf14@[79:42:Ef:E:eC:b:db:Eb]:5961?#` | `5961` | `42` |
| legacy vs rust-url | `itms://9𢸼]:7CrO@[6:8a:4F:7f:C9:a:4:bb]:4/..574Ⓚ?#38s3dR5` | `4` | `8` |
| legacy vs rust-url | `stun://EdP04􎐕44⊭ @[F:2:A:f5:DF:7:f5:4]:835?#` | `835` | `2` |
| legacy vs rust-url | `cap://3vd95jVyb4N⧃]𢩾󴊯󴨔Q𨫴ev@[A1:8:37:e:C:F8:a:c7]:287?#` | `8` | `287` |
| legacy vs rust-url | `http://I2dbX10c7D4Z5p5WK3r􊡩8No28PB3W84KX9f7c67@[Ae:0a:0:B:4:9:0A:2d]:7/򁌉􊊴ᴭ⋧)񬯉
򆺇􉔌󾘻_퉙03 먢➺M8U1!3l3pN62N6m9h0T?#` | `7` | `0` |
| legacy vs rust-url | `wss://553de5u44LPLuC40nwL⨗♫3QDIpK0Qqy9796tEQpb@[f2:3D:16:Af:8C:2:e:55]:03552?rkWn+` | `3552` | `3` |
| legacy vs rust-url | `qb://0w427wo56G9B57zL8s0H7g6536rg5@[4e:9D:b:F:cC:1:b4:2]:4861?04=0XJ\f05_#` | `4861` | `9` |
| legacy vs rust-url | `https://9g48mrR~j􋿚(340J4n68DW@[aF:41:5C:dB:E6:0A:F:82]:6691/...󇪑"}𐃤`8gq3z0b^hSww269B225?` | `6691` | `41` |
| legacy vs rust-url | `https://32P8B@[1d:2:Ce:8F:4:5a:E:2]:1753` | `1753` | `2` |
| legacy vs rust-url | `https://Iq6kIdh2nu583zO7K83><Y809i@[b2:5:dE:d:Fe:93:34:4]:4229#x◨4?#` | `5` | `4229` |
| legacy vs rust-url | `wss://O􎠍	)h80Q9@[e:0:7d:7E:1b:AA:75:ff]:25#` | `25` | `0` |
| legacy vs rust-url | `ws://JXR>$%򺬽q8Gj9l@[5:9:3D:a:00:3D:88:75]:27\6v89HH5(y3h67IazJ6?#` | `27` | `9` |
| legacy vs rust-url | `ftp://Dn6u3ajZab91c@kX-GeG4X04s-35K3a-3:4615jH@Y2!5xt4`404_ZZ:4?` | `4` | `4615` |
| legacy vs rust-url | `ws://pEO37of14I11pS22󫎨𣐊3Z9@[E9:0:EA:DE:b9:b:24:c]:6?#` | `6` | `0` |
| legacy vs rust-url | `ws://gC!󸃅
"􉞷q@[9f:9f:1:D0:4:d:d8:B]:9680?#` | `9680` | `9` |
| legacy vs rust-url | `http://8531yw2񊻍9uY0281@[7:8F:d:Cd:c6:4d:c:9A]:498\5s4Bp5l8gGnl032V87?#` | `498` | `8` |
