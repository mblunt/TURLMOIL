# Port parsing error

**Description:** One parser fails to correctly extract port, returning malformed or corrupted data

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3�$#I2` | `88` | `50` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ 9𝙘 87⊕M�?1?�4?&1?�4?` | `48` | `50` |
| whatwg vs custom | `http://558:767332:�@Ug0pl866281hd.Mj7-N𩁧Ƈ⑰?#k` | `767332` | `733` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3��$#I2` | `88` | `50` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[g֐똘9𝟘87⋕M�튔?1?𻇋4?&1?𻇋4?` | `48` | `50` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3��$#I2` | `88` | `9120` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?/":3��$#I2` | `88` | `77058479` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88` | `88` | `50` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB` | `48` | `50` |
| whatwg vs ada | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gֆ龸⊕M󐃔?1?􉯋4?&1?􉯋4?` | `48` | `8175` |
| whatwg vs node | `http://558:767332:𫖗@Ug0pl866281hd.Mj7-N𩶧Ƈ⑲?#k` | `767332` | `22` |
| whatwg vs python | `data://7c6R	9ﵭ𖷺d4c2@[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `53` | `.` |
| ada vs node | `https://JxUSุvT⭇@99.93.4.62:22F56^<oϩxg*6}::'25Ny`K934🩵ꊧ𑏅@00?"Uʗaa` | `22` | `2` |
| whatwg vs ada | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝓘‏87⢕M𖦔?1?𻆋4?&1?𻆋4?` | `48` | `048` |
| legacy vs rust | `http://I3q8912G8b󿿄^𧢡 23o@[a7:16:2A:1E:fE:D:3B:8]:3  E1n27S1$9IULq&[Ll91#` | `16` | `3` |
| legacy vs rust | `wss://8k484X0h98𩒎
࿏���𪶃Gy@[9D:4F:D:5D:4:99:A:5]:43"v*409uBX252g8Xx3Ak?#` | `4` | `43` |
| legacy vs rust | `wss://jxc8703Ầ�M8l18d@[38:6:A8:6:6c:0d:13:fa]:15|VV7KA59v6LDP4A6=14?#` | `6` | `15` |
| legacy vs rust | `file://dZ8b24u69𡀜“1p0y0i1fzQ1786@[C2:77:bc:5E:d2:a:f:9]:187 
 qdO4l60d4Uy"Rp54Gx1?#` | `77` | `187` |
| legacy vs rust | `https://K2w6u522VW376oL95s0,𢠧 1ᚯ⇓u@[E:5C:2:f9:3C:A:94:f]:23^4mFc67+78Gm8br1d1Z?#` | `23` | `5` |
| rust vs rust | `data://DFWPX07Bs61MfVwD02񩓋󡀡��(@2�▪�u udd87@[8c:8A:6B:9:cc:18:Dc:3]:73?#` | `73` | `8` |
| rust vs rust | `ws://gC!󸰃
"󱶷q@[9f:9f:1:D0:4:d:d8:B]:9680?#` | `9` | `9680` |
| rust vs rust | `wtai://7uJa5m81@[b8:3:Ad:Ed:0f:D:1:5]:52/...sF8o4v3102WWeFtk9HP?#` | `3` | `52` |
| rust vs rust | `http://8531yw2󺳭9uY0281@[7:8F:d:Cd:c6:4d:c:9A]:498\5s4Bp5l8gGnl032V87?#` | `498` | `8` |
| rust vs rust | `http://49t1hw52PPM*0|4T@[01:46:94:Ba:cB:eb:4D:51]:2/..760929h205fy0PAK7475yb?#` | `2` | `46` |
| rust vs rust | `message://84094JvqGv5078104K7\13g@[24:6b:cE:8:6:3d:eF:C2]:5?󾉾?D##` | `5` | `6` |
