# Backslash Normalisation

**Description:** WHATWG-compliant parsers convert `\` to `/` in the path; others preserve the backslash literally.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|

| javascript-whatwg vs javascript-uri-js | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#h15x1R[643` | `/%5COX34yP4Vcq93lr4k5687` | `/\OX34yP4Vcq93lr4k5687` |
| javascript-whatwg vs javascript-legacy | `data:/\/T3^qjvBK04FP3J1@33m1nL76:00x887Pwd92k2BF8wbJ8\?#` | `/\/T3%5E%10qjvBK04FP3J1@33m1nL76:00%05x887Pwd92k2BF8wbJ8\` | `/T3%5EqjvBK04FP3J1@33m1nL76:00x887Pwd92k2BF8wbJ8/` |
| javascript-whatwg vs javascript-fast-url-parser | `wss://https://y113:M{x_@75.5.52.35!a3-FLmmM7\9jq9M3XF56?#9` | `//y113:M%7Bx_@75.5.52.35!a3-FLmmM7/9jq9M3XF56` | `//y113:M%7Bx_@75.5.52.35!a3-FLmmM7\9jq9M3XF56` |
| javascript-whatwg vs javascript-fast-url-parser | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#h15x1R[643` | `/\OX34yP4Vcq93lr4k5687` | `//OX34yP4Vcq93lr4k5687` |
| javascript-whatwg vs javascript-fast-url-parser | `data://file://5n1F0yoL3QA@1L50.-.HYi04189.-gq:3167jDk192~8k7\0Zu428Yk?` | `//5n1F0yoL3QA@1L50.-.HYi04189.-gq:3167jDk192~8k7/0Zu428Yk` | `//5n1F0yoL3QA@1L50.-.HYi04189.-gq:3167jDk192~8k7\0Zu428Yk` |
| javascript-uri-js vs javascript-url-parse | `ftp://ftp://7f195_12:833xyz{nZ\.4g`z0=1jnD09KW8#` | `//7f195_12:833xyz{nZ/.4g`z0=1jnD09KW8` | `//7f195_12:833%19%F1%87%87%A6%7BnZ/.4g%60z0=1jnD09KW8` |
| javascript-uri-js vs javascript-url-parse | `wss://wss://7xyz	,abc8;5efg8l8Fe:35GO1X\Y764O&29r8G97?#` | `//7xyz,abc8;5efg8l8Fe:35GO1X/Y764O&29r8G97` | `//7%F0%9E%AF%BF%F3%B8%AA%89,%F0%AB%8B%AF8;5%E2%A7%A68l8Fe:35GO1X/Y764O&29%22r8G97` |
| javascript-uri-js vs javascript-fast-url-parser | `openpgp4fpr://8G/.BUx34x38k9@[1d:9:4:f:8:D:Ec:6D]108xyz?#` | `openpgp4fpr://8G/.BUx34x38k9@[1d:9:4:f:8:D:Ec:6D]108xyz` | `/.BUx34%F2%83%BB%84%F0%B7%8E%9538k9@[1d:9:4:f:8:D:Ec:6D]108xyz` |
| javascript-uri-js vs javascript-fast-url-parser | `dntp://F70_9xQh7JXV@[D:C:a1:cE:b:33:D:f]:42256/L\gWg4AMU613@o0O?#` | `/L/gWg4AMU613@o0O` | `/L\gWg4AMU613@o0O` |
| javascript-uri-js vs javascript-fast-url-parser | `wss://http://n
\)3xyz:abc2=-3d0h.Q3Yz5.8.69.-M77<xyz46Ct9FdR33618053kuU?#` | `//n/)3xyz:abc2=-3d0h.Q3Yz5.8.69.-M77<xyz46Ct9FdR33618053kuU` | `//n/)3xyz:abc2=-3d0h.Q3Yz5.8.69.-M77%3Cxyz46Ct9FdR33618053kuU` |
| perl-uri vs go-net | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#h15x1R[643` | `/\OX34yP4Vcq93lr4k5687` | `/%5COX34yP4Vcq93lr4k5687` |
| perl-uri vs go-net | `wss://https://y113:M{X_@75.5.52.35abc!a3-FLmmM7\9jq9M3XF56?#9` | `//y113:M{X_@75.5.52.35abc!a3-FLmmM7\9jq9M3XF56` | `//y113:M%7BX_@75.5.52.35abc!a3-FLmmM7%5C9jq9M3XF56` |
| javascript-legacy vs go-net | `pttp://3S2201fZjPr3XKK2103:9T@1:5/\OX34yP4Vcq93lr4k5687?#h15x1R[643` | `/\OX34yP4Vcq93lr4k5687` | `//OX34yP4Vcq93lr4k5687` |
| javascript-legacy vs go-net | `wss://https://y113:M{x_@75.5.52.35abc!a3-FLmmM7\9jq9M3XF56?#9` | `//y113:M%7Bx_@75.5.52.35abc!a3-FLmmM7/9jq9M3XF56` | `//y113:M{x_@75.5.52.35abc!a3-FLmmM7\9jq9M3XF56` |
| javascript-legacy vs go-net | `%2568xxps%253A//hFp7E%257006%25753xyz\4L96n%256AxJT?#` | `%68xxps%3A//hFp7E%7006%753xyz\4L96n%6AxJT` | `%2568xxps%253A//hFp7E%257006%25753xyz/4L96n%256AxJT` |
| csharp-systemuri vs rust-url | `data://file://5n1\xyz@gq:3167/0Zu428Yk?` | `//5n1/xyz@gq:3167/0Zu428Yk` | `//5n1\xyz@gq:3167/0Zu428Yk` |
| csharp-systemuri vs rust-url | `openpgp4fpr://8G/.BUx34x@[1d:9:4:f]:108abc6u0s6_P7,$P6K\rK611?#` | `/.BUx34x@[1d:9:4:f]:108abc6u0s6_P7,$P6K/rK611` | `/.BUx34x@[1d:9:4:f]:108abc6u0s6_P7,$P6K\rK611` |
