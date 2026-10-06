# Percent-Encoding Differences in Keys

**Description:** Parsers differ in whether they decode percent-encoded characters (especially control characters like %09, %0A, %0D) in query key names.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| lib1 (whatwg) vs lib2 (legacy) | `http:/6s70j7/,z8494wU-<~3Pm70B2r^488B?"2/\t...` | `{"\"2/\uc180...\ud00f": ""} (tab decoded)` | `{"\"2/\t\uc180...\ud00f": ""} (tab literal)` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://file://:@4Xoi...?...\r...%0D...` | `key without \r (CR decoded away)` | `key with \r (CR kept literal)` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://https://kw7od19gGl...?...F\r` | `{"...7F": ""} (no CR)` | `{"...7F\r": ""} (CR appended)` |
| lib1 (whatwg) vs lib2 (legacy) | `ftp://http://1mys:...?\tB...\n6` | `{"B...6": ""} (tab+newline stripped)` | `{"\tB...\n6": ""} (tab+newline kept)` |
| lib1 (whatwg) vs lib2 (legacy) | `ws://3sI52lm9EKS134v20ZY?...\n...\tOE3...n?#` | `key without \r and \t (control chars stripped)` | `key with \r and \t (control chars kept)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `://F2tA0/...?2P7-+%0C+94\87=#` | `{} (no keys parsed)` | `{"2P7- \f 94\\87": ""} (+ decoded as space, %0C as \f)` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `http:/6s70j7/...?"2/\t...` | `{} (empty - key not extracted)` | `{"\"2/\uc180...\ud00f": null}` |
| lib86 (python-urllib3) vs lib88 (python-furl) | `=wtaiz39.50sabout...?...` | `{} (empty)` | `{"key": null} (key decoded and returned)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `%42%51%6Ds%72p://...?`%3Du;N%36%5F(~*{3/` | `{} (fails to decode encoded key chars)` | `{"`=u;N6_(~*{3/": ""} (decodes %3D and %5F)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `oidkdtn...?0.95p87%FE#3@` | `{} (empty)` | `{".\u008895p87%FE": ""} (partial decode - \xFE kept encoded)` |
| lib86 (python-urllib3) vs lib87 (python-yarl) | `http:/6s70j7/...?"2/\t...` | `{} (cannot parse key)` | `{"\"2/\uc180...": ""} (key decoded and returned)` |
| lib86 (python-urllib3) vs lib89 (python-httpx) | `wÁ³://...?KÀ½4h3` | `{} (cannot parse)` | `{"K\u00c0\u00bd4h3": ""} (double-encoded bytes decoded)` |
| perl-uri vs python-urllib3 | `://8r4RJ4WunSK8Vk4:...?%098?9=7Dv3_bL+-&6=`=_A&t8\#kJU4` | `{"\t8?9":"7Dv3_bL -", "6":"`=_A", "t8\\":null}` | `{"8?9":["7Dv3_bL -"], "6":["`=_A"]}` |
| perl-uri vs python-urllib3 | `ft%2570://%2577...?5%2561;%2526=2jN3%252Bw%2536cn;6/%2526%2538%255B=qi898(f%255B23` | `{"%26":"2jN3%2Bw%36cn", "5%61":null, "6/%26%38%5B":"qi898(f%5B23"}` | `{"5%61;%26":["2jN3%2Bw%36cn;6/%26%38%5B=qi898(f%5B23"]}` |
| perl-uri vs python-urllib3 | `//ms-secondary-screen-controller...?=yM"#X|HmagnetQ8://...?=yM"` | `{"H\u007fmagnetQ8://34c58D2jDc:60K624@5.97.04.3:25\t\u0016\u241a...":"yM\""}` | `{"H\u007fmagnetQ8://34c58D2jDc:60K624@5.97.04.3:25\u0016\u241a...":["yM\""]}` |
| perl-uri vs python-urllib3 | `m%2573-sett%2569%256Egs://...?%252C=%2534񩷈󹇦%2530m1%2577Rwv6%2553Zx%2531;!%2533%2523` | `{"!%33%23":null, "%2C":"%34..."}` | `{"%2C;!%33%23":[...]}` |
| csharp-systemuri vs python-urllib3 | `?셇
0E6@74.74.69.77:=...&셇
0E6@74.74.69.77:=...` | `{"\uc147\n0E6@74.74.69.77:": ["...", "..."]}` | `{"\uc1470E6@74.74.69.77:": ["...", "..."]}` |
| csharp-systemuri vs python-urllib3 | `?K`=6{|r*W!/8
` | `{"K`": ["6{|r*W!/8\u0016\n"]}` | `{"K`": ["6{|r*W!/8\u0016"]}` |
| csharp-systemuri vs python-urllib3 | `?	i􀭧	9?4~w_=@!1y4,qb` | `{"	i\udbc2\udf67	9?4~w_": ["@!1y4,qb"]}` | `{"i\udbc2\udf679?4~w_": ["@!1y4,qb"]}` |
| csharp-systemuri vs python-urllib3 | `?
C⌫sb╾o?75i'...://27C5V6^(/18T=C],&A=Hk55&`53=.1C!\9-i}` | `{"
C\u232bsb\u257eo?75i'...://27C5V6^(/18T": ["C],"], "A": ["Hk55"], "`53": [".1C!\\9-i}"]}` | `{"C\u232bsb\u257eo?75i'...://27C5V6^(/18T": ["C],"], "A": ["Hk55"], "`53": [".1C!\\9-i}"]}` |
| python-furl vs python-urllib3 | `?9=4%66%40%23V%31f` | `{"9": "4f@#V1f"}` | `{"9": ["4f@#V1f"]}` |
| python-yarl vs python-urllib3 | `?=I%22Or:1-`T08=[2!` | `{"":": "I\"Or:1-`T08=[2!"}` | `{"":": ["I\"Or:1-`T08=[2!"]}` |
| python-furl vs python-urllib3 | `?=I%22Or%3A1-%60T08=%5B2%21` | `{"":": "I\"Or:1-`T08=[2!"}` | `{"":": ["I\"Or:1-`T08=[2!"]}` |
| python-yarl vs python-urllib3 | `?ZJ*]1$%2538"%2534=S%2577_%256F0%2565%2526&%25282_=59;;%2540 񵲑𠁵` | `{"ZJ*]1$%38\"%34": "S%77_%6F0%65%26", "%282_": "59;;%40..."}` | `{"ZJ*]1$%38\"%34": ["S%77_%6F0%65%26"], "%282_": ["59;;%40..."]}` |
| nodejs-url vs perl-uri | `?Nq=Grs%39` | `{"Nq": ["Grs%39"]}` | `{"Nq": "Grs9"}` |
| nodejs-url vs php-parseurl | `?Nq=Grs%39` | `{"Nq": ["Grs%39"]}` | `{"Nq": "Grs9"}` |
| nodejs-url vs php-parseurl | `?5%2561;%2526=2jN3%252Bw%2536cn` | `{"5%2561;%2526": ["2jN3%252Bw%2536cn..."]}` | `{"5%61;%26": "2jN3%2Bw%36cn..."}` |
| nodejs-url vs php-parseurl | `?ZJ*]1$%2538"%2534=S%2577_%256F0%2565%2526&%25282_=59` | `{"%25282_": ["59;;%2540..."], "ZJ*]1$%2538\"%2534": ["S%2577_%256F0%2565%2526"]}` | `{"ZJ*]1$%38\"%34": "S%77_%6F0%65%26", "%282_": "59;;%40..."}` |
