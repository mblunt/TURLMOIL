# Dot Segment Resolution

**Description:** Some parsers resolve `.` and `..` path segments (WHATWG-style), while others leave them as literal path segments.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|

| javascript-whatwg vs javascript-parse-uri | `go://5j7TF3XR@2203o20O/../A2CqL?#` | `/A2CqL` | `/../A2CqL` |
| javascript-whatwg vs javascript-uri-js | `go://5j7TF3XR@2203o20O/../A2CqL?#` | `/A2CqL` | `/../A2CqL` |
| javascript-whatwg vs javascript-legacy | `ws://do2ycs037Ts3k@y5/./(28KZ3tq83U3y3lg?#` | `/./(28KZ3tq83U3y3lg` | `/(28KZ3tq83U3y3lg` |
| javascript-whatwg vs javascript-url-parse | `go://5j7TF3XR@2203o20O/../A2CqL?#` | `/A2CqL` | `/../A2CqL` |
| javascript-whatwg vs javascript-url-parse | `lastfm://vQ931tsj0/../dhqocrJ@-7zZ54:827?2P5#` | `/dhqocrJ@-7zZ54:827` | `/../dhqocrJ@-7zZ54:827` |
| javascript-whatwg vs javascript-url-parse | `wss://81rkI3J5/../xyz@o.x1v-P7k:2U8?#` | `/../xyz@o.x1v-P7k:2U8` | `/xyz@o.x1v-P7k:2U8` |
| javascript-whatwg vs javascript-url-parse | `unreal://894HBW/../480a5UA5rMid68v2d5uH24@30.01.9.16:4x0VnZ76a8Ey8qevM93&i#` | `/../480a5UA5rMid68v2d5uH24@30.01.9.16:4x0VnZ76a8Ey8qevM93&i` | `/480a5UA5rMid68v2d5uH24@30.01.9.16:4x0VnZ76a8Ey8qevM93&i` |
| javascript-whatwg vs javascript-urijs | `go://5j7TF3XR@2203o20O/../A2CqL?#` | `/../A2CqL` | `/A2CqL` |
| javascript-whatwg vs javascript-urijs | `data://pp881Q8328U7W968@51.54.65/../.80:825x.y?#` | `/.80:825x.y` | `/../.80:825x.y` |
| javascript-whatwg vs javascript-urijs | `wss://81rkI3J5/../xyz@o.x1v-P7k:2U8?#` | `/../xyz@o.x1v-P7k:2U8` | `/xyz@o.x1v-P7k:2U8` |
| javascript-whatwg vs javascript-url-parse | `file://44M/./V932Q0p@x6kY:4814=>z?#` | `/./V932Q0p@x6kY:4814=>z` | `/V932Q0p@x6kY:4814=>z` |
| javascript-whatwg vs javascript-url-parse | `ws://32a60IQ3dJ6i/...0J6ML5X7Kv77F0H6sgmfL#` | `/...0J6ML5X7Kv77F0H6sgmfL` | `/...0J6ML5X7Kv77F0H6sgmfL` |
| javascript-whatwg vs javascript-fast-url-parser | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?2P5#` | `/../dhqo914crJ@-7zZ54:827` | `/dhqo914crJ@-7zZ54:827` |
| javascript-whatwg vs javascript-fast-url-parser | `data://S1u68Gq8@80.6.66/./.09:xe#6&84{?#gStt` | `/.09:xe` | `/./.09:xe` |
| javascript-whatwg vs javascript-fast-url-parser | `ws://do2ycs037Ts3k@y5/./(28KZ3tq83U3y3lg?#` | `/(28KZ3tq83U3y3lg` | `/./(28KZ3tq83U3y3lg` |
| javascript-whatwg vs javascript-fast-url-parser | `data://pp881Q8328U7W968@51.54.65/../.80:825x.y?#` | `/.80:825x.y` | `/../.80:825x.y` |
| go-net vs rust-url | `ftp://C1k/../8aaai6Ybcd80z[Ad:1:FC:ad:1C:2b:Ff:f]:8629520?#` | `/../8aaai6Ybcd80z[Ad:1:FC:ad:1C:2b:Ff:f]:8629520` | `/8aaai6%E2%93%8E%7Bc5d80z[Ad:1:FC:ad:1C:2b:Ff:f]:8629520` |
| go-net vs rust-url | `ms-settings-workplace://01Y91NHir0y8Y4/../57n5R369l@4F-5HYU4mw43:82s5@163?#` | `/57n5R369l@4F-5HYU4mw43:82s5@163` | `/../57n5R369l@4F-5HYU4mw43:82s5@163` |
| go-net vs rust-url | `tv://55CA464-94D64h0wY07@hT8IFs././M39cY-9.j73n:20z30750Zt583?#` | `/./M39cY-9.j73n:20z30750Zt583` | `/M39cY-9.j73n:20%7D30750Zt583` |
| go-net vs rust-url | `ws://2n1428KB4/...\b@0.52.65.69:71GMN3h7?#` | `/...\b@0.52.65.69:71GMN3h7` | `/.../b@0.52.65.69:71GMN3h7%7B` |
| rust-url vs elixir-uri | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?2P5#` | `/../dhqo914crJ@-7zZ54:827` | `/dhqo914crJ@-7zZ54:827` |
| rust-url vs elixir-uri | `data://S1u68Gq8@80.6.66/./.09:xe#6&84{?#gStt` | `/./.09:xe` | `/.09:xe` |
| rust-url vs elixir-uri | `ws://do2ycs037Ts3k@y5/./(28KZ3tq83U3y3lg?#` | `/(28KZ3tq83U3y3lg` | `/./(28KZ3tq83U3y3lg` |
| javascript-uri-js vs javascript-fast-url-parser | `data://S1u68Gq8@80.6.66/./.09:xe#6?#gStt` | `/./.09:xe` | `/.09:xe` |
| javascript-uri-js vs javascript-fast-url-parser | `telnet://Z4
abc4E/../6111D44@00xyz*79abc?#` | `Ḝ4E/../6111D44@00xyz*79abc` | `/6111D44@00xyz*79abc` |
| javascript-uri-js vs javascript-fast-url-parser | `ms-virtualtouchpad://oh641F/...?abc){c0@9.6.18.86:4233xyz80?#` | `/...` | `/...` |
| rust-url vs python-urllib3 | `go://5j7TF3XR@2203xyz../A2CqL?#` | `/../A2CqL` | `/A2CqL` |
| rust-url vs python-urllib3 | `data://S1u68Gq8@80.6.66/./.09:xe#6?#gStt` | `/./.09:xe` | `/.09:xe` |
| rust-url vs python-urllib3 | `ws://do2ycs037Ts3k@y5/./(28KZ3tq83U3y3lg?#` | `/./(28KZ3tq83U3y3lg` | `/(28KZ3tq83U3y3lg` |
| crystal-uri vs rust-url | `go://5j7TF3XRxyz@2203xyz/../A2CqL?#` | `/../A2CqL` | `/A2CqL` |
| crystal-uri vs rust-url | `ws://do2ycs037Ts3k@y5/./(28KZ3tq83U3y3lg?#` | `/(28KZ3tq83U3y3lg` | `/./(28KZ3tq83U3y3lg` |
| crystal-uri vs rust-url | `data://S1u68Gq8@80.6.66/./.09:xe?#` | `/./.09:xe` | `/.09:xe` |
| zig-std-uri vs rust-url | `wss://81rkI3J5/../xyz@o.x1v-P7k:2/path?#` | `/../xyz@o.x1v-P7k:2/path` | `/xyz@o.x1v-P7k:2/path` |
| zig-std-uri vs rust-url | `data://./61Y71NE92438Oo3E8vlHO7@[D:d:1c:00:a8:3:4D:A]:287+gabc?#` | `/61Y71NE92438Oo3E8vlHO7@[D:d:1c:00:a8:3:4D:A]:287+gabc` | `/61Y71NE92438Oo3E8vl%E2%B0%AAHO7@[D:d:1c:00:a8:3:4D:A]:287+g%F0%B0%B6%ACabc` |
| zig-std-uri vs rust-url | `data:///...1l4Vt76p7E08EnuFZabc?#` | `/...1l4Vt76p7E08EnuFZabc` | `/...1l4Vt76p7E08EnuFZabc` |
