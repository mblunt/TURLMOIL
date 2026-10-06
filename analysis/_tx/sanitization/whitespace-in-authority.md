# Whitespace / Newline in Authority Section

**Description:** A URL containing whitespace (space, tab, newline, etc.) in the authority section causes parsers to disagree on where the userinfo ends and the host begins, or where the host ends entirely.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-uri vs rust-url | `https://SY37q09Gi
윎3@7R.--qbX6r5.V-/...:0
?#` | `SY37q09Gi` | `7r.--qbx6r5.v-` |
| java-uri vs rust-url | `https://p
󺖤⌚󦄎@.-/...D05.83vHl77qW0qM8BBw7TL1?#` | `p` | `.-` |
| java-uri vs rust-url | `dtn://D8G87164Inh82m18M94
𪱿m3n4@3o.-2-bi35N31C8-8R94218ia44no156/rn]1k3!y)?#` | `3o.-2-bi35N31C8-8R94218ia44no156` | `D8G87164Inh82m18M94` |
| java-uri vs rust-url | `ftp://c7ZE
`12@9FP.8.108a6Es0mNc958171BTV3y_8o2xeOkZgw6pN#` | `9fp.8.108a6es0mnc958171btv3y_8o2xeokzgw6pn` | `c7ZE` |
| js-legacy vs java-uri | `https://SY37q09Gi
윎3@7R.--qbX6r5.V-/...:0
?#` | `SY37q09Gi` | `7r.--qbx6r5.v-` |
| js-legacy vs java-uri | `https://p
󺖤⌚󦄎@.-/...D05.83vHl77qW0qM8BBw7TL1?#` | `.-` | `p` |
| js-legacy vs java-uri | `dtn://D8G87164Inh82m18M94
𪱿m3n4@3o.-2-bi35N31C8-8R94218ia44no156/rn]1k3!y)?#` | `3o.-2-bi35n31c8-8r94218ia44no156` | `D8G87164Inh82m18M94` |
| js-legacy vs python-yarl | `data://3nUoVw3822
g⥇⁲*@ 9dKV9DL0?` | `` | ` 9dkv9dl0` |
| elixir-uri vs python-yarl | `ws://R6tBj668463bSfmPR:737VaU02NqLv55OL712@68.38.1.241067	𚃁	9p?#` | `68.38.1.241067	𚃁	9p` | `68.38.1.241067𚃁9p` |
| elixir-uri vs python-yarl | `telnet://Z4
Ἔ4E/../6111D44@00?#` | `Z4
Ἔ4E` | `z4ἤ4e` |
| elixir-uri vs python-urllib3 | `ws://R6tBj668463bSfmPR:737VaU02NqLv55OL712@68.38.1.241067	𚃁	9p?#` | `68.38.1.241067	𚃁	9p` | `68.38.1.241067𚃁9p` |
| java-uri vs rust-url | `https://SY37q09Gi
...@7R.--qbX6r5.V-/...` | `SY37q09Gi` | `7r.--qbx6r5.v-` |
| java-uri vs rust-url | `ws://qr0S81N0W9b3frlJo3
...@f49HI-PC20-6uAIj｡jf:173` | `qr0S81N0W9b3frlJo3` | `f49hi-pc20-6uaij.jf` |
| js-whatwg vs java-uri | `telnet://Z4
Ἔ4E/../6111D44@00...` | `Z4%E1%BE%9C4E` | `Z4` |
| js-whatwg vs java-uri | `ms-secondary-screen-setup://...@G77k4t
⧝🈎怓5...` | `G77k4t%0E%E2%9B%9D%F0%9B%80%8E%E6%82%935%126D1%18%D1%A4%F4%85%AF%A7oA33a2ZL{722` | `G77k4t` |

| java-galimatias vs elixir-uri | `wss://2dCf58OlY:@	ᇰX8	ᵡ
Y󋘂:101L...` | `	ᇰX8	ᵡ
Y󋘂` | `xn--x8-8zc532p` |
| java-galimatias vs elixir-uri | `http://H0x5
陇9]kv*@.H7vQ-hy.-.O5fx7.R6:9377...` | `.H7vQ-hy.-.O5fx7.R6` | `h0x5` |
| java-galimatias vs elixir-uri | `ftp://SI
Ȇ
;0@319:264e9uSli906u5t39uea7?#` | `319` | `si` |
| java-galimatias vs elixir-uri | `http://T0a␉Rqq/.@7F03h6m0HuVI37sCrXz:1284...` | `xn--t0arqq-r85c` | `T0a␉Rqq` |
| java-net-url vs python-urllib3 | `file://085X...@W9I579-60L-S99j:64\n...@G?#9Ea1` | `g` | `W9I579-60L-S99j` |
| java-net-url vs python-urllib3 | `http://TB+\n6j5gjA7zb5@8.{unicode}c ...?#` | `TB+` | `8.𠬚🈎ϑ5𘸼 𭹓...` |
| java-net-url vs python-urllib3 | `ftp://07tCn99593539lnB\nZ...@0.JM18/...` | `0.jm18` | `07tCn99593539lnB䔤` |
| java-net-url vs python-urllib3 | `https://WX\n...@m.75B2169...` | `m.75b2169ݨ⳧񇐁!...` | `WX` |
| java-net-url vs python-urllib3 | `https://0Y86W62dJxk9...\nB@...@Vi0Jw6?#` | `vi0jw6` | `0Y86W62dJxk9⭓` |
| java-net-url vs python-urllib3 | `ftp://yy28uz068\n...@7L6C3enJ14Xb#` | `7l6c3enj14xb` | `yy28uz068ጧ𦔶` |
| java-net-url vs python-urllib3 | `https://xn--9nt\n7\t(-n49p/460Zsvjl27MAOYcp375N04.24.6.17:038WVX84PVG6]FiwsX17?` | `xn--9nt7(-n49p` | `xn--9nt` |
| java-galimatias vs rust-url | `ws://hNjVwC
24yrd7GQ38ij80788k8X@N9339a/.22c:0D*...` | `hnjvwc` | `n9339a` |
| java-galimatias vs rust-url | `wss://8 
4kd@0/../1.85.7.02:76;...` | `0.0.0.0` | `8` |
| java-galimatias vs rust-url | `ftp://c7ZE
`12@9FP.8.108a6Es0mNc...#` | `c7ze` | `9fp.8.108a6es0mnc958171btv3y_8o2xeokzgw6pn` |
| java-url vs rust-url | `ftp://07tCn99593539lnB丷
Z...@0.JM18/...` | `07tcn99593539lnb丷` | `0.jm18` |
| java-url vs rust-url | `ftp://yy28uz068ጏ
8py0a341C811Sf:564VcO@7L6C3enJ14Xb#` | `yy28uz068ጏ` | `7l6c3enj14xb` |
| java-url vs rust-url | `https://SY37q09Gi
ૢ3@7R.--qbX6r5.V-/...` | `sy37q09gi` | `7r.--qbx6r5.v-` |
| java-url vs rust-url | `https://p
捻⌚...@.-/...` | `p` | `.-` |
| java-galimatias vs rust-url | `ws://k778℧
1m8wF@[DD:5:1:A0:dc:5:AD:8]:191/...` | `xn--k778-je8a` | `[dd:5:1:a0:dc:5:ad:8]` |
| java-url vs rust-url | `http://JW
@57.91.41.73:4113?#` | `57.91.41.73` | `JW` |
| java-url vs rust-url | `ftp://9P16pUcY77iS0u
1k9Bh50@IFe.613...?` | `9P16pUcY77iS0u` | `ife.xn--613-5xd3727a` |
| java-galimatias vs rust-url | `wss://gT4VC9SbHs6241bD44W...
61g0@[D:72:a:A0:91:a5:6:D1]:8?` | `xn--gt4vc9sbhs6241bd44w-yo3k` | `[d:72:a:a0:91:a5:6:d1]` |
| java-galimatias vs rust-url | `wss://ftp://1760O8l:6k5VNP@9	{...
&...@3xbQg04784UM?#` | `xn--9{-3q8e` | `3xbqg04784um` |
| java-galimatias vs rust-url | `ftp://48XrlR:Ei@...
375u6g4YG3k342:363V@8Ppd(026t8D&4?	#8` | `xn---tp1av471x` | `8ppd(026t8d&4` |
| javascript-whatwg vs javascript-legacy | `wss://NjVwC
24yrd@N9339a:...?#` | `n9339a` | `N9339a` |
| javascript-whatwg vs javascript-legacy | `snews://c-
和L2@qS.nz.6-g074Av7O2n8:7228@DLUcVSJU4G4UoF15;b?#` | `dlucvsju4g4uof15` | `DLUcVSJU4G4UoF15;b` |
| javascript-whatwg vs javascript-legacy | `wss://J76Ề1
...@032XTwd3t254489`0p4RL1?#` | `032xtwd3t254489` | `032xtwd3t254489`0p4rl1` |
| javascript-whatwg vs javascript-legacy | `ws://892A...^...@1.72.3.1:4U3t4952@T5wd6A'0Za4?` | `t5wd6a'0za4` | `t5wd6a` |
| javascript-whatwg vs javascript-legacy | `dis://S7
/..L73A@r--8:0d7l4?#` | `r--8` | `s7` |
| javascript-whatwg vs javascript-legacy | `bolo://961wUi6TE3.72.9:6o4t10s6001T84932732i0L
άᾩ...@8.0K07YY80?#` | `8.0k07yy80` | `8.0K07YY80` |
| javascript-whatwg vs javascript-legacy | `wss://J76Ề1
0e3@032XTwd3t254489`0p4RL1?#` | `032xtwd3t254489` | `032xtwd3t254489`0p4rl1` |
| javascript-whatwg vs javascript-legacy | `view-source://0Y70uⲥ9Z'3
40@mBnD8tZ.D5jVWc-.8e-1.4to494kk1he3'92r33?#` | `mbnd8tz.d5jvwc-.8e-1.4to494kk1he3'92r33` | `mbnd8tz.d5jvwc-.8e-1.4to494kk1he3` |
| javascript-whatwg vs perl-uri | `ws://hrl49V3Q50/...8f77gTbO:
5T@H4t��𙍡@xvk.K-.M.5..96U37-N:3250...` | `hrl49v3q50` | `hrl49V3Q50` |
| zig-std-uri vs rust-url | `data://Bp90geG3Tba_	71MI/./3c@[2B:8:b:E:34:7:a0:8]:3qT3Fjm3dyn95864:dn9?#` | `Bp90geG3Tba_	71MI` | `Bp90geG3Tba_71MI` |
| zig-std-uri vs rust-url | `ms-visio://59wx9c712Bi16151	18428.9.06.1430HL9y4g7SVFMt1bV8p44Ga?#` | `59wx9c712Bi1615118428.9.06.1430HL9y4g7SVFMt1bV8p44Ga` | `59wx9c712Bi16151	18428.9.06.1430HL9y4g7SVFMt1bV8p44Ga` |
