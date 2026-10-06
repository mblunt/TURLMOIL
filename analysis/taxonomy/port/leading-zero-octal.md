# Leading zero port parsing (octal vs decimal)

**Description:** Ada interprets leading-zero ports as octal while Python converts to decimal

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| ada vs python | `https://example.com:0130/` | `0130` | `88` |
| ada vs python | `https://example.com:068/` | `068` | `56` |
| whatwg vs node-url | `unknown` | `48` | `048` |
| whatwg vs node-url | `unknown` | `6` | `06` |
| whatwg vs node-url | `unknown` | `70` | `0070` |
| whatwg vs node-url | `unknown` | `25` | `025` |
| whatwg vs node-url | `unknown` | `5` | `05` |
| whatwg vs node-url | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `48` | `048` |
| whatwg vs node-url | `dntp://891J7F짱ޯz3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
| whatwg vs node-url | `ftp://PfZV󹯅32OD6@.Q.TO.kdzL55-:03?#` | `3` | `03` |
| whatwg vs node-url | `ipps://68vOdk10D5e52򠣿7^𠓿)𪶿830hW36z6K1@36.38.8.55:03/...94710:093xSn8tPVC:3n9?#` | `3` | `03` |
| whatwg vs node-url | `http://b4w3Y148BYw7fI42􅾃󼝯𣙳0𩆏(󇩊5♆𣬜u2f@5J440.NLhA:0070\3YQ50-[lB1921007Z?#` | `70` | `0070` |
| whatwg vs node-url | `ws://V1112A*C"8JvMw8HUdmO3j7Mi@[e:B5:f1:e:a6:27:E:B]:025?#` | `25` | `025` |
| whatwg vs node-url | `wss://ElF679QRJ8wK8G 78b7a@1-2:05/.3J3f?#` | `5` | `05` |
| whatwg vs node-url | `ldaps://EE0:L3@@X-4-.:0956/./8򉕦,▁8?u#8u[(l#?t` | `956` | `0956` |
| whatwg vs node-url | `ms-spd://r7EOU:k2@8:017/..⊻}#?AX9'###DeD쫴K#G5` | `17` | `017` |
| whatwg vs node-url | `ftp://Ym178106R1T31cyT15p0:0614/...񋣳<⏝*4휳ᆖ=῟>򤫘@fzy119.6974nC2oo51?2#u2YGW?99_` | `614` | `0614` |
| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `48` | `048` |
| whatwg vs legacy | `dntp://891J7F짱ޯz3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
| whatwg vs legacy | `ftp://PfZV󹯅32OD6@.Q.TO.kdzL55-:03?#` | `3` | `03` |
| whatwg vs legacy | `ipps://68vOdk10D5e52򠣿7^𠓿)𪶿830hW36z6K1@36.38.8.55:03/...94710:093xSn8tPVC:3n9?#` | `3` | `03` |
| whatwg vs legacy | `http://b4w3Y148BYw7fI42􅾃󼝯𣙳0𩆏(󇩊5♆𣬜u2f@5J440.NLhA:0070\3YQ50-[lB1921007Z?#` | `70` | `0070` |
| whatwg vs legacy | `ws://V1112A*C"8JvMw8HUdmO3j7Mi@[e:B5:f1:e:a6:27:E:B]:025?#` | `25` | `025` |
| whatwg vs legacy | `wss://ElF679QRJ8wK8G 78b7a@1-2:05/.3J3f?#` | `5` | `05` |
| whatwg vs legacy | `ldaps://EE0:L3@@X-4-.:0956/./8򉕦,▁8?u#8u[(l#?t` | `956` | `0956` |
| whatwg vs legacy | `ms-spd://r7EOU:k2@8:017/..⊻}#?AX9'###DeD쫴K#G5` | `17` | `017` |
| whatwg vs legacy | `ftp://Ym178106R1T31cyT15p0:0614/...񋣳<⏝*4휳ᆖ=῟>򤫘@fzy119.6974nC2oo51?2#u2YGW?99_` | `614` | `0614` |
| whatwg vs legacy | `ftp:// Q@9.69.07.07:03\𴭗④07180G!v5N2v2@P3hng?#` | `3` | `03` |
| whatwg vs legacy | `unreal://0B7qGd3O􏍝@6em4lUnp6e48w:020/...'1Y03u3O5Rzj7X2LiLg?#` | `20` | `020` |
| whatwg vs legacy | `irc://8G45bkV06@-h--.1.-9kaeOt1nRj4:000/..74Xexu6_3?#` | `0` | `000` |
| whatwg vs legacy | `ftp://nzhd0QPNSo7Rh6q0k4:087/...7M5@:05@0󔭀☨󾠘񾨇􁫸낂Щ󛧓󰉆2H56xj05D6F6E19`xKN?􎍻󰘪8(#/` | `87` | `087` |
| whatwg vs legacy | `data://8:⫂8{795@03｡6｡6.51:0637/ᵣ?#` | `637` | `0637` |
| whatwg vs legacy | `http://K1in61g55q616975HBK✶=9!K9W7v@9.5.98.0:057\2431O7u273kY-1]y1U7?#` | `57` | `057` |

| whatwg vs legacy | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `48` | `048` |
| whatwg vs legacy | `dntp://891J7F짱ޯz3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
| whatwg vs legacy | `ftp://PfZV󹯅32OD6@.Q.TO.kdzL55-:03?#` | `3` | `03` |
| whatwg vs legacy | `ipps://68vOdk10D5e52򠣿7^𠓿)𪶿830hW36z6K1@36.38.8.55:03/...94710:093xSn8tPVC:3n9?#` | `3` | `03` |
| whatwg vs legacy | `http://b4w3Y148BYw7fI42􅾃󼝯𣙳0𩆏(󇩊5♆𣬜u2f@5J440.NLhA:0070\3YQ50-[lB1921007Z?#` | `70` | `0070` |
| legacy vs node | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `48` | `048` |
| legacy vs node | `dntp://891J7F짱ޯz3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
| legacy vs node | `ftp://PfZV󹯅32OD6@.Q.TO.kdzL55-:03?#` | `3` | `03` |
| legacy vs node | `ipps://68vOdk10D5e52򠣿7^𠓿)𪶿830hW36z6K1@36.38.8.55:03/...94710:093xSn8tPVC:3n9?#` | `03` | `3` |
| legacy vs node | `http://b4w3Y148BYw7fI42􅾃󼝯𣙳0𩆏(󇩊5♆𣬜u2f@5J440.NLhA:0070\3YQ50-[lB1921007Z?#` | `70` | `0070` |
| legacy vs rust | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `48` | `048` |
| legacy vs rust | `dntp://891J7F짱ޯz3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
| legacy vs rust | `ftp://PfZV󹯅32OD6@.Q.TO.kdzL55-:03?#` | `3` | `03` |
| legacy vs rust | `ipps://68vOdk10D5e52򠣿7^𠓿)𪶿830hW36z6K1@36.38.8.55:03/...94710:093xSn8tPVC:3n9?#` | `3` | `03` |
| legacy vs rust | `http://b4w3Y148BYw7fI42􅾃󼝯𣙳0𩆏(󇩊5♆𣬜u2f@5J440.NLhA:0070\3YQ50-[lB1921007Z?#` | `0070` | `70` |
| legacy vs ada | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gֆ釈8♽5M𜃔?1?󻍋4?&1?󻍋4?` | `48` | `048` |
| legacy vs ada | `dntp://891J7F짱챯z3>3D35@74.41.6.12:06/../975dnR310x$8Pvd@0Mq?` | `6` | `06` |
