# Host Case Folding

**Description:** Host is lowercased by one parser but returned in original mixed/upper case by another

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-hyper-uri | `http://Sh7/��qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `sh7` | `Sh7` |
| javascript-whatwg vs rust-hyper-uri | `file://a9HC5V03i92S3b9z330/..G⪬#𪗙$rI3a714Q󹡐;ʂ5#YS4P ?#` | `a9hc5v03i92s3b9z330` | `a9HC5V03i92S3b9z330` |
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqo...` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs legacy | `beshare://2406TUm7F68SmK2m3a/...Q...` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs legacy | `onenote://...@3324G845648oko2d9s8J?` | `%043324G845648oko2d9s8J` | `3324g845648oko2d9s8j` |
| whatwg vs legacy | `onenote://...@1j36y_82.Fv#` | `1j36y_82.Fv` | `1j36y_82.fv` |
| whatwg vs deno | `wss://yNk4103A?...` | `ynk4103a` | `yNk4103A` |
| whatwg vs deno | `ws://hrl49V3Q50/...` | `hrl49V3Q50` | `hrl49v3q50` |
| whatwg vs uri-js | `lastfm://vQ931tsj0/...` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs uri-js | `beshare://2406TUm7F68SmK2m3a/...` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs smithy | `wss://yNk4103A?...` | `ynk4103a` | `yNk4103A` |
| whatwg vs parse-uri | `wss://yNk4103A?...` | `ynk4103a` | `yNk4103A` |
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqoࠜ914crJ@-7zZ54:827
?5༢Ṅ΄4J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs legacy | `beshare://2406TUm7F68SmK2m3a/...Q➔I￿fffM@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ?1?` | `5gHx.3n2u6P4401.-7l` | `5ghx.3n2u6p4401.-7l:048` |
| whatwg vs legacy | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2纴6377723lG8J6O0u)!82?#` | `0pH.` | `0ph.` |
| whatwg vs legacy | `data://787: ᣸3F1@f:3151c34\lj45L@U1D=y!c9A/.W#8 – onenote://...@3324G845648oko2d9s8J` | `6w0U03` | `6w0u03` |
| whatwg vs legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs legacy | `acap://05筊P@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV?#` | `i4oh44ho008i3fosf.13010z1)av50l7txfuz213lv` | `I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` |
| whatwg vs legacy | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~🧻e,0i2IX@1j36y_82.Fv#` | `1j36y_82.Fv` | `1j36y_82.fv` |
| whatwg vs javascript-parse-uri | `wss://yNk4103A?󦳠m\𥨇⦷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `ynk4103a` | `yNk4103A` |
| whatwg vs javascript-parse-uri | `ws://hrl49V3Q50/...8f77gTbO:
5T@H4t𠓩𡴡@xvk.K-.M.5..96U37-N:3250⪼
C58?#` | `hrl49V3Q50` | `hrl49v3q50` |
| whatwg vs javascript-parse-uri | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4X.w04,	B}391752316e5ZVx99M` |
| whatwg vs javascript-uri-js | `lastfm://vQ931tsj0/../dhqo��914crJ@-7zZ54:827
?5𐿠ἄ΂J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs javascript-uri-js | `beshare://2406TUm7F68SmK2m3a/...Q➴I󯃿M@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs javascript-uri-js | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,%09b%7D391752316e5zvx99m` |
| whatwg vs javascript-urijs | `wss://yNk4103A?󦓠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `ynk4103a` |
| whatwg vs javascript-urijs | `ws://do2ycs037T󨃢s3k@1𦋒3⦷8y5/./(28KZ3tq83U3y3lg?#󣣱` | `xn--138y5-2x5cz9190b` | `1𦋒3⦷8y5` |
| whatwg vs javascript-urijs | `wss://0vKeJx114448R6I7VM0	@	:5993	975wc50d10JgS895j{7V?#` | `` | `:5993	975wc50d10jgs895j{7v` |
| javascript-whatwg vs javascript-legacy | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?5...#` | `vQ931tsj0` | `vq931tsj0` |
| javascript-whatwg vs javascript-legacy | `beshare://2406TUm7F68SmK2m3a/...@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| javascript-whatwg vs javascript-legacy | `acap://05@I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV?` | `i4oh44ho008i3fosf.13010z1)av50l7txfuz213lv` | `I4Oh44Ho008I3fOsF.13010z1)av50L7TXFuZ213LV` |
| javascript-whatwg vs javascript-legacy | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b` |
| javascript-whatwg vs javascript-legacy | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33@1j36y_82.Fv#` | `1j36y_82.fv` | `1j36y_82.Fv` |
| javascript-whatwg vs javascript-legacy | `onenote://Dau2OPU1@3324G845648oko2d9s8J?#wy` | `%043324g845648oko2d9s8j` | `3324g845648oko2d9s8j` |
| javascript-whatwg vs javascript-smithy | `https://RJB3/...rR2V4q78myX1h87?@.:289?` | `` | `rjb3` |
| javascript-whatwg vs javascript-smithy | `ms-browser-extension://978311?@[43:74:3:c0:75:a:d5:C]:6639?` | `` | `978311` |
| javascript-whatwg vs javascript-smithy | `wss://86r7vfbIfERe3j8?@hUH-1Q95Y9T:9738?` | `` | `86r7vfbifere3j8` |
| whatwg vs legacy | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?5Ὄ82J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs legacy | `beshare://2406TUm7F68SmK2m3a/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs legacy | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~𯞻e,0i2IX@1j36y_82.Fv#` | `1j36y_82.Fv` | `1j36y_82.fv` |
| whatwg vs parse-uri | `wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `ynk4103a` | `yNk4103A` |
| whatwg vs parse-uri | `ws://hrl49V3Q50/...8f77gTbO:5T@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250⪼C58?#` | `hrl49V3Q50` | `hrl49v3q50` |
| whatwg vs legacy | `ws://6w0U03?#AP` | `6w0U03` | `6w0u03` |
| whatwg vs uri-js | `beshare://2406TUm7F68SmK2m3a/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs uri-js | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?5Ὄ82J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs url-parse | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?5Ὄ82J38vx94MhO3P6~2P5#` | `vQ931tsj0` | `vq931tsj0` |
| whatwg vs url-parse | `beshare://2406TUm7F68SmK2m3a/...Q@[4d:2A:81:f:1:A:b6:C0]:727?` | `2406TUm7F68SmK2m3a` | `2406tum7f68smk2m3a` |
| whatwg vs urijs | `wss://yNk4103A?@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `ynk4103a` |
| whatwg vs urijs | `ws://hrl49V3Q50/...@xvk.K-.M.5..96U37-N:3250C58?#` | `hrl49v3q50` | `hrl49V3Q50` |
