# Fragment unicode stripping

**Description:** One parser strips or corrupts raw unicode in fragment while the other preserves or percent-encodes it

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⚪3365-�� KNi+*e!cI/1S2]Tjva9D{0?#𾮱` | `#𾮱` | `#` |
| whatwg vs legacy | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9` | `#󺯑` | `#` |
| whatwg vs legacy | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9` | `#󺯑` | `#%F3%BA%AF%91` |
| whatwg vs ada | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⪱3365-↝᭱̄ KNi+*e!cI/1S2]Tjva9D{0?#𖾱` | `#𖾱` | `#` |
| whatwg vs node-url | `unknown` | `#󺯑` | `#%F3%BA%AF%91` |
| whatwg vs node-url | `unknown` | `#󳦉` | `#%F3%B3%A6%89` |
| whatwg vs posix | `file://a9HC5V03i92S3b9z330/..G⪬` | `#
#%F0%A8%B5%99$rI3a714Q%F3%B9%A2%90;%15%CB%8268#YS4P%20?#` | `#񶆹$rI3a714Q􊖠;˂68#YS4P%20?#` |
| whatwg vs posix | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478` | `#7%F2%85%8E%A92%F2%97%AA%9E%F3%8A%A6%B109cRGS67z3kjyg#` | `#7힅��2힗���f09cRGS67z3kjyg#` |
| whatwg vs go | `ws://do2ycs037T򡙢s3k@1𢓲3⊷3y5/./(28KZ3tq83U3y3lg?#􃫉` | `#􃫉` | `#%F3%B3%A6%89` |
| whatwg vs legacy | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪫3365-񦢴 KNi+*e!cI/1S2]Tjva9D{0?#󾢱` | `#󾢱` | `#%F3%BA%AF%91` |
| whatwg vs legacy | `ws://do2ycs037T􌷒s3k@1𩥍θ�8y5/./(28KZ3tq83U3y3lg?#􌳩` | `#􌳩` | `#%F3%B3%A6%89` |
| radix (3) vs whatwg (4) | `ftp://jV518{#��q33979@1.49.4.19:52`5oT2QOOhXI750M1638?#` | `#%F3%B7%A7%8Dq33979@1.49.4.19:52%605oT2QOOhXI750M1638?#` | `#��q33979@1.49.4.19:52`5oT2QOOhXI750M1638?#` |


| legacy vs ada | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⋋𝊉𛒢
!⚚��𕯻𚭿]
#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| legacy vs whatwg | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7𽂎��𢦦09cRGS67z3kjyg#` | `#7%F2%85%8E%A92%F2%97%AA%9E%F3%8A%A6%B109cRGS67z3kjyg#` | `#7𽂎��𢦦09cRGS67z3kjyg#` |
| legacy vs whatwg | `wss://DZ7103w4zf2n48C9NV4#⛋
n74Eh54gx@7k3tnJ9848z4p9s5NZk9780}90rQ?` | `#%E2%8F%8Bn74Eh54gx@7k3tnJ9848z4p9s5NZk9780}90rQ?` | `#⛋
n74Eh54gx@7k3tnJ9848z4p9s5NZk9780}90rQ?` |
