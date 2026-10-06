# Host case normalization

**Description:** One parser lowercases the host; the other preserves original case or normalizes differently.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| radix (3) vs whatwg (4) | `wss://yNk4103A?󶳠 m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `ynk4103a` |
| radix (3) vs whatwg (4) | `ws://hrl49V3Q50/...8f77gTbO:` | `hrl49V3Q50` | `hrl49v3q50` |
| radix vs jsprim | `wss://yNk4103A?` | `ynk4103a` | `yNk4103A` |
| radix vs jsprim | `ws://hrl49V3Q50/` | `hrl49v3q50` | `hrl49V3Q50` |
| legacy vs jsprim | `wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `ynk4103a` | `yNk4103A` |
| legacy vs node | `wss://yNk4103A?󶳠m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `ynk4103a` |
| legacy vs whatwg | `http://Sh7/𦦎qn7g0b4U44HDW69L31@7.06.60.37:95^50+0j496j]0a415dv1?#0` | `sh7` | `Sh7` |
| legacy vs whatwg | `file://a9HC5V03i92S3b9z330/..G⪬#𨢹$rI3a714Q𗢐;˂72#YS4P ?#` | `a9hc5v03i92s3b9z330` | `a9HC5V03i92S3b9z330` |
| legacy vs whatwg | `ws://Z9I6Z786V06#𧬀􍖘@􌊯񂩿𪆝2􏹽@21.52.75.69:1{𘿾󳷻?#` | `z9i6z786v06` | `Z9I6Z786V06` |
| legacy vs whatwg | `http://70dx5𩓔៙J⁁ᴵv@2W00968j1V3_kw005JH49j82M8?` | `2w00968j1v3_kw005jh49j82m8` | `2W00968j1V3_kw005JH49j82M8` |
| legacy vs whatwg | `wss://cmP3J9s7@f..7S1j-2..dO6-B-In:8#QUT~(287s4707D50]12?#` | `f..7s1j-2..do6-b-in:8` | `f..7S1j-2..dO6-B-In:8` |
| go-net vs rust-url | `wss://yNk4103A?🗻6m\𥨇⨷ᵨ@0.05.46.81:59215212280{L77d39G46i91QBSN424?#` | `yNk4103A` | `ynk4103a` |
| go-net vs rust-url | `ws://hrl49V3Q50/...8f77gTbO:
5T@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250⪼
C58?#` | `hrl49V3Q50` | `hrl49v3q50` |
| go-net vs rust-url | `ws://6627HpNE72N>4@6a4X.w04,	B}391752316e5ZVx99M?#` | `6a4X.w04,	B}391752316e5ZVx99M` | `6a4x.w04,b}391752316e5zvx99m` |
