# Path Segments Affecting Host Extraction

**Description:** Dot-segments (/../, /./), single-slash URLs, or other path-like constructs in the authority cause different parsers to extract different host values or fail to parse the host entirely.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs javascript-smithy | `https:/a(19x?/5bK/%
$BV7@76.0.3.2:9780DmI3a6I217]5]9#` | `a(19x` | `` |
| whatwg vs javascript-smithy | `wss://.../0𐻋
(��}7?%p@89.54.22.0:2368\𐇨⬄󡥓tY67S37m7B2fbpEQ1Z2?##9u` | `` | `...` |
| whatwg vs javascript-smithy | `wss://4VE/...t9pJRm?/󯲿᫘𐴔%=9m6@5pe18.u62275QROF8.h:0585,5C7"1p15126z7Ui784?#` | `4ve` | `` |
| whatwg vs javascript-smithy | `ws://U00N745R98{-92`8B853qV?N07b82Bb9J576O0󨃑Ÿ��𣕮%2@?♾𐻨7u'v8410U436@[4B:4:6d:C:E:6:a:4d]:79-#` | `u00n745r98{-92`8b853qv` | `` |
| javascript-whatwg vs javascript-legacy | `http://///1K8jECVgP23Ō?Y...` | `xn--1k8jecvgp23-v9b` | `` |
| javascript-whatwg vs javascript-legacy | `go://5j7TF3XR@2203󙹨o20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `` |
| javascript-whatwg vs javascript-smithy | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?` | `file` | `` |
| javascript-whatwg vs javascript-smithy | `chrome-extension://FgL/../6Lnx1T1qqd?` | `fgl` | `` |
| javascript-whatwg vs javascript-deno | `data://7841S8HHbqof18&@ndv799213vqQi126XMb:376\?` | `ndv799213vqQi126XMb` | `` |
| whatwg vs uri-parser | `soldatpwid://.../4Ku21984jdGvl51unc 0@-5V0w29:860#` | `...` | `-5V0w29` |
| whatwg vs trurl | `data://S1u68@80.6.66/./.09:...?#gStt` | `80.6.66` | `` |
| whatwg vs trurl | `file://a9HC5V03i92S3b9z330/..G?#` | `a9hc5v03i92s3b9z330` | `` |
| whatwg vs swift-url | `file://a9HC5V03i92S3b9z330/..G?#` | `a9hc5v03i92s3b9z330` | `a9HC5V03i92S3b9z330` |
| whatwg vs go-net | `https://189q46u/...r62h66SP2ksO 4nZ3G81tolVKM@322N8QX8?#` | `189q46u` | `` |
| whatwg vs swift-url | `soldatpwid://.../4Ku21984jdGvl51unc 0@-5V0w29:860#` | `...` | `` |
| python-urllib-parse vs python-furl | `data://S1u68@80.6.66/./.09:...?#gStt` | `80.6.0.66` | `` |
| php-rfc3986 vs php-league-uri | `data://S1u68@80.6.66/./.09:...?#gStt` | `` | `80.6.66` |
| swift-foundation vs swift-misc | `data://S1u68@80.6.66/./.09:...?#gStt` | `80.6.66` | `` |
| swift-foundation vs swift-misc | `https://189q46u/...r62h66SP2ksO@322N8QX8-100...?#` | `189q46u` | `` |
| elixir-uri vs elixir-ex_url | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `vQ931tsj0` | `` |
| rust-url vs rust-urlparse | `go://5j7TF3XR
@2203o20O/../A2CqL?#` | `2203o20o` | `` |
| rust-url vs rust-urlparse | `data://pp881Q@51.54.65/../.80:825?#` | `51.54.65` | `` |
| erlang-uri-string vs erlang-hackney-url | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `vQ931tsj0` | `` |
| erlang-uri-string vs erlang-hackney-url | `	ᵋ://6t2v155/./	ze...-K:	h
S#|?` | `` | `ᴋ` |
| python-httpx vs python-rfc3986 | `ws://hrl49V3Q50/...8f77gTbO:
5T@H4t@xvk.K-.M.5..96U37-N:3250?#` | `hrl49V3Q50` | `` |
| python-httpx vs python-rfc3986 | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `vQ931tsj0` | `` |
| python-httpx vs python-rfc3986 | `data://S1u68@80.6.66/./.09:...?#gStt` | `` | `80.6.66` |
| python-uritools vs python-hyperlink | `data://o421p1@[69:28:cA:C:5a:0c:2:f]0o...@6w0U03?#AP` | `` | `6w0U03` |
| go-net vs java-okhttp | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `` | `vQ931tsj0` |
| go-net vs java-okhttp | `https://189q46u/...r62h66SP2ksO@322N8QX8-100?#` | `` | `189q46u` |
| java-uri vs java-galimatias | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `` | `vQ931tsj0` |
| java-spring-web vs java-apache-httpclient | `data://S1u68@80.6.66/./.09:...?#gStt` | `80.6.66` | `` |
| java-spring-web vs java-apache-httpclient | `data://./61Y71NE92438Oo3E8vlHO7@[D:d:1c:00:a8:3:4D:A]:287?#` | `.` | `` |
| java-spring-web vs java-apache-httpclient | `data://pp881Q8@51.54.65/../.80:825?#` | `51.54.65` | `` |
| ruby-addressable vs ruby-uri | `https://189q46u/...r62h66SP2ksO@322N8QX8-100?#` | `` | `189q46u` |
| ruby-addressable vs ruby-uri | `ws://hrl49V3Q50/...8f77gTbO:
5T@H4t@xvk.K-.M.5..96U37-N:3250?#` | `hrl49v3q50` | `` |
| node-whatwg vs php-league | `go://5j7TF3XR
xvr@2203󙹨o20O/../A2CqL?#` | `` | `2203󙹨o20O` |
| java-jdk-uri vs java-spring-mvc | `data://4444r@9rM｡H3F574l69.1mg-y
3?#` | `` | `9rM｡H3F574l69.1mg-y
3` |
| java-jdk-uri vs java-spring-mvc | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5@1JLw5x?#` | `` | `1JLw5x` |
| javascript-whatwg vs javascript-uri-parser | `soldatpwid://.../4Ku21984jdGvl51unc@-5V0w29:860#` | `...` | `-5V0w29` |
| javascript-whatwg vs javascript-uri-parser | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827?#` | `vq931tsj0` | `-7zZ54` |
| rust-url vs rust-uriparse | `soldatpwid://.../4Ku21984jdGvl51unc@-5V0w29:860#` | `` | `...` |
| rust-url vs rust-uriparse | `ws://hrl49V3Q50/...8f77gTbO:@H4t@xvk.K-.M.5..96U37-N:3250?#` | `` | `hrl49v3q50` |
| javascript-whatwg vs rust-url | `data://S1u68@80.6.66/./.09?#` | `` | `80.6.66` |
| go-net vs python-urllib3 | `https://189q46u/...r62h66SP2ksO@322N8QX8-100?#` | `` | `189q46u` |
| go-net vs python-urllib3 | `data://S1u68@80.6.66/./.09?#` | `` | `80.6.66` |
| go-net vs rust-url | `wss://0qUe64W783@543YscTb.7ce2P.B..1:54?#/./j7?#` | `` | `0que64w783e8⛹` |
| go-net vs csharp-systemuri | `https://189q46u/...r62h66SP2ksO@322N8QX8?#` | `` | `189q46u` |
| csharp-systemuri vs python-urllib3 | `data://787:@f:315@U1D=y!c9A/.W#8` | `` | `u1d=y!c9a` |
| go-net vs csharp-systemuri | `data://S1u68@80.6.66/./.09?#` | `80.6.66` | `` |
