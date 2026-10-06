# Unicode Normalization (NFC/NFD/NFKC)

**Description:** Unicode normalization forms (NFC, NFD, NFKC, NFKD) are applied differently: one parser decomposes or composes Unicode characters (e.g. precomposed vs decomposed Greek letters, circled numbers decoded to ASCII digits) while another returns the raw code points.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| python-urllib3 vs python-yarl | `telnet://Z4
ᾔ4E/../6111D44@00?#` | `z4ᾔ4e` | `z4ἤ4ι4e` |
| python-urllib3 vs python-yarl | `http://558:767332:@Ug0pl866281hd.Mj7-N𝳧᱉⑳?#k` | `ug0pl866281hd.mj7-n𝳧᱉⑳20` | `ug0pl866281hd.mj7-n𝳧᱉⑳` |
| python-urllib3 vs python-yarl | `https://r2y51K:la@743e.I7.xn--0198oui&tx0m8b9g3"51k6-vr3p761a?{#` | `743e.i7.0◎19⠊8oui&tx0m8b9g3"51k6` | `743e.i7.xn--0198oui&tx0m8b9g3"51k6-vr3p761a` |
| ruby-addressable vs ruby-uri | `http://558:767332:@Ug0pl866281hd.Mj7-N𝳧᱉⑳?#k` | `` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` |
| ruby-addressable vs ruby-uri | `http://5n	f@29.00.6.78(97217)...?#` | `29.00.6.xn--78(97217)4whxc-bv1k41vgn82z` | `` |
| kotlin-ktor vs java-okhttp3 | `http://558:767332:@Ug0pl866281hd.Mj7-N𝳧᱉⑳?#k` | `Ug0pl866281hd.Mj7-N𝳧᱉⑳` | `Ug0pl866281hd.Mj7-Nð±£§áâ³` | <---- UTF8 vs LATIN-1
| kotlin-ktor vs java-okhttp3 | `http://3KHrM77A48u93Oi4	289oWUAN96	]...\\á¾½Þ\uð\u­?#` | `3KHrM77A48u93Oi4	289oWUAN96	]...\u᾽ފ𠭐` | `3KHrM77A48u93Oi4	289oWUAN96	]...\\á¾½Þð ­` |
