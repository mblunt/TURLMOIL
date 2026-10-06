# Userinfo Bleeding into Host

**Description:** The userinfo (username/password) portion bleeds into the host field because the @ sign is not parsed as a userinfo/host delimiter.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs javascript-parse-uri | `http://DQA2d00o4G@󬃣ῤ+󠒰✓,`𐳬𤵚𐸴󠅠򢃦婳	� h@:21f #` | `` | `󬃣ῤ+󠒰✓,`𐳬𤵚𐸴󠅠򢃦婳	� h@` |
| whatwg vs javascript-parse-uri | `ftp://3*@8󥗅YJ@1]p
둈𠈕𐳝]󤕄˩󠂶粞xSJ3s{3pYp3181y}m1i?
#ASE91bL)` | `` | `8󥗅YJ@1]p
둈𠈕𐳝]󤕄˩󠂶粞xSJ3s{3pYp3181y}m1i` |
| whatwg vs javascript-parse-uri | `ws://00v069
}𛳌{A37689VA3@06'"StN7ld4v8.379l1|938#g` | `` | `06'"StN7ld4v8.379l1|938` |
| whatwg vs javascript-parse-uri | `http://tB9maq36Xi3W0@93.59.72.404v𥖜&󢀀J@2mX0R2'5(023p?=66a2DgM` | `93.59.72.404v𥖜&󢀀J@2mX0R2'5(023p` | `2mx0r2'5(023p` |
| whatwg vs javascript-url-parse | `http://DQA2d00o4G@󬃣ῤ+󠒰✓,`𐳬𤵚𐸴󠅠򢃦婳	� h@:21f #` | `` | `:21f ` |
| whatwg vs javascript-url-parse | `http://3KHrM77A48u93Oi4	289oWUAN96	]\᾽Ҋ𠣐
]!8󡼷󧇅>9Q:252℃7E%󯴊U058681sy4P8Y79R6|T?#` | `` | `3khrm77a48u93oi4289owuan96]` |
| javascript-whatwg vs javascript-legacy | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b` |
| javascript-whatwg vs javascript-legacy | `http://tB9maq36Xi3W0@93.59.72.404v@2mX0R2'5(023p?=66a2DgM` | `2mx0r2'5(023p` | `2mx0r2` |
| javascript-whatwg vs javascript-uri-js | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,%09b%7D391752316e5zvx99m` |
| whatwg vs parse-url | `https://1MZ1T@7.6.20.4:01dQ186WXb15ayMuy626a#` | `` | `1MZ1T@7.6.20.4` |
| whatwg vs parse-url | `https://he135W2M4Zl7UG27WGn3tF53yjQA9IiSkw9@57.52.8.6:2840r8xM#` | `` | `he135W2M4Zl7UG27WGn3tF53yjQA9IiSkw9@57.52.8.6` |
| whatwg vs parse-url | `http://IcQq283el796K79unK2qc@89.8.2.84:89l17iayMY380F95Qfv9` | `` | `IcQq283el796K79unK2qc@89.8.2.84` |
| whatwg vs parse-url | `http://FM38474AbQC7q@16.56.16.80:7165Epe#45613!8D49h0Jb` | `` | `FM38474AbQC7q@16.56.16.80` |
| whatwg vs parse-url | `http://jIc119fSma@2hZ-65Yo4:E.73Ep54#7?#` | `` | `jIc119fSma@2hZ-65Yo4` |
| whatwg vs parse-url | `https://4AD16.ux@98.34.84.53:2k3#S4?#` | `` | `4AD16.ux@98.34.84.53` |
| whatwg vs parse-url | `http://q9t0XgJb6f3IC@vn-0e434h---766u:0659r6419a2WI9eI6279#` | `` | `q9t0XgJb6f3IC@vn-0e434h---766u` |
| whatwg vs parse-url | `http://J47CJ5@RJP0-378w2Dzc47..ow:65MOC1J8Wd91KcV461i8#` | `` | `J47CJ5@RJP0-378w2Dzc47..ow` |
| whatwg vs parse-url | `https://2b9ZMT@5389S63-P4l5.:79KM43E5KP#` | `` | `2b9ZMT@5389S63-P4l5.` |
| whatwg vs parse-url | `http://65PGIf8G0DYQ46@27.71.2.3:76S0Lb5656WM46D7#` | `` | `65PGIf8G0DYQ46@27.71.2.3` |
| whatwg vs uri-parser | `wss://yNk4103A?@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `ynk4103a` | `0.05.46.81` |
| whatwg vs uri-parser | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?5#` | `vQ931tsj0` | `-7zZ54` |
| whatwg vs uri-parser | `beshare://2406TUm7F68SmK2m3a/...Q@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `[4d` |
| whatwg vs uri-parser | `ws://hrl49V3Q50/...@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250C58?#` | `hrl49v3q50` | `H4t𠫩𩎡@xvk.K-.M.5..96U37-N` |
| whatwg vs crystal-uri | `data://o421p1>8k50HN27@[69:28:cA:C:5a:0c:2:f]0o޷𒩔𘃜1(v^k1vY4q4h@6w0U03?#AP` | `6w0U03` | `[69:28:cA:C:5a:0c:2:f]0o޷𒩔𘃜1(v^k1vY4q4h@6w0U03` |
| whatwg vs crystal-uri | `http://tB9maq36Xi3W0@93.59.72.404v񗂠&󢏀J@2mX0R2'5(023p?=66a2DgM` | `93.59.72.404v񗂠&󢏀J@2mX0R2'5(023p` | `2mx0r2'5(023p` |
| whatwg vs csharp-systemuri | `data://o421p1>8k50HN27@[69:28:cA:C:5a:0c:2:f]0o޷𒩔𘃜1(v^k1vY4q4h@6w0U03?#AP` | `6w0U03` | `[69:28:ca:c:5a:c:2:f]` |
| javascript-legacy vs javascript-jsuri | `wss://yNk4103A?𮖸ə@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `0.05.46.81` |
| javascript-legacy vs javascript-jsuri | `ws://00v069}@06'"StN7ld4v8.379l1|938#g` | `06'"StN7ld4v8.379l1｜938` | `06` |
| javascript-legacy vs javascript-jsuri | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⪱3365-KNi+*e!cI/...` | `http` | `9
⪱3365-Ｋni+*e!cI` |
| elixir-uri vs elixir-ex_url | `go://5j7TF3XR
zXR@2203o/../A2CqL?#` | `5j7TF3XR` | `` |
| rust-url vs rust-urlparse | `http://DQA2d00o4G@+@:21f #` | `Ḥ+ΧϿι` | `` |
| rust-url vs rust-urlparse | `ws://00v069}@06'"StN7ld4v8.379l1|938#g` | `06'"stn7ld4v8.379l1|938` | `` |
| rust-urlparse vs rust-url | `http://tB9maq36Xi3W0@93.59.72.404v@2mX0R2'5(023p?=66a2DgM` | `93.59.72.404v噗&J@2mx0r2'5(023p` | `2mx0r2'5(023p` | <--- Reparsing bug potential
| erlang-uri-string vs erlang-hackney-url | `go://5j7TF3XR
@2203o20O/../A2CqL?#` | `` | `5j7TF3XR` |
| erlang-uri-string vs erlang-hackney-url | `ws://00v069}@06'"StN7ld4v8.379l1|938#g` | `06'"StN7ld4v8.379l1|938` | `` |
| erlang-uri-string vs erlang-hackney-url | `ftp://3*@8YJ@1]p...?#ASE91bL)` | `` | `1]p
꺈𝓕𠺕𯊠]˩6簞硓xSJ3s{3pYp3181y}m1i` |
| python-uritools vs python-hyperlink | `http://12q*:=*3k@Ŋ:3997264334@,A@YA]k3F0I4180158a5?#n05` | `YA]k3F0I4180158a5` | `` |
| python-uritools vs python-hyperlink | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `2mX0R2'5(023p` | `` |
| python-uritools vs python-hyperlink | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5@1JLw5x?#` | `1JLw5x` | `` |
| go-net vs java-okhttp | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `2mx0r2'5(023p` | `` |
| java-uri vs java-galimatias | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `2mx0r2'5(023p` | `` |
| go-net vs java-okhttp | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5@1JLw5x?#` | `1jlw5x` | `` |
| php-pecl-http vs php-pear-net-url2 | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `2mX0R2'5(023p` | `2mx0r2'5(023p` |
| perl-uri vs perl-mojo | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `` | `2mX0R2'5(023p` |
| kotlin-ktor vs java-okhttp3 | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `2mX0R2'5(023p` | `93.59.72.404v噗&J@2mX0R2'5(023p` |
| javascript-whatwg vs javascript-parse-uri | `http://558:767332:@Ug0pl866281hd.Mj7-N𝳧᱉⑳?#k` | `558` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` |
| javascript-whatwg vs javascript-parse-uri | `http://tB9maq36Xi3W0@93.59.72.404v噗&J@2mX0R2'5(023p?=66a2DgM` | `93.59.72.404v噗&J@2mX0R2'5(023p` | `2mx0r2'5(023p` |
| javascript-whatwg vs javascript-urijs | `http://12q*:=*3k@Ŋ:3997264334@,A@YA]k3F0I4180158a5?#n05` | `` | `YA]k3F0I4180158a5` |
| javascript-whatwg vs javascript-urijs | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4X.w04,B}391752316e5ZVx99M` |
| javascript-whatwg vs javascript-parse-url | `https://1MZ1T@7.6.20.4:01dQ186WXb15ayMuy626a#` | `` | `1MZ1T@7.6.20.4` |
