# CRLF/Tab Stripped from Query Keys

**Description:** Some parsers (following the WHATWG URL standard) strip CR (`\r`), LF (`\n`), and TAB (`\t`) characters from query strings before parsing, causing those characters to disappear from key names, while others preserve them as-is.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs javascript-legacy | `ftp://https://kw7od19gGl...?...F` | `{"...F": ""}` | `{"...F\r": ""}` |
| javascript-whatwg vs javascript-legacy | `ftp://http://1mys:...?	B𫋯
6` | `{"B\ud86c\udeef6": ""}` | `{"	B\ud86c\udeef\n6": ""}` |
| javascript-whatwg vs javascript-legacy | `wss://k6qfW...?2R4X󾙑7}` | `{"2R4X\udbb9\ude517}": ""}` | `{"2R4X\udbb9\ude517\r}": ""}` |
| javascript-whatwg vs javascript-legacy | `data:///...??0𨨱6` | `{"?0\u000b\ud862\ude316\u007f": ""}` | `{"?0\u000b\r\ud862\ude316\u007f": ""}` |
| javascript-whatwg vs javascript-legacy | `ws://3sI52...?...\fOE3...n?` | `{"...\fOE3...n?": ""}` | `{"...\f\tOE3...n?": ""}` |
| javascript-whatwg vs javascript-legacy | `http://ZxQ21581...?...\u0010P\udba0...\ud82a\udd22` | `{"...\u0010P\udba0...7?\ud82a\udd22": ""}` | `{"...\u0010P\udba0...\t7?\ud82a\udd22": ""}` |
| javascript-whatwg vs javascript-legacy | `http:/6s70j7...?"2/솀5...` | `{"\"2/\uc1805...": ""}` | `{"\"2/\t\uc1805...": ""}` |
| javascript-whatwg vs javascript-legacy | `ftp://file://...?󶊾...󼪟  ❓- l...` | `{"\udb98\udebe...\udbb2\ude9f...\u2753- l...": ""}` | `{"\udb98\udebe...\udbb2\ude9f\r...\u2753- l...": ""}` |
| perl-uri vs python-urllib3 | `?2P7-  94\87=` | `{"2P7- \f\r 94\\87": ""}` | `{}` |
| perl-uri vs python-urllib3 | `?='◞	񩦸L` | `{"":"◞	\ud966\uddb8L"}` | `{"":["'\u25de\ud966\uddb8L"]}` |
| elixir-uri vs python-urllib3 | `?='◞	񩦸L` | `{"":"◞񩦸L"}` | `{"":"'◞	񩦸L"}` |
| elixir-uri vs python-urllib3 | `http:/6s70j7/...?"2/	솀5...` | `{"\"2/\uc1805...": ""}` | `{"\"2/\t\uc1805...": ""}` |
| ruby-addressable vs python-urllib3 | `?K...\t\u0006\ud808...` | `{"K...\u0006\ud808...": ["."]}` | `{"K...\t\u0006\ud808...": ["."]}` |
| elixir-uri vs python-urllib3 | `?...;=Z&x1&=-=7h0` | `{"...{319151b98cMyr?/90~bmfX}3\\X;": ["Z"]}` | `{"...{319151b98cMyr?/90~bmfX}3\\X;": ["Z"]}` |
| rust-url vs elixir-uri | `http:/6s70j7/...?"2/	솀5...` | `{"\"2/\uc1805...": [""]}` | `{"\"2/\t\uc1805...": ""}` |
| rust-url vs elixir-uri | `?󶊾𭜀𣶠z󼪟 ❓- l` | `{"\udb98\udebe...\udbb2\ude9f...\u2753- l...": [""]}` | `{"\udb98\udebe...\udbb2\ude9f\r...\u2753- l...": ""}` |
| rust-url vs elixir-uri | `ftp://http://1mys:...?	B𫋯
6` | `{"B\ud86c\udeef6": [""]}` | `{"	B\ud86c\udeef": ""}` |
| rust-url vs elixir-uri | `?...OE3񐐘...n?` | `{"...OE3\ud901...n?": [""]}` | `{"...\tOE3\ud901...n?": ""}` |
| rust-url vs elixir-uri | `?^I[񿜑92^ᵒD鶙` | `{"^I\u000b[\ud9bd\udf1192^\u1d52D\u9d99": [""]}` | `{"^I\u000b[\ud9bd\udf1192^\u1d52D\u9d99": ""}` |
| ruby-addressable vs perl-uri | `?5:=Q󻪱` | `{"5:": "Q󻪱"}` | `{"5:": "Q󻪱\r"}` |
| ruby-addressable vs perl-uri | `?http://http://5:@7l03...?K`=6{|r*W!/8
` | `{"K`": "6{|r*W!/8\u0016"}` | `{"K`": "6{|r*W!/8\u0016\n"}` |
| ruby-uri vs perl-uri | `?셇
0E6@74.74.69.77:=򑝅𤓻>0GD0t21149T61=m23no?&셇
...` | `{"셇\n0E6@74.74.69.77:": "�...�..."}` | `{"셇\n0E6@74.74.69.77:": ["�...", "�..."]}` |
| go-net vs php-parseurl | `?셇
0E6@74.74.69.77:=򑝅𤓻>0GD0t21149T61=m23no?&셇
0E6...` | `{"셇\n0E6@74.74.69.77:": ["...", "..."]}` | `{"셇0E6@74.74.69.77:": ["...", "..."]}` |
| csharp-systemuri vs python-urllib3 | `?K`=6{|r*W!/8
` | `{"K`": ["6{|r*W!/8\u0016\n"]}` | `{"K`": ["6{|r*W!/8\u0016"]}` |
| csharp-systemuri vs python-urllib3 | `?	i􀭧	9?4~w_=@!1y4,qb&5` | `{"	i􀭧	9?4~w_": ["@!1y4,qb"]}` | `{"i􀭧9?4~w_": ["@!1y4,qb"]}` |
| csharp-systemuri vs python-urllib3 | `?
...key
=value` | `{"key": ["value"]}` | `{"\r\nkey\r\n": ["value"]}` |
| python-ada-url vs python-urllib3 | `?	B𫋯6` | `{"B𫋯6": [""]}` | `{}` |
| python-ada-url vs python-urllib3 | `?"2/	솀5򘵽𫅴퀏` | `{"\"2/솀5򘵽𫅴퀏": [""]}` | `{}` |
| rust-url vs perl-uri | `?'𞍍 key
=value` | `{"key\r\n": [""]}` | `{"key": [""]}` |
| python-ada-url vs python-urllib3 | `?^I[񿜑92^...` | `{"^I[񿜑92^ᵒD鶙": [""]}` | `{}` |
| nodejs-url vs php-parseurl | `?"2/	솀5...=` | `{"\"2/\t\uc180...": [null]}` | `{"\"2/_\uc180...": ""}` |
| nodejs-url vs perl-uri | `?"2/	솀5...=` | `{"\"2/\t\uc180...": [null]}` | `{}` |
| nodejs-url vs php-parseurl | `?􇣃l񪙻𩜞sh...|'` | `{"􇣃l񪙻𩜞sh􏌄Z-2|'": [null]}` | `{}` |
| nodejs-url vs perl-uri | `?􇣃l key...` | `{"􇣃l key...": [null]}` | `{}` |
