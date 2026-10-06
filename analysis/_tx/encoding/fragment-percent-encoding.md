# Fragment percent-encoding

**Description:** One parser percent-encodes fragment while other uses raw unicode or different encoding

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs parse_uri | `mms://7l90:\M5.i91-E3-4328c.-3g:𣑰#÷愤񑢬�` | `#%C3%B7%E6%84%A3%F4%86%AC%A4` | `#4` |
| whatwg vs uri_parse | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⚪3365-�� KNi+*e!cI/1S2]Tjva9D{0?#𾮱` | `#%F3%BA%AF%91` | `#43w5%7A` |

| whatwg vs node-url | `unknown` | `#-,%31{` | `#-,%31%7B` |
| whatwg vs node-url | `unknown` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| whatwg vs posix | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9` | `#󺯑` | `#%F3%BA%AF%91` |
| whatwg vs posix | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<` | `#-,%31{` | `#-,%31%7B` |
| whatwg vs posix | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e` | `#	6&84{?#gStt` | `#6&84{?#gStt` |
| whatwg vs posix | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?` | `#󳦉` | `#%F3%B3%A6%89` |
| whatwg vs posix | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| whatwg vs node-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪫3365-ؾb KNi+*e!cI/1S2]Tjva9D{0?#󋾱` | `#󋾱` | `#%F3%BA%AF%91` |
| whatwg vs node-url | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?�� D?0~폳�5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| whatwg vs node-url | `ws://do2ycs037T󹕢2s3k@1𖽂2⊷3⦷8y5/./(28KZ3tq83U3y3lg?#󃻉` | `#󃻉` | `#%F3%B3%A6%89` |
| whatwg vs go | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| whatwg vs go | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| whatwg vs go | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢
!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| whatwg vs go | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7򅎩2򗪞󊦱09cRGS67z3kjyg#` | `#7%F2%85%8E%A92%F2%97%AA%9E%F3%8A%A6%B109cRGS67z3kjyg#` | `#7򅎩2򗪞󊦱09cRGS67z3kjyg#` |


| radix (3) vs whatwg (4) | `data://3࢏#ㅵ̇!2Oun0Ya1692h3~f4u4T?#` | `#%E3%87%B5%0307!2Oun0Ya1692h3~f4u4T?#` | `#ㅵ̇!2Oun0Ya1692h3~f4u4T?#` |
| radix (3) vs whatwg (4) | `data://ZH5}+𔖮<񲔈v8K3u46@[88:9F:b:58:29:e:f4:5D]:1242𩈇

1@Zg4)7t8y288$8Ko03?#󘼷
ႄ縐` | `#%F4%89%B0%804:%E2%B0%89%F3%BE%A6%8F%E2%93%9D%F1%83%9B%AC1@[8C:E0:b:E:A:c:f2:bE]91b%E2%A5%B259uw0=?#` | `#󾺀
4:ⲉ􋪏⍄᲻�1@[8C:E0:b:E:A:c:f2:bE]91b╲
59uw0=?#` |
| radix (3) vs whatwg (4) | `ftp://vKb8N8Cf03S89#��q33979@1.49.4.19:52`5oT2QOOhXI750M1638?#` | `#%F3%B7%A7%8Dq33979@1.49.4.19:52%605oT2QOOhXI750M1638?#` | `#��q33979@1.49.4.19:52`5oT2QOOhXI750M1638?#` |
| radix (3) vs whatwg (4) | `file://R43P8l8oV3l4629⁴#򺫷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `#%F4%84%A8%B7;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `#򺫷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` |
| radix (3) vs whatwg (4) | `http://PJ4OvFF90T7∌#`I8@qf0u05.V-5l64801.0v:07591C634Gqdx8w91817F1v?#` | `#%60I8@qf0u05.V-5l64801.0v:07591C634Gqdx8w91817F1v?#` | `#`I8@qf0u05.V-5l64801.0v:07591C634Gqdx8w91817F1v?#` |
| legacy vs ada | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| legacy vs ada | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| legacy vs ada | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e#	6&84{?#gStt` | `#	6&84{?#gStt` | `#6&84{?#gStt` |
| legacy vs ada | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?#󳦉` | `#󳦉` | `#%F3%B3%A6%89` |
| legacy vs ada | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢
!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| legacy vs ada | `https://https://51򈖤u
𡠳󳓪	#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?
#` | `#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?%0B#` | `#gYIkh15L@:%5E4;74cr3:6%7C169g4-fN5R56?%0A#` |
| legacy vs ada | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| legacy vs ada | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| legacy vs ada | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e#	6&84{?#gStt` | `#	6&84{?#gStt` | `#%096&84%7B?#gStt` |
| legacy vs ada | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?#󳦉` | `#󳦉` | `#%F3%B3%A6%89` |
| legacy vs ada | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢%0A!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| legacy vs ada | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪫3365-�74 KNi+*e!cI/1S2]Tjva9D{0?#��` | `#��` | `#%F3%BA%AF%91` |
| legacy vs ada | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѲ<
%0E%09o%30%33?���?🗲5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| legacy vs ada | `data://S1u68��󴢍_Gq8@80.6.66/./.09:Ҭ��e#	6&84{?#gStt` | `#	096&84%7B?` | `#6&84{?#gStt` |
| legacy (1) vs ada (2) | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| legacy (1) vs ada (2) | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| legacy (1) vs ada (2) | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢
!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| ada (2) vs net (3) | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| ada (2) vs net (3) | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| ada (2) vs net (3) | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢
!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| legacy vs ada | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9

⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `#󺯑` | `#%F3%BA%AF%91` |
| legacy vs ada | `file:/%2FV%546%58%72C%0D_382IV%33L%4B%6Az69%40%72853QAr%61%6Av013%32N8%67em%3A0%35%30zѴ<
%0E%09o%30%33?򉮫D?0~􏳢5#-,%31{` | `#-,%31{` | `#-,%31%7B` |
| legacy vs ada | `data://S1u68𩩹𤊭Gq8@80.6.66/./.09:Ҭ򇛣e#	6&84{?#gStt` | `#%096&84%7B?#gStt` | `#6&84{?#gStt` |
| legacy vs ada | `ws://do2ycs037T󹕢s3k@1𦭂3⦷8y5/./(28KZ3tq83U3y3lg?#󳦉` | `#󳦉` | `#%F3%B3%A6%89` |
| legacy vs ada | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢
!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et%27JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` |
| legacy vs ada | `https://https://51򈖤u
𡠳󳓪	#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?
` | `#gYIkh15L@:^4;74cr3:6|169g4-fN5R56?%0B#` | `#gYIkh15L@:%5E4;74cr3:6%7C169g4-fN5R56?%0A#` |
| legacy vs ada | `file://a9HC5V03i92S3b9z330/..G⪬#𨵙$rI3a714Q󹢐;˂68#YS4P ?#` | `#%F0%A8%B5%99$rI3a714Q%F3%B9%A2%90;%15%CB%8268#YS4P%20?#` | `#𨵙$rI3a714Q󹢐;˂68#YS4P%20?#` |
| legacy vs ada | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7򅎩2򗪞󊦱09cRGS67z3kjyg#` | `#7%F2%85%8E%A92%F2%97%AA%9E%F3%8A%A6%B109cRGS67z3kjyg#` | `#7򅎩2򗪞󊦱09cRGS67z3kjyg#` |
| legacy vs ada | `ws://Z9I6Z786V06#󹸁3<򷗩@􈞦➷I󺭤2􏹽@21.52.75.69:1{𠾾􎙻
?#` | `#%F3%B9%B8%813%3C%F2%B7%97%A9@%F4%88%9E%A6%E2%9E%B7I%F3%BA%AD%A42%F4%8F%B9%BD@21.52.75.69:1{%F0%A0%BE%BE%F4%8E%99%BB?#` | `#󹸁3%3C򷗩@􈞦➷I󺭤2􏹽@21.52.75.69:1%7B𠾾􎙻%0A?#` |
