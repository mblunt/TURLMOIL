# Unicode Normalization (NFKC/NFC)

**Description:** One parser applies Unicode normalization (NFKC/NFC) to the host, converting compatibility characters like superscript digits (⁴→4), micro sign (µ→μ), or modifier letters (ᵛ→v) to their canonical equivalents, while the other preserves the original code points.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| go-net vs python-yarl | `file://R43P8l8oV3l4629⁴#𔚷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| go-net vs python-yarl | `http://Tt5㎗ᵛi#𙯕𠁄⸸8㐵@[A5:30:4:9:1:90:A9:3]:5[27=78UZg5T2VLUP09a?#` | `Tt5㎗ᵛi` | `tt5㎗vi` |
| go-net vs python-yarl | `file://SÀµÀ³86nl880𘷡#🿬@E823HNh?#` | `SÀµÀ³86nl880𘷡` | `sàμà΃ゆ86nl880𘷡` |
| js-whatwg vs go-net | `file://R43P8l8oV3l4629⁴#𔚷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| go-net vs python-yarl | `http://Tt5㎗ᵛi#𙯕𠁄⸸8㐵@[A5:30:4:9:1:90:A9:3]:5[27=78UZg5T2VLUP09a?#` | `Tt5㎗ᵛi` | `tt5㎗vi` |
| go-net vs python-yarl | `file://SÀµÀ³86nl880𘷡#(🿤𗪸�<{À¸5KÁÀ³3@E823HNhÁQqp-29-55j.?#` | `SÀµÀ³86nl880𘷡` | `sàμà΃ゆ86nl880𘷡` |
| js-whatwg vs csharp-systemuri | `file://R43P8l8oV3l4629⁴#𔚷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| js-whatwg vs python-urllib3 | `file://R43P8l8oV3l4629⁴#...` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| js-whatwg vs dart-core | `file://R43P8l8oV3l4629⁴#𔚷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `r43p8l8ov3l4629%E2%81%B4` | `r43p8l8ov3l46294` |
| csharp-systemuri vs rust-url | `file://R43P8l8oV3l4629⁴#...` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| js-whatwg vs csharp-systemuri | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| js-whatwg vs csharp-systemuri | `(URL with host r43p8l8ov3l4629⁴)` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| go-net vs rust-url | `...@R43P8l8oV3l4629⁴...` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| go-net vs rust-url | `...@Tt5㕗ᵛi...` | `Tt5㕗ᵛi` | `xn--tt5vi-8t0e` |
| js-whatwg vs go-net | `...(URL with superscript-4 in host)...` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| js-whatwg vs go-net | `...(URL with modifier letter v in host)...` | `Tt5㖗ᵛi` | `xn--tt5vi-8t0e` |
| js-whatwg vs go-net | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| js-whatwg vs go-net | `http://Tt5垗ᵛi#...@[A5:30:4:9:1:90:A9:3]:5[27=...?#` | `Tt5垗ᵛi` | `xn--tt5vi-8t0e` |
| go-net vs rust-url | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| go-net vs rust-url | `file://SÀµÀ³86nl880𝲱#...?#` | `SÀµÀ³86nl880𝲱` | `xn--s386nl880-q1aa798f5r08t` |
| csharp-systemuri vs rust-url | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| javascript-whatwg vs csharp-systemuri | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `r43p8l8ov3l46294` | `r43p8l8ov3l4629⁴` |
| go-net vs rust-url | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| go-net vs rust-url | `http://Tt5㖗ᵛi#𩿕...` | `Tt5㖗ᵛi` | `xn--tt5vi-8t0e` |
| perl-uri vs rust-url | `file://R43P8l8oV3l4629⁴#...@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| javascript-whatwg vs javascript-legacy | `wss://8dB...` | `xn--8db` | `8Dᴮ` |
| csharp-systemuri vs rust-url | `http://Tt5㖗ᵛi#...` | `tt5㖗ᵛi` | `xn--tt5vi-8t0e` |
| crystal-uri vs rust-url | `file://R43P8l8oV3l4629⁴#𐓷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| csharp-systemuri vs rust-url | `file://R43P8l8oV3l4629⁴#𐓷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| javascript-whatwg vs crystal-uri | `file://R43P8l8oV3l4629⁴#𐓷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `R43P8l8oV3l4629⁴` | `r43p8l8ov3l46294` |
| javascript-whatwg vs crystal-uri | `http://Tt5㕗ᵛi#𙣽𘁄⸸5@[A5:30:4:9:1:90:A9:3]:5[27=78UZg5T2VLUP09a?#` | `Tt5㕗ᵛi` | `xn--tt5vi-8t0e` |
| javascript-whatwg vs rust-url | `file://R43P8l8oV3l4629⁴#𐓷;.fs9b9:00rhS@8X-6l9u0..F83q7pC3sLNI?#` | `r43p8l8ov3l46294` | `r43p8l8ov3l46294` |
