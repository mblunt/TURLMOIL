# Leading Zeros in IPv4 Octets

**Description:** Parsers disagree on whether to strip leading zeros from IPv4 address octets (e.g., 01.0.39.6 vs 1.0.39.6), where one normalizes octets to their minimal decimal representation and the other preserves the original encoding.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-galimatias vs rust-url | `ws://b315VlgK2h6fKa1B01o:2@01.0.39.6:944/...` | `01.0.39.6` | `1.0.39.6` |
| java-galimatias vs rust-url | `http://aLH3sRc5Ffw@5.00.97.79:2902?#` | `5.00.97.79` | `5.0.97.79` |
| java-galimatias vs rust-url | `ftp:// Q@9.69.07.07:03\...` | `9.69.07.07` | `9.69.7.7` |
| java-galimatias vs rust-url | `ftp://4R75...@84.89.04.4?#` | `84.89.04.4` | `84.89.4.4` |
| java-galimatias vs rust-url | `http://0Py710 e84y@64.93.03.72:...` | `64.93.03.72` | `64.93.3.72` |
| java-galimatias vs rust-url | `ftp://y2y94lkS9mw9np03@82.4.01.4:98/...` | `82.4.01.4` | `82.4.1.4` |
| java-galimatias vs rust-url | `https://6#5X@7g.s9:855}?...@64.93.03.72:...` | `64.93.03.72` | `64.93.3.72` |
| java-galimatias vs rust-url | `https://1/.../64.09.91.353...` | `64.09.91.xn--353d7g7eiip3y3z7j9o25e-irp9243i` | `64.09.91.353...` |
| java-galimatias vs rust-url | `http://aLH3sRc5Ffw@5.00.97.79:2902?#x69e+3` | `5.00.97.79` | `5.0.97.79` |
| java-galimatias vs rust-url | `https://HK69g9V4q6i@8.82.5.02:0/./...` | `8.82.5.2` | `8.82.5.02` |
| java-galimatias vs rust-url | `https://Snd8a2ic17...@91.2.62.00:43/...` | `91.2.62.00` | `91.2.62.0` |
| javascript-uri-js vs crystal-uri | `ftp://Kds2CYszhi8H67d𬁚Qtjf@08.61.1.95:76?#` | `08.61.1.95` | `8.61.1.95` |
| javascript-whatwg vs crystal-uri | `ws://8f𒎟]D8Eu8@6.2/..56.2:044Ѕ𮘧𢂢5K4wuQX)5601&hI3AAh?` | `6.2` | `6.0.0.2` |
| javascript-whatwg vs crystal-uri | `https://zy𗒄𚕣|a@2.6.29?#.47:1𙫝 𐲂 9` | `2.6.29` | `2.6.0.29` |
| javascript-whatwg vs crystal-uri | `https://4⦽v7j@3.97.6/..34:6✿𘜠𖣤	⧘2!7Gq^Vn1]:7j4EoXe2l?#` | `3.97.6` | `3.97.0.6` |
