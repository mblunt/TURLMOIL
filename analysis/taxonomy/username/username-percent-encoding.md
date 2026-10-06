# Username percent-encoding

**Description:** One parser preserves raw username while other applies percent-encoding or decoding

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2񀈠À³#?󳃶À¬À¼` | `QP1km1TV` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2񀈠À³#?󳃶À¬À¼` | `QP1km1TV` | `VcJI58u50` |
| whatwg vs legacy | `	l://@526⸝v⠹5:936𥱟Hj2@9󾾑郐8Vl᢫𨔒𪒐a񏶧o?#0` | `%40526%E2%B8%9Dv%E2%A0%B95` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs legacy | `	l://@526⸝v⠹5:936𥱟Hj2@9󾾑郐8Vl᢫𨔒𪒐a񏶧o?#0` | `%40526%E2%B8%9Dv%E2%A0%B95` | `VcJI58u50` |
| whatwg vs legacy | `smtp://s7LTÀºÁºkÀ±c@Àº029K	~Aℕ6󾅷M6?2À£f򂚕򌠎 À©#Ȝ#33` | `s7LT%C3%80%C2%BA%C3%81%C2%BAk%C3%80%C2%B1c` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs legacy | `smtp://s7LTÀºÁºkÀ±c@Àº029K	~Aℕ6󾅷M6?2À£f򂚕򌠎 À©#Ȝ#33` | `s7LT%C3%80%C2%BA%C3%81%C2%BAk%C3%80%C2%B1c` | `VcJI58u50` |
| whatwg vs legacy | `xmlrpc.beeps://X40(H$񃮏H6ᵂF⪗,	▹<3@i065.u5hTycv8.H0ДE𡨋*1񍩲𠀆𱣬Ѱ(64b9d93l{D8z2W53{042?#P` | `X40(H$%F3%8E%8F%84H6%E1%B5%82F%E2%AA%97,%E2%96%B9%3C3` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2` | `QP1km1TV` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs legacy | `smtp://s7LTÀºÁºkÀ±c@Àº029K` | `s7LT%C3%80%C2%BA%C3%81%C2%BAk%C3%80%C2%B1c` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs ada | `http://70t𨀞򗳄}!򑈫፨𡑵K%ZhV513bX8247@U55328XB07Y5lA2P749255w?#` | `70t%F0%A8%80%9E%F2%97%B3%84%7D!%F2%91%88%AB%E1%8D%A8%F0%A1%91%B5K%ZhV513bX8247` | `%EB%A6%B5%022%F3%BE%85%96u%E5%83%8A` |
| whatwg vs node | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6627HpNE72N%3E4` | `mRd810U5154Pf7d8Ro3` |
| whatwg vs legacy | `https://5j7TF3XR􋭙ࣼ⤕40xvr@example.com` | `5j7TF3XR%05%F4%8B%AD%99%E0%A3%BC%0F%01%E2%A4%9540xvr` | `5j7TF3XR􋭙
ࣼ⤕40xvr` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62` | `JxUS%E0%A3%B8vT%E2%AD%87%4099.93.4.62` | `JxUSࣸvT⭇` |
| whatwg vs legacy | `https://6627HpNE72N>4@example.com` | `6627HpNE72N%3E4` | `6627HpNE72N>4` |
| whatwg vs legacy | `https://S1u68𩩹𤊭Gq8@80.6.66` | `S1u68%F0%A9%A9%B9%F0%A4%8A%ADGq8` | `S1u68𩩹𤊭Gq8` |
| whatwg vs legacy | `https://do2ycs037T󹕢s3k@example.com` | `do2ycs037T%F3%B9%95%A2s3k` | `do2ycs037T󹕢s3k` |
| whatwg vs legacy | `https://2W21SCBE@example.com` | `2W21SCBE` | `2W21SCB	E` |
| whatwg vs legacy | `https://p875ἙP|󳔞7o4@example.com` | `p875%E1%BC%99P%7C%F3%B3%94%9E7o4` | `p875ἙP|
󳔞7o4` |
| whatwg vs legacy | `https://4444r󰟤2@example.com` | `4444r%F0%B0%9F%A42` | `4444r󰟤2` |
| whatwg vs legacy | `https://70dx5󲵄៙J⁁25v@example.com` | `70dx5%F3%B2%B5%84%E1%9F%99J%E2%81%8125v` | `70dx5󲵄៙J⁁25v` |
| whatwg vs legacy | `https://pp881Q8328U7W968e敜ᜈ` 󩍭8b5zO@example.com` | `pp881Q8328U7W968e%E6%95%9C%E1%9C%88%60%20%F3%A9%8D%AD8b5zO` | `pp881Q8328U7W968e敜ᜈ` 󩍭8b5zO` |
| radix (3) vs whatwg (4) | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `JxUSࣸvT⭇` | `JxUS%E0%A3%B8vT%E2%AD%87` |
| radix (3) vs whatwg (4) | `go://5j7TF3XR􋭙
ࣼ⤕40xvr@2203󙹨o20O/../A2CqL?#` | `5j7TF3XR%05%F4%8B%AD%99%E0%A3%BC%0F%01%E2%A4%95` | `5j7TF3XRࣼ⤕` |
| radix (3) vs whatwg (4) | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6627HpNE72N>4` | `6627HpNE72N%3E4` |
| radix (3) vs whatwg (4) | `http://5n	󴈧]𩎯AcT1@29.00.6.78(97217)
4444r󰟤2@9rM｡H3F574l69.1mg-y
3񂛟#ㇵ07!2Oun0Ya1692h3~f4u4T?#` | `5n%F3%B4%88%A7%5D%F0%A9%8E%AFAcT1` | `5n	󴈧]𩎯AcT1` |
| radix (3) vs whatwg (4) | `acap://05窊񶩏P@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV?#` | `05窊򶩏P` | `0%065%E7%AA%8A%F2%B6%A9%8FP` |
| radix (3) vs whatwg (4) | `https://p8Ͱ┐;󲺃S797UqAD@[7:2d:4:A7:394:3:3:4]:8󶿍Cj,nT4FL9@wewJOZrh?#` | `p8%CD%B0%04%E2%94%90%3B%F3%B2%BA%83S797UqAD%40%5B7` | `p8Ͱ┐;󲺃S797UqAD` |
| radix (3) vs whatwg (4) | `ut2004://4881CYNhgxL9ta019G7񃬰l63k@4o:246/..lu0u9'756.13t15Sh?#` | `4881CYNhgxL9ta019G7񃬰l63k` | `4881CYNhgxL9ta019G7%F1%83%AC%B0%0Bl63k` |
| radix (3) vs whatwg (4) | `data://2T8䋕󳺀𩲊򧀄⠻sXῴ񦕏<X@3:3]63u[f:Da:d:A5:aF:8f:%1"⠉⠀2&񁡃8 3=5S=3+fxf@j62e33h1vo?#` | `2T8%E4%8B%95%F3%B3%BA%80%1B%F0%A9%B2%8A%F2%A7%80%84%15%E2%A0%BB%13sX%E1%BF%B4%07%F1%A6%95%8F%3CX%403` | `2T8䋕󳺀𩲊򧀄⠻sXῴ񦕏<X` |
| legacy vs node | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `JxUSࣸvT⭇` | `JxUS%E0%A3%B8vT%E2%AD%87` |
| legacy vs node | `go://5j7TF3XR􋭙
ࣼ⤕40xvr@2203󙹨o20O/../A2CqL?#` | `5j7TF3XR%05%F4%8B%AD%99%E0%A3%BC%0F%01%E2%A4%95` | `5j7TF3XR􋭙
ࣼ⤕` |
| legacy vs node | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6627HpNE72N>4` | `6627HpNE72N%3E4` |
| legacy vs node | `http://tB9maq36Xi3W0@93.59.72.404v䙜&󱼀J@2mX0R2'5(023p?=66a2DgM` | `tB9maq36Xi3W0` | `tB9maq36Xi3W0%40` |
| legacy vs node | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e#	6&84{?#gStt` | `S1u68𩩹𤊭Gq8` | `S1u68%F0%A9%A9%B9%F0%A4%8A%ADGq8` |
| legacy vs node | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?#󳦉` | `do2ycs037T󹕢s3k` | `do2ycs037T%F3%B9%95%A2s3k` |
| legacy vs node | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `2W21SCB	E` | `2W21SCBE` |
| legacy vs node | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z򱸇􁗾?#~n\sp` | `K)5` | `K)5%40` |
| legacy vs node | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5⑿&6-wYv𣿒េh1=Ԁo5H71j}Z55(9@1JLw5x?#` | `0xb8pmKx6k4%40%5Ba4` | `0xb8pmKx6k4` |
| legacy vs node | `http://5n	󴈧]𩎯AcT1@29.00.6.78(97217)` | `5n%F3%B4%88%A7%5D%F0%A9%8E%AFAcT1` | `5n	󴈧]𩎯AcT1` |
| legacy vs node | `data://o421p1>
8k50HN27@[69:28:cA:C:5a:0c:2:f]0oٷ𡵔𧵜1(v^k1vY4q4h@6w0U03?#AP` | `o421p1%0C%3E8k50HN27%40%5B69` | `o421p1>
8k50HN27` |
| legacy vs node | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `JxUSࣸvT⭇` | `JxUS%E0%A3%B8vT%E2%AD%87%40` |
| legacy vs node | `go://5j7TF3XR􋭙
ࣼ⤕40xvr@2203󙹨o20O/../A2CqL?#` | `5j7TF3XR%05%F4%8B%AD%99%E0%A3%BC%0F%01%E2%A4%9540xvr` | `5j7TF3XR􋭙
ࣼ⤕40xvr` |
| legacy vs node | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6627HpNE72N>4` | `6627HpNE72N%3E4` |
| legacy vs node | `http://tB9maq36Xi3W0@93.59.72.404v䙜&󱼀J@2mX0R2'5(023p?=66a2DgM` | `tB9maq36Xi3W0` | `tB9maq36Xi3W0%40` |
| legacy vs node | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e#	6&84{?#gStt` | `S1u68𩩹𤊭Gq8` | `S1u68%F0%A9%A9%B9%F0%A4%8A%ADGq8` |
| legacy vs whatwg | `go://5j7TF3XR𢳝9𡂟@2203𶢸o20O/../A2CqL?#` | `5j7TF3XR%05%F4%8B%AD%99%E0%A3%BC%0F%01%E2%A4%9540xvr` | `5j7TF3XR𢳝9∼⌔5𡂕40xvr` |
| legacy vs whatwg | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5⑲&6-wYv𚿢𐑸h1=Ԁo5H71j}Z55(9@1JLw5x?#` | `0xb8pmKx6k4%40%5Ba4` | `0xb8pmKx6k4` |
| legacy vs whatwg | `https://⦹.𠮡2I11;𷐞fCxg
0)𦐧􆞹w @46񁄺,3@Op12b.p7.gDB278F-7p401O0C2.0t2WXM60ux8ys?#` | `%E2%A6%B9.%F0%A0%AE%A12I11%3B%F0%B7%90%9EfCxg0)%F0%A6%90%A7%F4%86%9E%B9w%20%4046%F1%81%84%BA,%123` | `%E2%A6%B9.%F0%A0%AE%A12I11%3B%F0%B7%90%9EfCxg0)%F0%A6%90%A7%F4%86%9E%B9w%20%4046%F1%81%84%BA%2C%123` |
| legacy vs whatwg | `magnet://K7FQ}ᴺ⨍3􂮏
s5,@8+结#9cV2:6725!𒁥󹷨╳`uNS:jX:3g8$mj37q562?#` | `K7FQ%7D%0E%E1%B4%BA%E2%A8%8D3%F4%82%AE%8F%1Es5,` | `K7FQ%7D%0E%E1%B4%BA%E2%A8%8D3%F4%82%AE%8F%1Es5%2C` |
| legacy vs whatwg | `cvs://4FJ27Ov=&Z7WbQ850RN@[DA:DA:BD:9:8:1f:c8:EB]/...:39Ga$8d06aF2:3PLid1c?#` | `4FJ27Ov%3D&Z7WbQ850RN` | `4FJ27Ov%3D%26Z7WbQ850RN` |
