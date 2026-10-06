# Scheme appended to or mixed in authority

**Description:** One parser appends the scheme to authority field or one parser returns authority-only while other includes scheme prefix.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| radix (3) vs whatwg (4) | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9⪱3365-񝱴 KNi+*e!cI/1S2]Tjva9D{0?#󺯑` | `http` | `http:` |
| radix (3) vs whatwg (4) | `http://file://340`􏚐-MhGLd54l6GF33.1.75.6:	򬚱4 ~򚇔󺒉q􌕬𥦘(񰫉8󶌈񅋏⠃z񽜏H83A91v++6u_5nv'oZ6?#` | `file:` | `file` |
| radix (3) vs whatwg (4) | `https://https://J:G7	@9.95.9.93:60)%6M2UuZ9(Z3NX^yMO.9.?#88V66W[` | `https` | `https:` |
| radix (3) vs whatwg (4) | `http://ftp://5O4:8836@285-:775(V=g9M06zNR8TPfDh5Q3?#K` | `ftp` | `ftp:` |
| radix (3) vs whatwg (4) | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504⊋󈲙󋬢!⚚􅫕􆻽󠶏]#48-2Et'JUtEK0yt7B65C?#8Bq4YM1Oc9M=NQ` | `file` | `file:` |
| radix (3) vs whatwg (4) | `http://ftp://k3YON7E1bPA9FJa0k0K:o􍖸P􌕚@𩶆Ж⒑HI𽌋31᪡A𖮫4@.0816:8829󍲓469j7I870AW8q2a424J?#o` | `ftp:` | `ftp` |
| radix (3) vs whatwg (4) | `data://data://d󼀲s6銟B02nu784@:40 M򦷚!	/ytd8K6735NBNs4'38Cx?#` | `data` | `data:` |
| radix (3) vs whatwg (4) | `ftp://https://hVaV8O12996@9]󍈅$)zAj60O2bK5^Ne@ll[S6?#KXpr` | `https:` | `https` |
| legacy vs jsprim | `http://https://8L⍔
𛓜9F@[A:e:6:E:4d:e:f:d1]:4026≪𐰠𲄱὞ཀp1pP:R?#` | `https` | `https:` |
| legacy vs jsprim | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
≫3365-򇙴 KNi+*e!cI/1S2]Tjva9D{0?#𾯱` | `http` | `http:` |
| legacy vs jsprim | `http://file://340`𓻌-MhGLd54l6GF33.1.75.6:	𻂚4 ~𪡇𾢉q𓑍𩑸(񌢩𒄈𱓏␃z񟓏햠�Fv6u_5nv'oZ6?#` | `file` | `file:` |
| legacy vs jsprim | `wss://wss://3:@≫Љ.𛛂:48{0Od12L00s@ib6Oz1R2n?` | `wss` | `wss:` |

| legacy vs net | `%0B||oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504󧏊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X` | `%0B:5` | `:5` |
| legacy vs whatwg | `http://https://8L⸔𧓜9F@[A:e:6:E:4d:e:f:d1]:4026⥚򃊠𢔱ⲞU67~bj2A6N95`p1pP:R?#` | `https` | `https:` |
| legacy vs whatwg | `http://file://340`􏚐-MhGLd54l6GF33.1.75.6:	򬚱4 ~򚇔󺒉q􌕬𥦘(񰫉8󶌈񅋏⠃z񽜏H83A91v++6u_5nv'oZ6?#` | `file` | `file:` |
| legacy vs whatwg | `http://ftp://k3YON7E1bPA9FJa0k0K:o􍖸P􌕚@𩶆Ж⒑HI𽌋31᪡A𖮫4@.0816:8829󍲓469j7I870AW8q2a424J?#o` | `ftp` | `ftp:` |
| legacy vs whatwg | `http://Sh7/𦦎qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `sh7` | `Sh7` |
| legacy vs whatwg | `ws://ftp://yt27638jbF3V513SEa7:9yt[A:a:5d:C:eb:cd:C:b]:2673𡍯a04񬢱xw𥅫?#` | `ftp` | `ftp:` |

| go-net vs rust-url | `http://https://8L⏔
🗜9F@[A:e:6:E:4d:e:f:d1]:4026⩚🂨𠨱⬞U67~bj2A6N95`p1pP:R?#` | `https` | `https:` |
| go-net vs rust-url | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?C|🚫=;%2𖦶𯛪🛁JC3gO32V12o3k1334w!?#3]<7` | `file` | `file:` |
| go-net vs rust-url | `http://ftp://3Z28🟄✕═80155jYLqM1BW/[4:a:E:F4:2F:6:B:eF]92商>📥⬤🗇𠺥Su(6t25J0iwxw21j30]?♧#"_0Z3` | `ftp:` | `ftp` |
| go-net vs rust-url | `https://https://J:G7	@9.95.9.93:60)%6M2UuZ9(Z3NX^yMO.9.?#88V66W[` | `https` | `https:` |
| go-net vs rust-url | `wss://wss://3:@⩛Љ.🗜:48{0Od12L00s@ib6Oz1R2n?` | `wss:` | `wss` |
| go-net vs rust-url | `http://ftp://5O4:8836@285-:775(V=g9M06zNR8TPfDh5Q3?#K` | `ftp` | `ftp:` |
