# Percent Encoding

**Description:** Parsers differ on whether path characters are percent-encoded or left as raw Unicode/bytes, or whether existing percent-encoded sequences are decoded.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|
| javascript-whatwg vs javascript-url-parse | `soldatpwid://.../4Ku21984jdGvl51unc0x3z@-5V0w29:860#` | `/4Ku21984jdGvl51unc0%F0%A4%84%983z@-5V0w29:860` | `/4Ku21984jdGvl51unc0x3z@-5V0w29:860` |
| javascript-whatwg vs javascript-url-parse | `dnsm8t:Y@x1xqh@abc:Z3r6b0~8w{3GB65G+06}?#` | `Y@%F0%A0%94%A01%F0%A3%88%BEqh%F0%90%AC%88z:Z3r6b0~8w{3GB65G+06}` | `Y@x1xqhz:Z3r6b0~8w{3GB65G+06}` |
| javascript-whatwg vs javascript-urijs | `beshare://2406TUm7F68SmK2m3a/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727` |
| javascript-whatwg vs javascript-url-parse | `https://ftp://1R43cy/x[ca:d:b:6:D6:b3:0:c]xyz661abc#u7` | `//1R43cy/x[ca:d:b:6:D6:b3:0:c]%F3%B5%94%A7661%F3%B0%BE%BD` | `//1R43cy/x[ca:d:b:6:D6:b3:0:c]xyz661abc` |
| javascript-whatwg vs javascript-urijs | `wss://https://9V6a7pCDDCfx@y.z:3061?#` | `//9V6a7pCDDCf%E3%92%8D%CF%BF%11%15` | `//9V6a7pCDDCfx` |
| go-net vs rust-url | `go://3iU361k/.4A8kRx@R8.301BxZ01Pu3g0997:9187K640zk063C89?#` | `/.4A8kRx@R8.301BxZ01Pu3g0997:9187K640zk063C89` | `/.4A8kR%F0%A6%9F%B4%F4%8C%B0%AB8%F3%BA%A0%A9%3Em%E2%84%B1%3Ekly6EL5` |
| go-net vs rust-url | `http://http://YY5G8vqt1pVe4xX0jU4@wZ0.e9h-:5404Jjpk*hF21O+4XS727b6?#` | `//YY5G8vqt1pVe4xX0jU4@wZ0.e9h-:5404Jjpk*hF21O+4XS727b6` | `//YY5G8vqt1pVe4%E2%8D%95X0jU4@wZ0.e9h-:5404Jjpk*hF21O+4XS727b6` |
| csharp-systemuri vs rust-url | `ftp://ftp://4c8j8k2LN2g4gttpz5l	xyz@54.5.3.42:75CdO16?#` | `//4c8j8k2LN2g4gttpz5l%09xyz@54.5.3.42:75CdO16` | `//4c8j8k2LN2g4gttpz5lxyz@54.5.3.42:75CdO16` |
| csharp-systemuri vs rust-url | `jar://70odWU9.66:7AzV33629mAxq3Dn@52.6.7Dm0t6/E3g{^0R4I6?#` | `/E3g%7B%5E0R4I6` | `/E3g%7B^0R4I6` |
| go-net vs rust-url | `wss://wss://3:@xLj.abc:48{0Od12L00s@ib6Oz1R2n?` | `//3:@xLj.abc:48{0Od12L00s@ib6Oz1R2n` | `//3:@%E2%A6%9B%D0%89.%F0%A7%9B%82:48%7B0Od12L00s@ib6Oz1R2n` |
| javascript-uri-js vs javascript-url-parse | `soldatpwid://.../4Ku21984jdGvl51unc0x3z@-5V0w29:860#` | `/4Ku21984jdGvl51unc0x3z@-5V0w29:860` | `/4Ku21984jdGvl51unc0%F0%A4%84%983z@-5V0w29:860` |
| javascript-uri-js vs javascript-url-parse | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| javascript-uri-js vs javascript-url-parse | `https://ftp://1R43cy/x[ca:d:b:6:D6:b3:0:c]xyz661abc#u7` | `//1R43cy/x[ca:d:b:6:D6:b3:0:c]xyz661abc` | `//1R43cy/x[ca:d:b:6:D6:b3:0:c]%F3%B5%94%A7661%F3%B0%BE%BD` |
| javascript-uri-js vs javascript-url-parse | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gx9y87zM?1?2?&1?2?` | `/;14[gx9y87zM` | `/;14[g%D5%869%F0%9D%B2%9887%E2%A2%95M%F3%B0%92%94` |
| csharp-systemuri vs elixir-uri | `beshare://2406TUm7F68SmK2m3a/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727` |
| csharp-systemuri vs elixir-uri | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95%5E50+0j496j]0a415dv1` | `/𦖎qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| csharp-systemuri vs elixir-uri | `ms-settingsthingsms-walk-to://ms-settingsthingsms-walk-to://3k8ᛮ𒠊a@22.6.4.5801珡o8xU340xTrdvfpyZ3|0?#` | `//3k%068%E1%9B%AE%F4%82%98%8Aa@22.6.4.5801%E7%8F%A1o8xU340xTrdvfpyZ3%7C0` | `//3k8ᛮ𒠊a@22.6.4.5801珡o8xU340xTrdvfpyZ3|0` |
| javascript-whatwg vs elixir-uri | `beshare://2406TUm7F68SmK2m3a/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727` |
| javascript-whatwg vs elixir-uri | `http://file://340`xyz@1.75.6:	xy4 ~xyzq(yz8abcz?#` | `//340%60xyz@1.75.6:%09xy4%20~xyzq(yz8abcz` | `//340`xyz@1.75.6:	xy4 ~xyzq(yz8abcz` |
| javascript-legacy vs elixir-uri | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95%5E50+0j496j]0a415dv1` | `/𦖎qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| javascript-legacy vs elixir-uri | `sLopenpgp4fpraFQ7://2W21SCBE@5gHx.3n2u6P4401.-7l:048/;14[gx9y87zM?1?2?&1?2?` | `/;14[g%D5%869%F0%9D%B2%9887%E2%A2%95M%F3%B0%92%94` | `/;14[gx9y87zM` |
| perl-uri vs go-net | `beshare://2406TUm7F68SmK2m3a/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q➴I󿗿M@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@%5B4d:2A:81:f:1:A:b6:C0%5D:727` |
| perl-uri vs go-net | `bolo://0xyz1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `/,{9PwCe@1269J11mwzD+1` | `/,%7B9PwCe@1269J11mwzD+1` |
| perl-uri vs go-net | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95%5E50+0j496j%5D0a415dv1` | `/𦖎qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| cpp-ada-url vs rust-url | `https://https://J:G7	@9.95.9.93:60)?#` | `//J:G7@9.95.9.93:60)` | `//J:G7@9.95.9.93:60)` |
| cpp-ada-url vs rust-url | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95%5E50+0j496j]0a415dv1` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| cpp-ada-url vs rust-url | `jar://70odWU9.66:7AzV33629mAxq3Dn@52.6.7Dm0t6/E3g{^0R4I6?#` | `/E3g%7B^0R4I6` | `/E3g%7B%5E0R4I6` |
| cpp-ada-url vs rust-url | `wss://81rkI3J5/../xyz 氽^=4@o.x1v-P7k:2e^tS8QB00G4^826u(U8?#` | `/%F3%B5%9E%AE%20%E6%B0%BD^=4@o.x1v-P7k:2e^tS8QB00G4^826u(U8` | `/%F3%B5%9E%AE%20%E6%B0%BD%5E=4@o.x1v-P7k:2e%5EtS8QB00G4%5E826u(U8` |
| java-okhttp vs rust-url | `http://Sh7/xqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95%5E50+0j496j]0a415dv1` | `/%F0%A6%A6%8Eqn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1` |
| java-okhttp vs rust-url | `https://4xyz@3.97.6/..34:6xyz	xy2!7Gq^Vn1]:7j4EoXe2l?#` | `/..34:6xyz%0FRxy%E2%A9%982!7Gq%5EVn1]:7j4EoXe2l` | `/..34:6xyz%0FRxy%E2%A9%982!7Gq^Vn1]:7j4EoXe2l` |
| javascript-legacy vs go-net | `bolo://0xyz1e65.4.17.3:77058479/,{9PwCe@1269J11mwzD+1#8` | `/,{9PwCe@1269J11mwzD+1` | `/,%7B9PwCe@1269J11mwzD+1` |
| javascript-legacy vs go-net | `wss://wss://3:@xyz.abc:48{0Od12L00s@ib6Oz1R2n?` | `//3:@xyz.abc:48{0Od12L00s@ib6Oz1R2n` | `//3:@xyz.abc:48%7B0Od12L00s@ib6Oz1R2n` |

