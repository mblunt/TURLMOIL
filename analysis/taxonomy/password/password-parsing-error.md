# Password parsing error

**Description:** One parser fails to correctly extract password, returning corrupted or malformed data

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2�À³#?󳃶À¬À¼` | `p` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs legacy | `https://9e6𩱗
2r2:8OⓇ0S%B@29.5.42.92:4𗕶@��🮫41gFX2723Lo894?376
]
:
#E22NXKX36` | `8O%E2%93%870S%B%4029.5.42.92%3A4%F0%A7%8E%B6` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs parse_uri | `http://3H35MD6E3O59lR61743:9@7。67.88.221ʲ��4?46⟼ oX77#I@o57` | `9` | `6T%F3%B4%89%927y2%1E%F1%80%BD%9E%F1%A4%B0%AB%04%F4%82%8C%99%E2%84%B810m5E%F1%B5%A2%82` |
| whatwg vs custom | `ms­ wh©t¥board-cm¤://ZEÁ1IoºzvL14µ8:SQ6@[0:1¸:BE:d6:0a:6B:b5:05]±962&k8Á0005hi6q0xn¹-\F?	p��˃Z#` | `SQ6` | `%33*%12�12` |
