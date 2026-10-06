# Surrogate Pair Encoding

**Description:** Some parsers encode supplementary Unicode characters as UTF-16 surrogate pairs (%ED%A…%ED%B…), while others encode them as proper UTF-8 sequences (%F0…).

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|

| javascript-whatwg vs javascript-smithy | `beshare://2406TUm7F68SmK2m3a/...Q+I@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q%E2%9E%B4I%ED%AE%BD%ED%B7%BFM@%5B4d:2A:81:f:1:A:b6:C0%5D:727` |
| javascript-whatwg vs javascript-smithy | `ftp://ftp://7f195_12:833X{nZ\.4g`z0=1jnD09KW8#` | `//7f195_12:833%19%F1%87%87%A6%7BnZ/.4g%60z0=1jnD09KW8` | `//7f195_12:833%19%ED%A3%9C%ED%B7%A6%7BnZ%5C.4g%60z0=1jnD09KW8` |
| javascript-whatwg vs javascript-fast-uri | `soldatpwid://.../4Ku21984jdGvl51unc0x3z@-5V0w29:860#` | `/4Ku21984jdGvl51unc0%F0%A4%84%983z@-5V0w29:860` | `/4Ku21984jdGvl51unc%0A0%uD850%uDD183z@-5V0w29%3A860` |
| javascript-whatwg vs javascript-fast-uri | `beshare://2406TUm7F68SmK2m3a/...Q+IM@[4d:2A:81:f:1:A:b6:C0]:727?` | `/...Q%E2%9E%B4I%F3%BF%97%BFM@[4d:2A:81:f:1:A:b6:C0]:727` | `/...Q%u27B4I%uDBBD%uDDFFM@%5B4d%3A2A%3A81%3Af%3A1%3AA%3Ab6%3AC0%5D%3A727` |
| javascript-whatwg vs javascript-fast-uri | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827?2P5#` | `/dhqo%F4%86%B8%9F914crJ@-7zZ54:827` | `/../dhqo%uDBDB%uDE1F914crJ@-7zZ54%3A827%0A` |
