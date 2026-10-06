# Host parsing differences

**Description:** Divergent parsing of IP addresses in authority

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs parse_uri | `mms://7l90:\M5.i91-E3-4328c.-3g:􃁰#÷愺󻂤` | `7l90` | `lm5E4nQ8-6o.6Q0Bij6:4` |
| whatwg vs parse_uri | `ws://c6F9񆺗/...}󾦌竏#0.;i98º@n1FL6Po:226⌤GJq344(tj.2E603ED`1?O|0􏯄.U` | `xn--c6f9-t973a` | `lm5E4nQ8-6o.6Q0Bij6:4` |
| whatwg vs php-http | `data://7c6R	9��𖮍
L2@[70:d:C:f3:84:CA:8:a]:53\405oPoRsyy352r1q1?` | `[70:d:c:f3:84:ca:8:a]:53` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99:32206` |
| whatwg vs php-http | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99:32206` |
