# Punycode encoding differences

**Description:** One parser applies punycode (xn--) encoding to internationalized domain names; the other preserves raw unicode.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| radix (3) vs whatwg (4) | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?#󳦉` | `do2ycs037T󹕢s3k@1𦭂3⦷8y5` | `xn--138y5-2x5cz9190b` |
| radix (3) vs whatwg (4) | `http://jn7Lq懏0?􋍎7^32	@󹕔⊧@。93-D。CEsHZE2Ko2v:򥜰𨔵𩋇\v)핦_𫁾	}缣9󳷕?⎫39R0TCc2d?am􀙰貀#` | `xn--jn7lq0-mm6l` | `jn7Lq懏0` |
| radix (3) vs whatwg (4) | `file://a9HC5V03i92S3b9z330/..G⪬#𨵙$rI3a714Q󹢐;˂68#YS4P ?#` | `a9hc5v03i92s3b9z330` | `a9HC5V03i92S3b9z330` |
| legacy vs jsprim | `http://558:767332:𖶗@Ug0pl866281hd.Mj7-N񸱧᪉␔?#k` | `558:767332:𖶗@Ug0pl866281hd.Mj7-N񸱧᪉␔` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` |
| legacy vs node | `http://558:767332:𖺗@Ug0pl866281hd.Mj7-N𨑧Ᲊ⑲?#k` | `ug0pl866281hd.Mj7-N𨑧Ᲊ⑲` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` |

| go-net vs rust-url | `http://558:767332:𮺗@Ug0pl866281hd.Mj7-N𝝧ẉ␄?#k` | `558:767332:𮺗@Ug0pl866281hd.Mj7-N𝝧ẉ␄` | `ug0pl866281hd.xn--mj7-n20-u52a34516f` |
| go-net vs rust-url | `ws://do2ycs037T񿗢s3k@1𶻌3⩧ȸy5/./(28KZ3tq83U3y3lg?#🛩` | `do2ycs037T񿗢s3k@1𶻌3⩧ȸy5` | `xn--138y5-2x5cz9190b` |
| go-net vs rust-url | `ftp://9𠨴\�bad4m0h2R84jkVdTKx⏒𥗷Ω𞇓[Df:0:Ac:7:7B:d2:1c:d]:2315 71i|=4BLux0Vb1D7B34?#` | `xn--9-ro8w` | `9𠨴\�bad4m0h2R84jkVdTKx⏒𥗷Ω𞇓[Df:0:Ac:7:7B:d2:1c:d]:2315 71i|=4BLux0Vb1D7B34` |
