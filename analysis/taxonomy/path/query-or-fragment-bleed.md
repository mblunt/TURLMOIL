# Query or Fragment Bleed

**Description:** Part of the query string or fragment is captured in the path by some parsers, while others correctly stop the path at `?` or `#`.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|
| javascript-legacy vs javascript-fast-url-parser | `ventriloI://3Y63NWUY67C3:3v@7j@7Er0.59z85j18m:50|U1M17Dk8qg7_68u557r^5?#` | `/:50%7CU1M17Dk8qg7_68u557r%5E5` | `%7CU1M17Dk8qg7_68u557r%5E5` |
| javascript-legacy vs javascript-fast-url-parser | `http://a657hRrnd9d8]fyxz017420@7Eez6.C-py-.1c9F.uS:20|t9bp45XcDx0)}6W7U?#` | `/:20%7Ct9bp45XcDx0)%7D6W7U` | `%7Ct9bp45XcDx0)%7D6W7U` |
| javascript-legacy vs javascript-fast-url-parser | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gx9y87zM?1?2?&1?2?` | `sLopenpgp4fpraFQ7://2W21SCB%09E@5gHx.3n2u6P4401.-7l:048/;14[gx9y87zM` | `/;14[gx9y87zM` |
| javascript-legacy vs javascript-fast-url-parser | `wss://p875xyP|
xyz7o4@479.za.88-64-bt.xn--673,x7f-c325c?#` | `/` | `/,x7f-c325c` |
| javascript-legacy vs javascript-fast-url-parser | `ws://G%253793Z%25761@11:%2536%25397%2529MX8%2574|
8?%2523|` | `/:%2536%25397%2529MX8%2574%7C%0D8` | `%2536%25397%2529MX8%2574%7C8` |
| javascript-legacy vs javascript-fast-url-parser | `http://xn--848kjrnt@-x576a:1211<xy?#` | `%3Cxy` | `/:1211%3Cxy` |
