# Multiple hash handling

**Description:** One parser uses first # as fragment boundary, other uses last # in the URL

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#43w5%7A` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#!` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#󺯑` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#3]<7` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#g` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#1` |
| parse_uri vs uri_parse | `p/drmmaps풑mongodbocf://2i9a4/...5c8V1򁱲	6Y7ltv:8799􍊘?##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `##e𠃴z񲩘᫪f!#ᅣp膾T# P#𥄱` | `#ASE91bL)` |
| parse_uri vs uri_parse | `ws%73%3A%2F/%39%63D%33%362a%4Af1'𫐾􄴽2o@%79r%59.69ENq%76.i%34xp%58%30x4%3A%30%313?#!%35AN>|_` | `#!%35AN>|_` | `#43w5%7A` |
| parse_uri vs uri_parse | `ws%73%3A%2F/%39%63D%33%362a%4Af1'𫐾􄴽2o@%79r%59.69ENq%76.i%34xp%58%30x4%3A%30%313?#!%35AN>|_` | `#!%35AN>|_` | `#!` |
| parse_uri vs uri_parse | `ws%73%3A%2F/%39%63D%33%362a%4Af1'𫐾􄴽2o@%79r%59.69ENq%76.i%34xp%58%30x4%3A%30%313?#!%35AN>|_` | `#!%35AN>|_` | `#󺯑` |

| whatwg vs legacy | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9` | `#󺯑` | `##e𠄴z�뚚ࢫf!#ᕣp릾哄#%20P#�퉱` |
| whatwg vs go | `https://https://51𡠤u
𩒪󳳪	#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?
#` | `#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?%0B#` | `#gYIkh15L@:%5E4;74cr3:6%7C169g4-fN5R56?%0A#` |
| whatwg vs legacy | `geo://168=~#𫔌􌲢I𗦘^lE𣓃9846Hk31:115t,걙0E(L0Z0h5)33P35'N56?#RE6+=` | `#%F0%A8%B5%99$rI3a714Q%F3%B9%A2%90;%15%CB%8268#YS4P%20?#` | `#𪆙$rI3a714Q􌲢;˂68#YS4P ?#` |
