# Query percent-encoding

**Description:** One parser percent-encodes query while other uses raw unicode or different encoding

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|

| whatwg vs parse_uri | `http://3H35MD6E3O59lR61743:9@7。。67.88.221ɲ𪧕?46⟼ oX77#I@o57` | `?46%E2%9F%BCoX77` | `?.%F3%AC%81%8D\` |



| whatwg vs posix | `wss://yNk4103A?󽦠m\ud898�⪷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?󽦠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?` |
| whatwg vs posix | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o񇚙xg*6}::'25Ny`K934𦭥ꩫ8jt9@00?` | `?%22U%E4%97%AA` | `?"U䗪` |
| whatwg vs posix | `lastfm://vQ931tsj0/../dhqo񾏾914crJ@-7zZ54:827` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5` | `?5���82J38vx94MhO3P6~2P5` |
| whatwg vs posix | `http://tB9maq36Xi3W0@93.59.72.404v��&𛋀J@2mX0R2'5(023p?` | `?=66%0Ca2DgM` | `?=66a2DgM` |
| whatwg vs node-url | `wss://yNk4103A?��m%5C��⪷ᵨ@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?#` | `?𩵱�𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` | `?��m%5C��⪷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` |
| whatwg vs node-url | `https://JxUS𣰸3vT⭇@99.93.4.62:22F56^<o��xg*6}::'25Ny`K934𖢵󎂧說8jt9@00?•U��` | `?•U%E4%97%AA` | `?•U��` |
| whatwg vs go | `wss://yNk4103A?񾤰8m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?񾤰8m%5C𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` |
| whatwg vs go | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `%22U䗪` |
| whatwg vs go | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?C|򷫉=;%2񨕶򝚚򯋟䁑JC3gO32V12o3k1334w!?#3]<7` | `?C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?` | `?C%7C򷫉=;%2񨕶򝚚򯋟䁑JC3gO32V12o3k1334w!?` |
| whatwg vs go | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?𡮫D?0~􏳢5#-,%31{` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25` | `?𡮫D?0~􏳢5` |
| whatwg vs legacy | `wss://yNk4103A?􃦉m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?􃦉m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?` |
| whatwg vs legacy | `https://JxUS⏸vT⭇@99.93.4.62:22F56^<o􃓉xg*6}::'25Ny`K934𦭥򺲧身8jt9@00?"U䗪` | `?"%22U%E4%97%AA|%22U䗪` | `?"%22U䗪` |
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqo󶢿914crJ@-7zZ54:827
?5󾢯Ἄ82J38vx94MhO3P6~2P5#` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5` | `?5󾢯Ἄ82J38vx94MhO3P6~2P5` |
| whatwg vs legacy | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?C|��=;%2󺥶󻖚��䁑JC3gO32V12o3k1334w!?#3]<7` | `?C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?` | `?C%7C��=;%2󺥶󻖚��䁑JC3gO32V12o3k1334w!?` |
| whatwg vs legacy | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?☉��?0~􏗲#-,%31{` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25` | `?☉��?0~􏗲` |
| whatwg vs legacy | `http://tB9maq36Xi3W0@93.59.72.404v䙜&􌳰J@2mX0R2'5(023p?=66a2DgM` | `?=66%0Ca2DgM` | `?=66a2DgM` |
| whatwg vs legacy | `http://ftp://3Z28󻃄♕801554jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>�ꂥ⬤󻵇�ꎵSu(6t25J0iwxw21j30]?♷#"_0Z3` | `?%E2%99%B7` | `?♷` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `?1?%F3%AC%B5%8B4?&1?%F3%AC%B5%8B4?` | `?1?󬵋4?&1?󬵋4?` |
| whatwg vs legacy | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2繶洶377723lG8J6O0u)!82?#` | `?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2%E7%B8%B46377723lG8J6O0u)!82?` | `?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2繶洶377723lG8J6O0u)!82?` |
| whatwg vs legacy | `wss://yNk4103A?󾢠m\��⪷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?󾢠m%5C��⪷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` |
| whatwg vs legacy | `https://JxUS�vT⭇@99.93.4.62:22F56^<o􋶩xg*6}::'25Ny`K934𝥭ꛧ8jt9@00?"U􃒢` | `?"%22U%E4%97%AA|%22U􃒢` | `%22U􃒢` |
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqo􌎟914crJ@-7zZ54:827
?5􃢯Ἄ82J38vx94MhO3P6~2P5#` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5` | `5􃢯Ἄ82J38vx94MhO3P6~2P5` |
| whatwg vs legacy | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?C|��L=;%2��􌓚􌣚􌢯��фJC3gO32V12o3k1334w!?#3]<7` | `?C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?` | `C%7C��=;%2��􌓚􌣚􌢯��фJC3gO32V12o3k1334w!?` |
| whatwg vs legacy | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?☉􂲟􃲲%0D5#-,%31{` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25` | `?􂢖�D?0~􃲲%0D5` |
| whatwg vs legacy | `http://tB9maq36Xi3W0@93.59.72.404v󻒜&􍃰J@2mX0R2'5(023p?=66a2DgM
` | `?=66%0Ca2DgM` | `=66a2DgM` |
| legacy (2) vs radix (3) | `󶳠m%5C𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?|` | `?|` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?|` |
| legacy (2) vs radix (3) | `%22U䗪|` | `%22U䗪|` | `%22U%E4%97%AA|` |
| legacy (2) vs radix (3) | `5􎯠Ὄ82J38vx94MhO3P6~2P5|` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5|` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5|` |
| legacy (2) vs radix (3) | `C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?|` | `C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?|` | `C%7C%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?|` |
| legacy (2) vs radix (3) | `%F2%89%AE%ABD?0~%F4%8F%B3%A25|` | `%F2%89%AE%ABD?0~%F4%8F%B3%A25|` | `%F2%89%AE%ABD?0~%F4%8F%B3%A25|` |
| legacy (2) vs radix (3) | `%0E%09o%30%33?` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25|` | `%F2%89%AE%ABD?0~%F4%8F%B3%A25|` |
| radix (3) vs whatwg (4) | `https://JxUSসvT⭇@99.93.4.62:22F56^<o��xg*6}::'25Ny`K934��ꫧ8jt9@00?"U跪` | `?"U%E4%97%AA` | `?"U跪` |
| radix (3) vs whatwg (4) | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30z�<
	o%30%33?���~��5#-,%31{` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25` | `?���D?0~�5` |
| radix (3) vs whatwg (4) | `wss://https://9V6a7pCDDCf㲍ο?\  ��ஆ+Bf.-2.--93jM3iBE.:3061��sT I_8F7V_021T46aK7=?` | `?\  ��ஆ+Bf.-2.--93jM3iBE.:3061��sT I_8F7V_021T46aK7=?` | `?\  ��ஆ+Bf.-2.--93jM3iBE.:3061��sT I_8F7V_021T46aK7=?` |
| radix (3) vs whatwg (4) | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2��6377723lG8J6O0u)!82?#` | `?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2%E7%B8%B46377723lG8J6O0u)!82?` | `?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2��6377723lG8J6O0u)!82?` |
| radix (3) vs whatwg (4) | `data://fzqjL?╃u7@637d5.a-wBj.:1l1Z
О1?#` | `?%0C%E2%A5%83u7@637d5.a-wBj.:1l1Z%0F%E2%93%9E1?` | `?╃u7@637d5.a-wBj.:1l1Z
О1?` |


| legacy vs ada | `wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?|wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%7BL77d39G46i91QBSN424` |
| legacy vs ada | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `?1?󬵋4?&1?󬵋4?` | `?1?%F3%AC%B5%8B4?&1?%F3%AC%B5%8B4?` |
| legacy vs ada | `http://jn7Lq懏0?􋍎7^32	@󹕔
⊧@。93-D。CEsHZE2Ko2v:򥜰𨔵𩋇\v)핦_𫁾	}缣9󳷕?⎫39R0TCc2d?am􀙰
貀#` | `?⎫39R0TCc2d?am􀙰\n貀` | `?%02%E2%8E%AB39R0TCc2d?am%F4%80%99%B0%E8%B2%80` |
| legacy (1) vs ada (2) | `wss://yNk4103A?𞾠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?𞾠m%5C𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` |
| legacy (1) vs ada (2) | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o̾9xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA|%22U䗪` | `|%22U䗪` |
| legacy (1) vs ada (2) | `lastfm://vQ931tsj0/../dhqo𖬟914crJ@-7zZ54:827
?5홏�ὄ` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5` | `?5홏�ὄ82J38vx94MhO3P6~2P5` |
| ada (2) vs net (3) | `wss://yNk4103A?𞾠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `𞾠m%5C𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` |
| ada (2) vs net (3) | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o̾9xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `%22U䗪` | `?%22U%E4%97%AA` |
| legacy vs ada | `wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `?%F3%B6%B3%A0%01%19m\%F0%A5%A8%87%E2%A8%B7%E1%B5%A8@0.05.46.81:5921521228%0C0{%0EL77d39G46i91QBSN424?` | `?󶳠m%5C𥨇⨷ᵨ@0.05.46.81:59215212280%7BL77d39G46i91QBSN424?` |
| legacy vs ada | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `%22U䗪` |
| legacy vs ada | `lastfm://vQ931tsj0/../dhqo􆸟914crJ@-7zZ54:827?5􎯠Ὄ82J38vx94MhO3P6~2P5#` | `?5%F4%8E%AF%A0%E1%BD%8C82J38vx94MhO3P6~2P5` | `5􎯠Ὄ82J38vx94MhO3P6~2P5` |
| legacy vs ada | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?C|󷫉=;%2񨕶򝚚򯋟䁑JC3gO32V12o3k1334w!?#3]<7` | `?C%13%EE%9C%85|%F2%B7%AB%89=;%2%F1%A8%95%B6%F2%9D%9A%9A%F2%AF%8B%9F%E4%81%91JC3gO32V12o3k1334w!?` | `C%7C󷫉=;%2񨕶򝚚򯋟䁑JC3gO32V12o3k1334w!?` |
| legacy vs ada | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<%0E%09o%30%33?󉮫D?0~􏳢5#-,%31{` | `?%F2%89%AE%ABD?0~%F4%8F%B3%A25` | `󉮫D?0~􏳢5` |
