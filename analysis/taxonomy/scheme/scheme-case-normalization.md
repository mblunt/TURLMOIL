# Scheme case normalization

**Description:** One parser lowercases the scheme while the other preserves its case

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| go-net (3) vs rust-url (4) | `Ktoolms-settings-screenrotationms-powerpointpaparazzilWGrediss://Keꇣ䩤x42@e5@Q.D	:346ь́ы.
@Q133Jx3~(R5De'4M3dE?#` | `ktoolms-settings-screenrotationms-powerpointpaparazzilwgrediss` | `Ktoolms-settings-screenrotationms-powerpointpaparazzilWGrediss
` |
| go-net (3) vs rust-url (4) | `jabberXsieveIms-getofficeTsmsnihgmodempms-settings-wifi://98hIAuC60ZeFJep0N04/../8DFW1TJ--6-.-s8M.-51..7L2:58ъ́Rs9n22MLc` | `jabberxsieveims-getofficetsmsnihgmodempms-settings-wifi` | `jabberXsieveIms-getofficeTsmsnihgmodempms-settings-wifi` |
| go-net (3) vs rust-url (4) | `E+thismessage:////O3x7t55š́ʙ̔̅/D
5bwO8@x..-61:7830i8529J676yi4MjO3891?#` | `e+thismessage` | `E+thismessage` |
| go-net (3) vs rust-url (4) | `datad1h61h67:00M5@02.55.19.28:893<ڒ̃ش̃b▭ a6325Y;08j0Y3dEY7=6?#rb` | `datad1h61h67` | `datad1h61h67` |
| go-net (3) vs rust-url (4) | `oUPgdlna-playsinglersftp://K85Kt2hAo8N3k2o3WR2x5[f:2:d:B4:FE:7e:5c:eA]3414
ع̣̇̉̒̓̕''s1F]J63px557D5@8?2C` | `oupgdlna-playsinglersftp` | `oUPgdlna-playsinglersftp` |
| go-net (3) vs rust-url (4) | `ms-settings-screenrotationms-settings-privacyF:/\/\q:1EISV3f6U93D1877pT7@e0TỮ hڑ̃:0267#½ sbr-BC981o1?Xṷ̸̡̧̠̅̿7#^` | `ms-settings-screenrotationms-settings-privacyf` | `ms-settings-screenrotationms-settings-privacyF` |
| go-net (3) vs rust-url (4) | `Kdatagpresj://s5959575`H滍̉ 0
j5Q3@EL.5-r.75v54X.Mkz2W0860_6*١̅,Iˣ 9115v0Ux233$xpqw452~?#07` | `kdatagpresj` | `Kdatagpresj` |
| go-net (3) vs rust-url (4) | `ms-walk-to6 info://4
y7W੮̀;Ḛ<⪪ 8ʙ̱
	22Dq@[42:9d:EA:39:a:df:4D:FD]{]C6@2Y@+d9=';aA&nM"25&#R` | `ms-walk-to6	info` | `ms-walk-to6 info` |
| whatwg vs ada | `redissNpalmfm://0'.茚⋡0^▒%/121@[6:e:c9:bB:3:80:b3:6b]:2348󨩌	+yA81Y*9l90gP8004{T?#{^nsGu` | `redissNpalmfm:` | `redissnpalmfm:` |
| whatwg vs ada | `BBiris://X9HW@K9-2kr23.u.C.1s272-:751}JḤ􀭥✉8	󟝆󄳉󑦐2􎰆⠝	0{` | `bbiris:` | `BBiris:` |
| whatwg vs ada | `Bms-settings-location2notesfenrollmentrcid://X6m缌52@rt.:349=h6+r!eedready𢥻elsims-066qEb{t05@7?#` | `bms-settings-location2notesfenrollmentrcid:` | `Bms-settings-location2notesfenrollmentrcid:` |
| whatwg vs ada | `E+thismessage:////O3x7t55򁟐𩌅/D` | `E+thismessage:` | `e+thismessage:` |
| whatwg vs ada | `firsKNN0I5o4b1st-run-pen-experience://9TGF61ᄕ
󲚫7J㼭5⁷07bnil@58.2.90.51:5244b65t15@?#` | `firsknn0i5o4b1st-run-pen-experience:` | `firsKNN0I5o4b1st-run-pen-experience:` |
| whatwg vs ada | `dataD1h61H67:00M5@02.55.19.28:893<𢑗𤿱b▭a6325Y;08j0Y3dEY7=6?#rb` | `datad1h61h67:` | `dataD1h61H67:` |
| whatwg vs ada | `ms-settings-screenrotationms-settings-privacyF:/\/\q:1EISV3f6U93D1877pT7@e0TỮh񢁏:0267#꼓sbr-BC981o1?󌙟㾆7#^` | `ms-settings-screenrotationms-settings-privacyF:` | `ms-settings-screenrotationms-settings-privacyf:` |
