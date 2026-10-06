# Path / Special Chars Affect Host Extraction

**Description:** Special characters (tabs, spaces, commas, etc.) cause one parser to truncate the host at a different point than the other.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| whatwg vs legacy | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b` |
| whatwg vs legacy | `http://tB9maq36Xi3W0@93.59.72.404v䙜&@2mX0R2'5(023p?=66a2DgM` | `2mx0r2'5(023p` | `2mx0r2` |
| whatwg vs legacy | `ws://5Bwl0o1Q197LGAH:37K04G83WYx|bFJ8qZay736m94AQ~
uUx@-j-6.785-.7g6wf2`?#` | `-j-6.785-.7g6wf2`` | `-j-6.785-.7g6wf2` |
| whatwg vs legacy | `ftp://jV518{#@1.49.4.19:52`5oT2QOOhXI750M1638?` | `jv518{` | `jv518` |
| whatwg vs legacy | `data://6w0U03?#AP
8k50HN27@[69:28:cA:C:5a:0c:2:f]0o` | `6w0U03` | `6w0u03` |
| legacy vs url-parse | `ws://00v069@06'"StN7ld4v8.379l1|938#g` | `06'"stn7ld4v8.379l1|938` | `938` |
| legacy vs url-parse | `wss://0QJ:68@35006-kA:8175"W1FF503J0ba5pZP8k4=?#` | `35006-ka:8175"w1ff503j0ba5pzp8k4=` | `35006-ka:8175` |
| legacy vs url-parse | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751}JḤ
	?#` | `k9-2kr23.u.c.1s272-:751}jḤ��✉真𐍉𑃈𑁐𑊐2🏀Ⱍ
{g` | `k9-2kr23.u.c.1s272-:751` |
| legacy vs url-parse | `redis://ONx5Y5jZ7j2WNz58DIQ\242eva798m7SE/./@[B3:4:A:cF:8B:0f:7:0C]?#` | `onx5y5jz7j2wnz58diq\242eva798m7se` | `onx5y5jz7j2wnz58diq` |
| legacy vs url-parse | `redissNpalmfm://0'.茚ⳡ0^▒%/121@?#` | `0'.茚ⳡ0^▒%` | `0` |
| javascript-whatwg vs javascript-legacy | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4x.w04,b}391752316e5zvx99m` | `6a4x.w04,b` |
| javascript-whatwg vs javascript-legacy | `http://tB9maq@93.59.72.404v@2mX0R2'5(023p?=` | `2mx0r2'5(023p` | `2mx0r2` |
| javascript-whatwg vs javascript-legacy | `http://...@-17yr154ZzY'53FF895\` | `-17yr154zzy'53ff895` | `-17yr154zzy` |
| javascript-whatwg vs javascript-legacy | `ws://...@-j-6.785-.7g6wf2`?` | `-j-6.785-.7g6wf2`` | `-j-6.785-.7g6wf2` |
| javascript-whatwg vs javascript-legacy | `ftp://jV518{#` | `jv518{` | `jv518` |
| javascript-whatwg vs javascript-legacy | `chrome://...@dP~`Wj3l6317761` | `dp~` | `dP~`Wj3l6317761` |
| javascript-whatwg vs javascript-legacy | `data://36.65.0.102452...}j6393c3x0Gn783Do14?` | `36.65.0.102452%E7%A7%96%F0%A8%AD%82}j6393c3x0Gn783Do14` | `36.65.0.xn--102452-ur1p66994a` |
| javascript-whatwg vs javascript-parse-uri | `data://1jlw5x[a4...` | `1jlw5x` | `[a4` |
| javascript-whatwg vs javascript-parse-uri | `data://.)n+5l6zz6u06h57855po/...` | `.)n+5l6zz6u06h57855po` | `8h58b7𩷋𡥔𤸟
H1Go[EE` |
| javascript-whatwg vs javascript-parse-uri | `wss://[D:C:a1:cE:b:33:D:f]:42256/` | `[D` | `[d:c:a1:ce:b:33:d:f]` |
| rust-url vs php-parseurl | `wss://0j443x4EQ43r9k7Ae78\]Ⲉ'06@[0:d:2:f0:7:C8:3:c]:3-3F?#` | `0j443x4eq43r9k7ae78` | `[0:d:2:f0:7:C8:3:c]` |
| javascript-whatwg vs python-urllib3 | `data://787:  ᠠ...␹3F1@f:315...@U1D=y!c9A/.W#8` | `U1D=y!c9A` | `u1d=y!c9a` |
| go-net vs rust-url | `wss://iɌ!>╎F0u20T018h66tQ48027@52.6.7.276N8o604wh228Z3Y,7-@1?#` | `0.0.0.1` | `1` |
| perl-uri vs rust-url | `https://zy🀄...|a@2.6.29?#.47:1...` | `2.6.29` | `2.6.0.29` |
