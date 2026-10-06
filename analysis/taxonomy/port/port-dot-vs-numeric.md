# Port dot vs numeric representation

**Description:** One parser returns dot (.) for missing/invalid port while the other returns a numeric value

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs parse_uri | `ed2k:/.//:f14.4.35.9:50ڀਧ#🞠*8𛷗��Ṿ?~0###Lc82` | `.` | `4` |
| whatwg vs parse_uri | `data://7c6R	9𧦩񆇝 L2@[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `53` | `.` |
