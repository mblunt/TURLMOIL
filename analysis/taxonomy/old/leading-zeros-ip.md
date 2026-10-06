# Leading Zeros in IP Octets

**Description:** Leading zeros in IPv4 octets are treated as octal by some parsers and rejected or normalized differently by others

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-url | `jabber://0156J7,-6bsU@31.07.67.02:006484\1=4l;7358z0X23QE?#` | `` | `31.07.67.02` |
| javascript-whatwg vs rust-url | `ymsgr://599I3d57S7DXd1:4@0.10.85.43:0486\󺫓��W)⩂􀿨#􁅂?*nf22k41999121*121;?#` | `` | `0.10.85.43` |
| whatwg vs legacy | `ftp://Kds2CYszhi8H67d...@08.61.1.95:76?#` | `` | `08.61.1.95:76` |
| whatwg vs legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88...` | `99.01.1.20:88` | `` |
| whatwg vs deno | `jabber://0156J7,-6bsU@31.07.67.02:006484...` | `` | `31.07.67.02` |
| whatwg vs deno | `data://...@0.10.85.43:0486...` | `` | `0.10.85.43` |
| whatwg vs smithy | `http://1109T8j9L283wR:Q4b3S@-08V.T-1.e1u6XP5-u2:2...` | `` | `-08v.t-1.e1u6xp5-u2` |
| whatwg vs smithy | `data://465...@4:340...` | `` | `4` |
| whatwg vs javascript-fast-url-parser | `ftp://Kds2CYszhi8H67d��Qtjf@08.61.1.95:76?#` | `` | `08.61.1.95` |
| whatwg vs javascript-fast-url-parser | `wss://x2xx0Z5yjQle3@0.5:4905~󡳐7783O2GU9KY58716T2"?#!` | `` | `0.5` |
| whatwg vs java-okhttp | `http://2022Y0
0676.53.14.76:54?#ᡚ` | `` | `2022y0` |
| whatwg vs java-okhttp | `https://JxUSvT@99.93.4.62:22F56...@00?"U` | `0.0.0.0` | `00` |
| python-httpx vs python-rfc3986 | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| python-uritools vs python-hyperlink | `https://JxUS@99.93.4.62:22F56...@00?"U` | `` | `00` |
| ruby-addressable vs ruby-uri | `https://JxUS@99.93.4.62:22F56...@00?"U` | `` | `0.0.0.0` |
| ruby-addressable vs ruby-uri | `ftp://012Vj@0...?#` | `` | `0` |
| ruby-addressable vs ruby-uri | `http://5n	f@29.00.6.78(97217)...?#` | `29.00.6.xn--78(97217)4whxc-bv1k41vgn82z` | `` |
| rust-url vs rust-http | `data://a08Azc@[F8:E1:d:06:B:B:08:67]:6120?#B` | `[F8:E1:d:06:B:B:08:67]` | `[f8:e1:d:6:b:b:8:67]` |
| rust-url vs rust-http | `ftp://a89pPVmz6J0@[A:08:e:5:F:fC:AA:fF]:4?#` | `[a:8:e:5:f:fc:aa:ff]` | `[A:08:e:5:F:fC:AA:fF]` |
| node-whatwg vs php-league | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `` |
| java-jdk-uri vs java-spring-mvc | `ws://3SEC8ar3W@99.01.1.20:88 E9?/...#I2` | `` | `99.01.1.20` |
| perl-uri vs perl-mojo | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `` |
| perl-uri vs perl-mojo | `ws://3SEC8ar3W@99.01.1.20:88 E9?/...#I2` | `99.01.1.20` | `` |
| perl-uri vs perl-mojo | `https://JxUS@99.93.4.62:22F56...@00?"U` | `00` | `` |
| r-httr vs r-curl | `https://JxUS@99.93.4.62:22F56...@00?"U` | `00` | `` |
| python-stdlib vs python-whatwg | `https://JxUS@99.93.4.62:22F56...@00?"U` | `00` | `99.93.4.62:22F56...@00` |
| scala-play vs elixir-uri | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `` |
| scala-play vs elixir-uri | `ws://3SEC8ar3W@99.01.1.20:88 E9?/...#I2` | `99.01.1.20` | `` |
| javascript-whatwg vs javascript-urijs | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-whatwg vs javascript-url-parse | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-whatwg vs javascript-fast-url-parser | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-whatwg vs javascript-fast-url-parser | `jabber://0156J7,-6bsU@31.07.67.02:006484\?#` | `` | `31.07.67.02` |
| javascript-whatwg vs javascript-parseuri | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-whatwg vs javascript-jsuri | `wss://yNk4103A?@0.05.46.81:592152?#` | `ynk4103a` | `0.05.46.81` |
| javascript-whatwg vs ada-uri-mime | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-whatwg vs ada-uri-mime | `wss://yNk4103A?@0.05.46.81:592152?#` | `` | `ynk4103a` |
| javascript-whatwg vs rust-url | `jabber://0156J7,-6bsU@31.07.67.02:006484?#` | `` | `31.07.67.02` |
| javascript-whatwg vs rust-url | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| rust-url vs rust-uriparse | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| csharp-systemuri vs python-urllib3 | `ftp://T1b8k1D0@84｡04.61.80:5449?#` | `` | `84｡04.61.80` |
| csharp-systemuri vs python-urllib3 | `jabber://0156J7@31.07.67.02:006484?#` | `` | `31.07.67.02` |
| csharp-systemuri vs python-urllib3 | `telnet://Z4Ḝ4E/../6111D44@00⋬?#` | `` | `00⋬` |
| whatwg vs python-urllib3 | `https://JxUSvT@99.93.4.62:22F56@00?"U` | `0.0.0.0` | `00` |
| whatwg vs python-urllib3 | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| go-net vs elixir-uri | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `` |
| go-net vs elixir-uri | `https://JxUSvT@99.93.4.62:22@00?U` | `00` | `` |
| whatwg vs python-urllib3 | `jabber://0156J7@31.07.67.02:006484?#` | `` | `31.07.67.02` |
| rust-uriparse vs python-urllib3 | `jabber://0156J7@31.07.67.02:006484?#` | `` | `31.07.67.02` |
| rust-url vs python-urllib3 | `jabber://0156J7@31.07.67.02:006484?#` | `` | `31.07.67.02` |
| whatwg vs go-net | `bolo://0ⳳ3@0𪳓1e65.4.17.3:770?#` | `0𪳓1e65.4.17.3` | `` |
