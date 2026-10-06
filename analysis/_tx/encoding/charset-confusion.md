# Charset / Encoding Confusion (Latin-1 vs UTF-8)

**Description:** One parser misinterprets the URL's character encoding (e.g., reads UTF-8 bytes as Latin-1), producing mojibake in the host field, while the other correctly handles Unicode code points.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| ada-uri-mime vs rust-url | `ws://do2ycs037T핗s3k@1𦒲3⦷8y5/./(28KZ3tq83U3y3lg?#򲗂c` | `1ð¦­3â¦·8y5` | `xn--138y5-2x5cz9190b` |
| ada-uri-mime vs rust-url | `ftp://4COWp$4�6L@f．.h0-aujmp7G74N89Z8gs4qIgo7n1Oi4m2117x?#` | `fï¼.h0-aujmp7G74N89Z8gs4qIgo7n1Oi4m2117x` | `f..h0-aujmp7g74n89z8gs4qigo7n1oi4m2117x` |
| ada-uri-mime vs rust-url | `data://dX11kuwT3n59F32𘂵394NYE@55。7。26.4950u53p5oj0,07S8A76Jsx?#` | `55ã7ã26.4950u53p5oj0,07S8A76Jsx` | `55%E3%80%827%E3%80%8226.4950u53p5oj0,07S8A76Jsx` |
| perl-uri vs python-urllib3 | `https://6U2K16Á¹721K5...
@.À¶-☹...` | `.à¶-☹ò¼²±àv!`8à≤...` | `.À¶-☹ò¼²±À
 v!`8À≤...` |
| perl-uri vs python-urllib3 | `file://EÁP3rÁµ6GÁXQÁG06Q1GLⒺ㞔5#...@...` | `EÁP3rÁµ6GÁXQÁG06Q1GLⒺ㞔5` | `eáp3ráµ6gáxqág06q1glⒺ㞔5` |
| perl-uri vs python-urllib3 | `https://6U2K16Á¹721K5Á 21d40Á¯4T@.À¶-⌙...` | `.à¶-⌙àv!`8à...` | `.À¶-⌙À
v!`8À...` |
| perl-uri vs python-urllib3 | `file://EÁP3rÁµ6GÁXQÁG06Q1GLⒺ㖼5#...` | `EÁP3rÁµ6GÁXQÁG06Q1GLⒺ㖼5` | `eáp3ráµ6gáxqág06q1glⒺ㖼5` |


| perl-uri vs python-urllib3 | `file://EAP3rAu6GAXQAG06Q1GL...` | `EAP3rAu6GAXQAG06Q1GL...` | `eap3rau6gaxqag06q1gl...` |
| perl-uri vs python-urllib3 | `https://6U2K16...@.A0-...(latin1 mojibake host)` | `.a0-... (lowercase mojibake)` | `.A0-... (uppercase mojibake)` |
| go-net vs rust-url | `file://SÀµÀ³86nl880𩷱#(...)@E823HNhÁQqp-29-55j...` | `SÀµÀ³86nl880𩷱` | `xn--s386nl880-q1aa798f5r08t` |
| javascript-whatwg vs perl-mojo-url | `go://5j7TF3XRὍ9
༼...⤕...` | `2203%F3%99%B9%A8o20O` | `2203ó¹¨o20O` |
| javascript-whatwg vs perl-mojo-url | `http://558:767332:...@Ug0pl866281hd.Mj7-N𑣧ᰉ⑳?#k` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` | `Ug0pl866281hd.Mj7-Nð±£§áâ³` |
| javascript-whatwg vs perl-mojo-url | `data://4444r42@9rM｡H3F574l69.1mg-y
3...` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `9rMï½¡H3F574l69.1mg-y
3ñ` |
| javascript-legacy vs java-galimatias | `http://91Á£4I
:.𚗤...Ā°1.È.62.47:5B0r4P6...` | `xn--n6-qfa5k` | `xn--914i-cga74b` |
| javascript-legacy vs java-galimatias | `file://D0185U7bHq0...
...ẚ/...@36.88.19.41:250...` | `xn--d0185u7bhq0-0w7b` | `xn--d0185u7bhq0-bk1c0111cxp97aru38a` |
| crystal-uri vs rust-url | `data://Áº5
𦑖⠅𓲿À³60@À¹Àº23pDÁ³S6dfÀ²1+34092PÀ°G5À¿#` | `À¹Àº23pDÁ³S6dfÀ²1+34092PÀ°G5À¿` | `%C3%80%C2%B9%C3%80%C2%BA23pD%C3%81%C2%B3S6df%C3%80%C2%B21+34092P%C3%80%C2%B0G5%C3%80%C2%BF` |
