# Fullwidth / Unicode Separator Normalization

**Description:** One parser normalizes fullwidth periods (．U+FF0E) or other Unicode dot-like separators to ASCII equivalents while the other treats them as literal characters in the host.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| legacy vs url-parse | `ventriloI://3Y63NWUY67C3:3v@7j@7Er0。59z85j18m:50?#` | `7er0.59z85j18m:50` | `7er0。59z85j18m:50` |
| legacy vs url-parse | `wss://60cD1k7Gx,⊮@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97.60.6.70034li959s+8c0m+wd84xqf` | `97．60.6.70034li959s+8c0m+wd84xqf` |
| javascript-whatwg vs javascript-url-parse | `data://3VC-L3f。 4Ih2mEa45&h3/...` | `3vc-l3f.4ih2mea45&h3` | `3vc-l3f。4ih2mea45&h3` |
| javascript-whatwg vs javascript-urijs | `https://439u6...@3VC-L3f。 4Ih2mEa45&h3/...` | `3VC-L3f。4Ih2mEa45&h3` | `3vc-l3f.4ih2mea45&h3` |
| javascript-legacy vs javascript-uri-js | `ftp://fN5T...@w943P｡4｡4-aT8V-5T-.:5648/...` | `w943p.4.4-at8v-5t-.:5648` | `w943p%EF%BD%A14%EF%BD%A14-at8v-5t-.` |
| javascript-legacy vs python-urllib3 | `data://97．60.6.70034li959s+8c0m+wd84xqf/...` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| javascript-legacy vs python-urllib3 | `data://｡.83g8𘻄78$dks246trzc32o14i/...` | `｡.83g8𘻄78$dks246trzc32o14i` | `..xn--83g878$dks246trzc32o14i-u5035a` |

| elixir-uri vs python-yarl | `wss://60cD1k7Gx,⊮@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97．60.6.70034LI959s+8c0M+wd84XqF` | `97.60.6.70034LI959s+8c0M+wd84XqF` |
| js-legacy vs python-urllib3 | `wss://60cD1k7Gx,⊮@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| js-whatwg vs csharp-systemuri | `data://KGzlD554sfIB719𫦗
𓰥N2ooZ7t6N@297-．5u4-:877?#` | `297-．5u4-` | `297-%EF%BC%8E5u4-` |
| js-whatwg vs csharp-systemuri | `ws://qr0S81N0W9b3frlJo3
6108cPJ4QP869@f49HI-PC20-6uAIj｡jf:173?#` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf` |
| js-legacy vs python-urllib3 | `https://439u6𛫞⮧C⏂5@3VC-L3f。。。。。。。。。。。4Ih2mEa45&h3/nnP9I1iaf"?#` | `3vc-l3f。4ih2mea45&h3` | `3vc-l3f.4ih2mea45&h3` |
| js-legacy vs python-urllib3 | `ftp://4COWp$𕓜6L@f．．.h0-aujmp7G74N89Z8gs4qIgo7n1Oi4m2117x?#` | `f．.h0-aujmp7g74n89z8gs4qigo7n1oi4m2117x` | `f..h0-aujmp7g74n89z8gs4qigo7n1oi4m2117x` |
| js-legacy vs python-urllib3 | `data://dX11kuwT3n59F32𘒵394NYE@55。7。〦26.4950u53p5oj0,07S8A76Jsx?#` | `55。7〦26.4950u53p5oj0,07s8a76jsx` | `55.7.26.4950u53p5oj0,07s8a76jsx` |
| js-whatwg vs dart-core | `https://439u6𛫞⮧C⏂5@3VC-L3f。4Ih2mEa45&h3/nnP9I1iaf"?#` | `3vc-l3f%E3%80%824ih2mea45&h3` | `3vc-l3f.4ih2mea45&h3` |
| go-net vs rust-url | `ws://695-rlH345@7。8。06。498o"7278Gt20e~ieQtf0y?#` | `7。8。06。498o"7278Gt20e~ieQtf0y` | `7.8.06.498o"7278gt20e~ieqtf0y` |
| rust-url vs ruby-addressable | `ftp://4COWp$..6L@f．.h0-aujmp7G74N89Z8gs4qIgo7n1Oi4m2117x?#` | `f..h0-aujmp7g74n89z8gs4qigo7n1oi4m2117x` | `f．.h0-aujmp7G74N89Z8gs4qIgo7n1Oi4m2117x` |
| rust-url vs ruby-addressable | `data://dX11kuwT3n59F32𘂵394NYE@55。7。26.4950u53p5oj0,07S8A76Jsx?#` | `55。7。26.4950u53p5oj0,07S8A76Jsx` | `55%E3%80%827%E3%80%8226.4950u53p5oj0,07S8A76Jsx` |
| rust-url vs ruby-addressable | `data://KGzlD554sfIB719𛧗
𣲥N2ooZ7t6N@297-．5u4-:877?#` | `297-%EF%BC%8E5u4-` | `297-．5u4-` |
| js-legacy vs python-hyperlink | `wss://60cD1k7Gx,⪮@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97．60.6.70034LI959s+8c0M+wd84XqF` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| csharp-systemuri vs rust-url | `ws://qr0S81N0W9b3frlJo3...@f49HI-PC20-6uAIj｡jf:173?#` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf` |
| js-whatwg vs csharp-systemuri | `data://KGzlD554sfIB719...
@297-．5u4-:877` | `297-．5u4-` | `297-%EF%BC%8E5u4-` |
| js-whatwg vs csharp-systemuri | `ws://qr0S81N0W9b3frlJo3
...@f49HI-PC20-6uAIj｡jf:173` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf` |
| csharp-systemuri vs rust-url | `ws://qr0S81N0W9b3frlJo3
...@f49HI-PC20-6uAIj｡jf:173` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf` |
| js-whatwg vs go-net | `ws://695-rlH345@7。 8。8。0。6。4。9。8o"7278Gt20e~ieQtf0y` | `7。8。0。6。4。9。8o"7278gt20e~ieqtf0y` | `7.8.06.498o"7278gt20e~ieqtf0y` |
| go-net vs rust-url | `ws://695-rlH345@7。8。0。6。4。9。8o"7278Gt20e~ieQtf0y` | `7。8。0。6。4。9。8o"7278Gt20e~ieQtf0y` | `7.8.06.498o"7278gt20e~ieqtf0y` |
| js-whatwg vs csharp-systemuri | `(URL with fullwidth period ． in host 297-．5u4-)` | `297-%EF%BC%8E5u4-` | `297-．5u4-` |
| js-whatwg vs csharp-systemuri | `(URL with halfwidth ideographic full stop ｡ in host)` | `f49hi-pc20-6uaij.jf` | `f49hi-pc20-6uaij｡jf` |
| python-urllib3 vs python-yarl | `wss://60cD1k7Gx,⊮@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97.60.6.70034LI959s+8c0M+wd84XqF` |
| python-urllib3 vs python-yarl | `https://...@3VC-L3f。 4Ih2mEa45&h3/...` | `3vc-l3f。4ih2mea45&h3` | `3VC-L3f.4Ih2mEa45&h3` |
| python-urllib3 vs python-yarl | `http://...@6。8.34.26:161?#` | `6.8.34.26` | `6。8.34.26` |
| python-urllib3 vs python-yarl | `http://...@5。2.47.4836Xu6_4Dst75W12864p?#` | `5。2.47.4836xu6_4dst75w12864p` | `5.2.47.4836Xu6_4Dst75W12864p` |
| js-whatwg vs js-url-parse | `https://439u6@3VC-L3f。 4Ih2mEa45&h3/...` | `3vc-l3f。4ih2mea45&h3` | `3vc-l3f.4ih2mea45&h3` |
| js-whatwg vs js-url-parse | `wss://...@。g〢67WQb4q62--5X-4k:670?` | `.g.67wqb4q62--5x-4k` | `。g〢67wqb4q62--5x-4k` |
| js-whatwg vs js-url-parse | `wss://...@G1h．u．M8Gc6320Xl7o752606Tl7C9A2H?#` | `g1h.u.m8gc6320xl7o752606tl7c9a2h` | `g1h．u．m8gc6320xl7o752606tl7c9a2h` |
| java-galimatias vs python-urllib3 | `wss://...@97．60.6.70034LI959s+8c0M+wd84XqF?#` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| go-net vs rust-url | `...@7。8〢06。498o"7278Gt20e~ieQtf0y...` | `7。8〢06。498o"7278Gt20e~ieQtf0y` | `7.8.06.498o"7278gt20e~ieqtf0y` |
| elixir-uri vs python-urllib3 | `...@97．60.6.70034LI959s+8c0M+wd84XqF...` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97．60.6.70034LI959s+8c0M+wd84XqF` |
| java-galimatias vs python-urllib3 | `...@3vc-l3f。 4ih2mea45&h3...` | `3vc-l3f。4ih2mea45&h3` | `3vc-l3f.4ih2mea45&h3` |
| java-galimatias vs python-urllib3 | `...@6。8.34.26...` | `6。8.34.26` | `6.8.34.26` |
| java-galimatias vs python-urllib3 | `...@g1h．u．m8gc6320xl7o752606tl7c9a2h...` | `g1h.u.m8gc6320xl7o752606tl7c9a2h` | `g1h．u．m8gc6320xl7o752606tl7c9a2h` |
| go-net vs rust-url | `...(URL with fullwidth period ．)...` | `-mgx4x6.70j-4w..` | `-mGx4X6．70J-4w．．` |
| perl-uri vs elixir-uri | `wss://M056j2:Qz0R3082s@5．90．55.47:177257836qH1OKH?#2W&TgJ` | `5．90．55.47` | `xn--59055-pcac87ad91ce.47:177257836qH1OKH` |
| java-galimatias vs elixir-uri | `...(URL with fullwidth period ． in host)...` | `97．60.6.70034li959s+8c0m+wd84xqf` | `97.60.6.70034li959s+8c0m+wd84xqf` |
| csharp-systemuri vs rust-url | `data://KGzlD554sfIB719...@297-．5u4-:877?#` | `297-%EF%BC%8E5u4-` | `297-．5u4-` |
| javascript-whatwg vs csharp-systemuri | `ws://qr0S81N0W9b3frlJo3...@f49HI-PC20-6uAIj｡jf:173?#` | `f49hi-pc20-6uaij｡jf` | `f49hi-pc20-6uaij.jf` |
| javascript-whatwg vs javascript-legacy | `data://dX11kuwT3n59F32...@55。 7。26.4950u53p5oj0,07S8A76Jsx?#` | `55%E3%80%827%E3%80%8226.4950u53p5oj0,07s8a76jsx` | `55.7.26.4950u53p5oj0,07s8a76jsx` |
| javascript-whatwg vs javascript-legacy | `ftp://O...@9．57．94.42030192R7$4}Q814WbFNj?#` | `9.57.94.42030192r7$4}q814wbfnj` | `9.57.94.42030192r7$4` |
| javascript-whatwg vs javascript-legacy | `about://B2N2H5d80693	7...@lV38hf5-Ht-x0-7p．wN0NdaOi0J63$?#` | `lV38hf5-Ht-x0-7p%EF%BC%8EwN0NdaOi0J63$` | `lv38hf5-ht-x0-7p.wn0ndaoi0j63$` |
| go-net vs rust-url | `ws://695-rlH345@7。8〆06。498o"7278Gt20e~ieQtf0y?#` | `7。8〆06。498o"7278gt20e~ieqtf0y` | `7.8.06.498o"7278gt20e~ieqtf0y` |
