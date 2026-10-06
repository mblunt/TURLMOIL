# Empty vs Non-empty Host

**Description:** One parser rejects the URL and returns empty/null host while the other extracts a host value

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-url | `data://TmOQOA6nx21Uyv8rx8E🯜	󷒹󬳺vAR@tZ7:3\8o9_51H3c699SBw61E#` | `` | `tZ7` |
| javascript-whatwg vs rust-url | `fle://f5Fx3Z8L1@-S9gK:798\f3-X5WV}_XMAi*0{0?#𩖿𩤥` | `` | `-S9gK` |
| javascript-whatwg vs rust-url | `bitcointsteam://3c85x8M52uMy@37p.o0:8666\7gZ$N?#*` | `` | `37p.o0` |
| javascript-whatwg vs rust-url | `callto://6p085437:6T󇅗7y2񰏞񬂮􀡙ℸ105􅃂@lm5E4nQ8-6o.6Q0Bij6:4	\H𩥵򿗁􂈳r 􁷇粲􁅟_sBiG06TA.n2c63N73L5𧱢$_=47L#4` | `` | `lm5E4nQ8-6o.6Q0Bij6` |
| javascript-whatwg vs rust-url | `ms-visio://9Zj5r9D116l93s9R7R0"ᶩ1<-
G-𬤬ᅓBXx@1---d:3\VrCMlD302jYIX8o3i4#` | `` | `1---d` |
| javascript-whatwg vs rust-url | `data://l8s54lT13Y637󆰸�1�⸭􁑵𩈸=󹡊𩈈Ed@16HQj9s-X3bI8r1t91s:23444\49I3j8Q48Aq1y4f6?#` | `` | `16HQj9s-X3bI8r1t91s` |
| javascript-whatwg vs rust-url | `Ndict://321X3F@6-.2p.1GC6Q-9845a4.:178\󺖖𩳲+}0wG!76Z5HX]00W53TkabǼ󀀫 ` | `` | `6-.2p.1GC6Q-9845a4.` |
| javascript-whatwg vs rust-url | `data://D3SJYe1:517@s.54--G-676..8.-56t:9\bug7UP3h0fvDt6sDJ$8y? #` | `` | `s.54--G-676..8.-56t` |
| javascript-whatwg vs rust-url | `itms://K4537u7Si:17zDx56o@ED042W.4d75mMABc:5\XF=𥏰U:L蛃墒>;󅣸◀𪓈B18Z5f82(I86m1lhu2?#I` | `` | `ED042W.4d75mMABc` |
| javascript-whatwg vs rust-url | `data://3퓺󷢜&Y'<[ÊU^8@6.85.8.67:83\9i7875a6La120e90Q?#` | `` | `6.85.8.67` |
| javascript-whatwg vs rust-url | `go://40F7zT_:6
@.S8-mrt.-0E.6-.Ww2T:7\p.Ể񡒢6T448E7Ri^Y7tv5_6:D?{鰸##YJ` | `` | `.S8-mrt.-0E.6-.Ww2T` |
| javascript-whatwg vs rust-url | `data://3SJYe1:517@ndv799213vqQi126XMb:376\3NOG520869Ga9au4WQ?#` | `` | `ndv799213vqQi126XMb` |
| javascript-whatwg vs rust-url | `pkcs11ms-projectg://8:@91.3.70.12:6200\95AQoDn?^ ⟱#.H28` | `` | `91.3.70.12` |
| javascript-whatwg vs rust-url | `data://7841S8HHbqof18&=󾁾289874Mx@ndv799213vqQi126XMb:376\3NOG520869Ga9au4WQ?#` | `` | `ndv799213vqQi126XMb` |
| javascript-whatwg vs rust-url | `mms://7l90:\M5.i91-E3-4328c.-3g:􁓀
#÷愣􁢬
` | `7l90` | `` |
| javascript-whatwg vs rust-url | `im://603M98,!so5u3@648.iRL7jv-41d93q5u:85\l6wRL3{1+09o7XT18$?#` | `648.iRL7jv-41d93q5u` | `` |
| javascript-whatwg vs rust-url | `data://9W08񡧦臺\不Ea24fry@6．52．61.99:290\1v164a1a7\eg1?#` | `6%EF%BC%8E52%EF%BC%8E61.99` | `` |
| javascript-whatwg vs rust-url | `spotify://6l0T3b94炋{U45@e..Z3Nn91g42c.-.499:06591\=32$JIFB891bLaUgU?#` | `e..Z3Nn91g42c.-.499` | `` |
| javascript-whatwg vs rust-url | `data://3L3H97:9675\rZ133]3NL192V`f821?2C𪑭⨸c8xY1@98.1.6.#` | `3L3H97` | `` |
| javascript-whatwg vs rust-url | `iax://741r028．5．6.49:672\)􁳕:;
7P{s7~3N63.)1Tw95MP?#L` | `741r028%EF%BC%8E5%EF%BC%8E6.49` | `` |
| javascript-whatwg vs rust-url | `edcoapcidms-settings-notificationsdropms-powerpoint://i26j2DO270DqS4P1f05'i@5｡93｡95.48:7\A44e14;2vr813M899'?#/[6$0` | `5%EF%BD%A193%EF%BD%A195.48` | `` |
| whatwg vs legacy | `ws://00v069...@06'"StN7ld4v8.379l1|938#g` | `` | `06` |
| whatwg vs legacy | `rediss...://0'...@[6:e:c9:bB:3:80:b3:6b]:2348...` | `` | `0` |
| whatwg vs legacy | `wss://0QJ:68@35006-kA:8175...` | `` | `35006-ka:8175` |
| whatwg vs legacy | `file://7:/...@Z72-Ix2v133...` | `` | `7` |
| whatwg vs legacy | `file://6LF707:3a1@j:28...` | `` | `j:28` |
| whatwg vs legacy | `ftp://...@-wRt04rzXgf-92I..77...` | `` | `-wrt04rzxgf-92i..xn--77-k6n` |
| whatwg vs legacy | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751...` | `` | `k9-2kr23.u.c.1s272-:751` |
| whatwg vs legacy | `ircsw://5OW:3Ua7KU76091v55J1Z@71-h59w-o:63...` | `71-h59w-o` | `71-h59w-o:63` |
| whatwg vs legacy | `ventriloI://3Y63NWUY67C3:3v\n@7j@7Er0。...@50|...` | `` | `7er0.59z85j18m:50` |
| whatwg vs legacy | `http://77oPR6l2e3146R7wX1u:nw75@-g.2pEcNOEPp42q0Tf.:9120...` | `` | `-g.2pecnoepp42q0tf.:9120` |
| whatwg vs deno | `data://TmOQOA6nx21Uyv8rx8E...@tZ7:3...` | `` | `tZ7` |
| whatwg vs deno | `ms-visio://...@1---d:3...` | `` | `1---d` |
| whatwg vs legacy | `ws://00v069
}{A37689VA3@06'"StN7ld4v8.379l1|938#g` | `` | `06` |
| whatwg vs legacy | `http://tB9maq36Xi3W0@93.59.72.404v𥖜&󢀀J@2mX0R2'5(023p?=66a2DgM` | `2mx0r2'5(023p` | `2mx0r2` |
| whatwg vs legacy | `wss://5j99330G>kH":<𦳨⚖↜ა_lE ?𥔁2l?
3{5Z2p` | `5j99330g` | `` |
| whatwg vs legacy | `ventriloI://3Y63NWUY67C3:3v
@7j@7Er0。z85j18m:50` | `` | `7er0.59z85j18m:50` |
| whatwg vs legacy | `redissNpalmfm://0'.茸⋡0^\%/121@[6:e:c9:bB:3:80:b3:6b]:2348󚃌	+yA81Y*9l90gP8004{T?#{^nsGu` | `` | `0` |
| whatwg vs legacy | `Ktoolms-settings-...://Keꇣ䩤x42@e5@Q.D	:346󜤳.
@Q133Jx3~(R5De'4M3dE?#` | `%15Q133Jx3~(R5De'4M3dE` | `` |
| whatwg vs legacy | `https://p c637a.:66898D8="037OOX(7244n35?#` | `` | `p` |
| whatwg vs legacy | `data://o421p1>
8k50HN27@[69:28:cA:C:5a:0c:2:f]0oٷ𡳬𨣜(@6w0U03?#AP` | `6w0U03` | `6w0u03` |
| whatwg vs legacy | `file://085X᥸󢲬 pKi4@W9I579-60L-S99j:64
𐴌感󧗄x5FH~z3qu7UD.0t@G?#9Ea1` | `` | `g` |
| whatwg vs legacy | `file://2:k26sQ2jJc4522@xn---a	6-e966c..138830o0insq7ays9q0far?#` | `` | `xn---a6-e966c..138830o0insq7ays9q0far` |
| whatwg vs legacy | `http://lKez9 6Dcv35wpcH3@XV.:068%󠀁* ᭞򡃘Sd4(# 43YD5wh]yco'907_2zJ?#` | `xv.:068` | `` |
| whatwg vs deno | `wss://p875ṙP|
󣓞7o4@479.za.88-64-bt.xn--673,x7f-c325c?#` | `479.za.88-64-bt.xn--673,x7f-c325c` | `` |
| whatwg vs deno | `data://TmOQOA6nx21Uyv8rx8E𠃜	󩣣L𐲹󢁱AR@tZ7:3\8o9_51H3c699SBw61E#` | `` | `tZ7` |
| whatwg vs deno | `im://603M98,!so5u3@648.iRL7jv-41d93q5u:85\l6wRL3{1+09o7XT18$?#` | `` | `648.iRL7jv-41d93q5u` |
| whatwg vs deno | `ms-visio://9Zj5r9D116l93s9R7R0"ᶹ1<-
G-𢲬ᅓBXx@1---d:3\VrCMlD302jYIX8o3i4#` | `` | `1---d` |
| whatwg vs deno | `fle://f5Fx3Z8L1@-S9gK:798\f3-X5WV}_XMAi*0{0?#𤏿d𣷥` | `` | `-S9gK` |
| whatwg vs deno | `bitcointsteam://3c85x8M52uMy@37p.o0:8666\7gZ$N?#*` | `` | `37p.o0` |
