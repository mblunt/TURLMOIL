# Trailing Dot in Host

**Description:** A trailing dot on the hostname is retained by one parser but stripped by another

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `ms-settings-lock://0pH.?...` | `0pH.` | `0ph.` |
| whatwg vs legacy | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e:1478` |
| whatwg vs deno | `http://3H35MD6E3O59lR61743:9@7。67.88.221...` | `7.67.88.xn--2214-2ec87815j` | `` |
| whatwg vs smithy | `wss://.../...` | `` | `...` |
| whatwg vs smithy | `data://.//...` | `` | `.` |
| javascript-whatwg vs javascript-legacy | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2...` | `0ph.` | `0ph.` |
| javascript-whatwg vs javascript-legacy | `http://lKez9 6Dcv35wpcH3@XV.:068%...` | `xv.` | `` |
| javascript-whatwg vs javascript-deno | `ms-settings-lock://0pH.?W2mqD@...` | `` | `.S8-mrt.-0E.6-.Ww2T` |
| javascript-whatwg vs javascript-deno | `itms://K4537u7Si:17zDx56o@ED042W.4d75mMABc:5\?` | `ed042w.4d75mmABc` | `` |
| whatwg vs jsuri | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴6377723lG8J6O0u)!82?` | `` | `0pH.` |
| whatwg vs jsuri | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7` | `` | `.8agD-.64.z64.091.E` |
| whatwg vs jsuri | `http://lKez9 6Dcv35wpcH3@XV.:068%...# 43YD5wh]yco'907_2zJ?` | `xv.` | `` |
| whatwg vs ada-uri-mime | `http://lKez9 6Dcv35wpcH3@XV.:068%...?#` | `xv.` | `` |
| whatwg vs trurl | `http://lKez9 6Dcv35wpcH3@XV.:068%...?#` | `xv.` | `` |
| whatwg vs trurl | `data://S1u68@80.6.66/./.09:...?#gStt` | `80.6.66` | `` |
| javascript-legacy vs javascript-deno | `ms-settings-lock://0pH.?W2mqD...` | `0ph.` | `0pH.` |
| javascript-legacy vs javascript-domurl | `ms-settings-lock://0pH.?W2mqD...` | `` | `0ph.` |
| haskell-network-uri vs haskell-uri-bytestring | `ms-settings-lock://0pH.?W2mqD...` | `0pH.` | `` |
| elixir-uri vs elixir-ex_url | `fPe2...3。+ 6。3E56-N6N9N3510D。a:94...?#` | `fPe20
95iZ3。+ 6。3E56-N6N9N3510D。a` | `` |
| rust-url vs rust-urlparse | `ms-settings-lock://0pH.?W2mqD...` | `` | `` |
| python-urllib3 vs python-yarl | `soldatpwid:///4Ku21984jdGvl51unc...@-5V0w29:860#` | `...` | `` |
| python-urllib3 vs python-yarl | `wss://t21@.../..@.O6z-p08...?W#` | `t21^...` | `` |
| python-httpx vs python-rfc3986 | `soldatpwid://.../4Ku21984jdGvl51unc@-5V0w29:860#` | `...` | `` |
| python-uritools vs python-hyperlink | `ftp://T1b8k1D0@84！04.61.80:5449...?#` | `84！04.61.80:5449🆕Xܚ%[` | `` |
| python-uritools vs python-hyperlink | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `` | `5．90．55.47:177257836qH1OKH` |
| php-pecl-http vs php-pear-net-url2 | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2...` | `` | `0pH.` |
| perl-uri vs perl-mojo | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2...` | `` | `0pH.` |
| r-httr vs r-curl | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2...` | `0ph.` | `0pH` |
| r-httr vs r-curl | `data://./61Y71NE92438...@[D:d:1c:00:a8:3:4D:A]:287?#` | `.` | `` |
| javascript-whatwg vs javascript-legacy | `ms-settings-lock://0pH.?W2mqD...` | `0ph.` | `0ph.` |
| javascript-whatwg vs rust-url | `http://I67326k0st4Ef713WG7ph183@sp957gG..-KPI18.Uk.:628?#` | `` | `sp957gg..-kpi18.uk.` |
| javascript-whatwg vs rust-url | `http://J47CJ5@RJP0-378w2Dzc47..ow:65?#` | `` | `rjp0-378w2dzc47..ow` |
| go-net vs python-urllib3 | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴?#` | `0ph.` | `0pH.` |
| go-net vs python-urllib3 | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴?#` | `0ph.` | `0pH.` |
| elixir-uri vs python-urllib3 | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴?#` | `0ph.` | `0pH.` |
| elixir-uri vs python-urllib3 | `https://11139j078uW1j8.-4A:83563?#` | `` | `11139j078uW1j8.-4A` |
| elixir-uri vs python-urllib3 | `wss://cmP3J9s7@f..7S1j-2..dO6-B-In:8?#` | `` | `f..7s1j-2..do6-b-in` |
| go-net vs csharp-systemuri | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴?#` | `0ph.` | `0pH.` |
| csharp-systemuri vs python-urllib3 | `https://11139j078uW1j8.-4A:83563?#` | `` | `11139j078uW1j8.-4A` |
| csharp-systemuri vs python-urllib3 | `wss://cmP3J9s7@f..7S1j-2..dO6-B-In:8?#` | `` | `f..7s1j-2..do6-b-in` |
| csharp-systemuri vs python-urllib3 | `wss://6:16@-wRt04rzXgf-92I..77ᇧ?#` | `` | `-wrt04rzxgf-92i..77ᇧ` |
| whatwg vs python-urllib3 | `ms-settings-lock://0pH.?W2mqD[2:C:Ee:C:FB:F8:6:1f]:2縴?#` | `0pH.` | `0ph.` |
| whatwg vs python-urllib3 | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478?#` | `.8agD-.64.z64.091.E` | `.8agd-.64.z64.091.e` |
| whatwg vs python-urllib3 | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33@1j36y_82.Fv#` | `1j36y_82.Fv` | `1j36y_82.fv` |
