# Control character stripping in authority

**Description:** One parser strips control characters from authority; the other preserves them percent-encoded.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `DB://` | `%0C` | `` |
| whatwg vs legacy | `Dmplatform://51XD2H6g9h@/../6𧇮Q怽:𪾚𸖦?` | `%04` | `` |
| whatwg vs legacy | `jms://w479N08g97DEC9zzt` | `%0E:630` | `:630` |
| whatwg vs legacy | `data://81C70pGo󱒲ݚ7` | `%0C` | `` |
| whatwg vs legacy | `data:///../𸢩ci6H49i4VJj@3.6.1.5:62` | `%18` | `` |
| whatwg vs legacy | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504` | `%0B` | `` |
| whatwg vs legacy | `acr://6jZQ򎰸䒽aS{P767go@:5/../` | `%0B:5` | `:5` |
| whatwg vs legacy | `fax://34*UG36.9-Q-n-0S.r1SZN.:2526` | `%0F` | `` |
| whatwg vs legacy | `DB://` | `%0C` | `` |
| whatwg vs legacy | `data:///./2▶7>����` | `|%10` | `|` |
| whatwg vs legacy | `data://81C70pGo𛊲�7) ঀG7@"59@tL4c98J-72..-CIO2rM:8��@/...?#` | `%0C` | `` |
| whatwg vs legacy | `data:///../񈦩ci6H49i4VJj@3.6.1.5:62��g?#` | `%18` | `` |
| whatwg vs legacy | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504񿏊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X(0A65` | `%0B` | `` |
| whatwg vs legacy | `DB://` | `%0C` | `` |
| whatwg vs legacy | `Dmplatform://51XD2H6g9h@/../6𧇮Q怽:𪾚𸖦?	􏟾􅑏⠞𩶩d#`U` | `%04` | `` |
| whatwg vs legacy | `jms://w479N08g97DEC9zzt 9758J󶻳㸷2Ygs@:630#󹹗)Ȩ_፨3{53u(#G8􃁺𖒎x⪙?` | `%0E:630` | `:630` |
| whatwg vs legacy | `data:///./2▶7>􇅁􆅉􏅦򚵛≼l@ᵪ[჻8򖼱Y򕌼񎉱11򽊷:0󿅫Ⓓ񟭑{~󰗐Ὂ𬄺99D+b7c4a16mM959U}hg -󰤒򓪙𠕝	`ᵊ┘03#` | `%10` | `` |
| whatwg vs legacy | `data://81C70pGo󱒲ݚ7) ᤞG7@"59@tL4c98J-72..-CIO2rM:8𥱂@/...?#` | `%0C` | `` |
| whatwg vs legacy | `data:///../𸢩ci6H49i4VJj@3.6.1.5:62􎩑g?#` | `%18` | `` |
| whatwg vs legacy | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504񜿊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X(0A65` | `%0B` | `` |
| whatwg vs legacy | `acr://6jZQ򎰸䒽aS{P767go@:5/../<$l0AAP4u4gRE8MqY1^Q55?#` | `%0B:5` | `:5` |
| whatwg vs legacy | `fax://34*UG36.9-Q-n-0S.r1SZN.:2526*󸁁Q􄴥8N@?#𦘓` | `%0F` | `` |
| whatwg vs legacy | `DB://
?H^~d:Da[89:51:F7:bA:C:5:C2:a5]:`V��𥒰🨛1🟐Fz1oE51Eae6Byy4T2q7?##ℳ#M@+5H` | `%0C` | `` |
| whatwg vs legacy | `Dmplatform://51XD2H6g9h@/../6񗲎��:����?	🨚🚏†񾲉d#`U` | `%04` | `` |
| whatwg vs legacy | `data://81C70pGo𙒲﬚7) ẠG7@"59@tL4c98J-72..-CIO2rM:8𓓂@/...?#` | `%0C` | `` |
| whatwg vs legacy | `DB://` | `%0C` | `` |
| whatwg vs legacy | `jms://w479N08g97DEC9zzt 9758J󼷳�롷𥢚𥠞𤢹𦫩:0񿥫Ⓝ��{~𘇐ᛂ🨺99D+b7c4a16mM959U}hg -𘈒󂹙𒉝	`ᴪ┘03#` | `%0E:630` | `:630` |
| whatwg vs legacy | `data://81C70pGo󄦶Ӛ7) ਞG7@"59@tL4c98J-72..-CIO2rM:8��@/...?#` | `%0C` | `` |
| whatwg vs legacy | `data:///../񋨩ci6H49i4VJj@3.6.1.5:62󻢡g?#` | `%18` | `` |
| whatwg vs legacy | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504󳏊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X(0A65` | `%0B` | `` |
| whatwg vs legacy | `acr://6jZQ􌢸𘢽 aS{P767go@:5/../<$l0AAP4u4gRE8MqY1^Q55?#` | `%0B:5` | `:5` |
| whatwg vs legacy | `fax://34*UG36.9-Q-n-0S.r1SZN.:2526*󀕁𔼥�@?#𡗃` | `%0F` | `` |
| whatwg vs deno | `DB://` | `%0C` | `` |
| whatwg vs deno | `Dmplatform://51XD2H6g9h@/../6𧇮Q怽:𪾚𸖦?	􏟾􅑏⠞𩶩d#`U` | `%04` | `` |
| whatwg vs deno | `jms://w479N08g97DEC9zzt 9758J󶻳㸷2Ygs
@:630#󹹗)Ȩ_፨3{53u(#G8􃁺𖒎x⪙?
` | `%0E:630` | `:630` |
| whatwg vs deno | `data:///./2▶7>􇅁􆅉􏅦򚵛
≼l@ᵪ[჻8򖼱Y򕌼񎉱11򽊷:0󿅫Ⓓ񟭑{~󰗐Ὂ𬄺99D+b7c4a16mM959U}hg -󰤒򓪙𠕝	`ᵊ┘03#` | `%0C` | `` |
| whatwg vs deno | `data://81C70pGo󱒲ݚ7) ᤞG7@"59@tL4c98J-72..-CIO2rM:8𥱂@/...?#` | `%0C` | `` |
| whatwg vs deno | `data:///../𸢩ci6H49i4VJj@3.6.1.5:62􎩑g?#` | `%18` | `` |
| whatwg vs deno | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504񜿊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X(0A65` | `%0B` | `` |
| whatwg vs deno | `acr://6jZQ򎰸䒽aS{P767go@:5/../<$l0AAP4u4gRE8MqY1^Q55?#` | `%0B:5` | `:5` |
| whatwg vs deno | `fax://34*UG36.9-Q-n-0S.r1SZN.:2526*󸁁Q􄴥8N@?#𦘓` | `%0F` | `` |
| whatwg vs trio | `DB://` | `%0C` | `` |
| whatwg vs trio | `Dmplatform://51XD2H6g9h@/../6𧇮Q怽:𪾚𸖦?	􏟾􅑏⠞𩶩d#`U` | `%04` | `` |
| whatwg vs trio | `jms://w479N08g97DEC9zzt 9758J󶻳㸷2Ygs
@:630#󹹗)Ȩ_፨3{53u(#G8􃁺𖒎x⪙?` | `%0E:630` | `:630` |
| whatwg vs trio | `data:///./2▶7>􇅁􆅉􏅦򚵛
≼l@ᵪ[჻8򖼱Y򕌼񎉱11򽊷:0󿅫Ⓓ񟭑{~󰗐Ὂ𬄺99D+b7c4a16mM959U}hg -󰤒򓪙𠕝	`ᵊ┘03#` | `|%10|` | `|` |
| whatwg vs trio | `data://81C70pGo󱒲ݚ7) ᤞG7@"59@tL4c98J-72..-CIO2rM:8𥱂@/...?#` | `%0C` | `` |
| whatwg vs trio | `data:///../𸢩ci6H49i4VJj@3.6.1.5:62􎩑g?#` | `%18` | `` |
| whatwg vs trio | `oidprosperoms-settings-airplanemode:///../p:H657@09.06.76.21:3504񜿊39|v&sl=2+l1&,&541,*|v9=2]/&\wL0:~`$5{&i)=8Y5hb'X(0A65` | `%0B` | `` |
| whatwg vs trio | `acr://6jZQ򎰸䒽aS{P767go@:5/../<$l0AAP4u4gRE8MqY1^Q55?#` | `%0B:5` | `:5` |
| whatwg vs trio | `fax://34*UG36.9-Q-n-0S.r1SZN.:2526*󸁁Q􄴥8N@?#𦘓` | `%0F` | `` |
