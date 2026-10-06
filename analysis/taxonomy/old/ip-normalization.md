# IP Address Normalization

**Description:** Hex, octal, dotless, or otherwise non-standard IP representations are expanded to standard dotted-decimal by some parsers but not others

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| javascript-whatwg vs rust-url | `0.10.85.43 ymsgr://599I3d57S7DXd1:4@0.10.85.43:0486\󺫓��W)⩂􀿨#􁅂?*nf22k41999121*121;?#` | `` | `0.10.85.43` |
| javascript-whatwg vs rust-url | `data://13.49.73.2 data://6uaU2o4ea56U147v534:6V224@13.49.73.2:737\?#7b09` | `` | `13.49.73.2` |
| javascript-whatwg vs rust-url | `dns://0mYmZcW5G830d0v248p8@60.9.9.5:913\~9N6OYy6C6U69f17qh?#` | `` | `60.9.9.5` |
| javascript-whatwg vs rust-url | `data://7Њ󁙝&Y'<[ÊU^8@6.85.8.67:83\9i7875a6La120e90Q?#` | `` | `6.85.8.67` |
| javascript-whatwg vs rust-url | `ms-media-stream-id://K05e󹡴	􁏬
):5𩹴𡕊􁻝
FᅁRYO@21.86.35.51:7\j_9JhK8327f8FvbVY9?` | `` | `21.86.35.51` |
| javascript-whatwg vs rust-url | `data://6uaU2o4ea56U147v534:6V224@13.49.73.2:737\?#7b09` | `` | `13.49.73.2` |
| javascript-whatwg vs rust-url | `jabber://0156J7,-6bsU@31.07.67.02:006484\1=4l;7358z0X23QE?#` | `` | `31.07.67.02` |
| javascript-whatwg vs rust-url | `data://465𤴂<^㷇𢁖l$󹰫␞3@4:340\dA469?` | `4` | `` |
| whatwg vs legacy | `https://JxUSvT...@99.93.4.62:22...@00?...` | `0.0.0.0` | `00` |
| whatwg vs deno | `ymsgr://...@0.10.85.43:0486...` | `` | `0.10.85.43` |
| whatwg vs deno | `data://6uaU2o4ea56U147v534...@13.49.73.2:737...` | `` | `13.49.73.2` |
| whatwg vs deno | `callto://P+...@70.87.66.78:522...` | `` | `70.87.66.78` |
| whatwg vs deno | `data://...@52.34.61.48:...` | `` | `52.34.61.48` |
| whatwg vs smithy | `ws://05?...@[7C:f:1e:8E:a0:ba:FF:d]...` | `0.0.0.5` | `` |
| whatwg vs smithy | `ftp://N3i7:J7j688.48.50.5:7114604327169...@8?...` | `0.0.0.8` | `` |
| whatwg vs smithy | `http://8/..G6WW?...` | `0.0.0.8` | `` |

| whatwg vs javascript-smithy | `ftp://N3i7:J7j688.48.50.5:7114604327169󠃧@8?	♸󡢮%67󠣉桩󨄀⪿��	
	ُ󡢮%67󠣉桩󨄀⪿��	
	ɴ#s|H` | `0.0.0.8` | `` |
| whatwg vs javascript-smithy | `http://8/..G6WW?1%󐠫90hAH@22:108OI32o46kTI2Z165335_?#` | `0.0.0.8` | `` |
| whatwg vs javascript-uri-js | `https://JxUS๸vT⭇@99.93.4.62:22F56^<o󠃙xg*6}::'25Ny`K934𦶵꣧8jt9@00?"U块` | `0.0.0.0` | `99.93.4.62` |
| javascript-whatwg vs javascript-legacy | `https://JxUSvT@99.93.4.62:22F56@00?` | `0.0.0.0` | `00` |
| javascript-whatwg vs javascript-legacy | `ws://3SEC8ar3W56860:Ol61@99.01.1.20:88 E9?` | `99.01.1.20:88` | `` |
| javascript-whatwg vs javascript-smithy | `ws://05?@[7C:f:1e:8E:a0:ba:FF:d]h605?` | `0.0.0.5` | `` |
| javascript-whatwg vs javascript-smithy | `ftp://N3i7:J7j688.48.50.5:7114604327169@8?` | `0.0.0.8` | `` |
| javascript-whatwg vs javascript-smithy | `http://8/..G6WW?@22:108?` | `0.0.0.8` | `` |
| javascript-whatwg vs javascript-uri-js | `https://JxUSvT@99.93.4.62:22F56@00?` | `0.0.0.0` | `99.93.4.62` |
| whatwg vs legacy | `https://JxUSvT@99.93.4.62:22F56^<o...@00?"U` | `0.0.0.0` | `00` |
| whatwg vs parse-uri | `https://JxUSvT@99.93.4.62:22F56^<o...@00?"U` | `0.0.0.0` | `99.93.4.62` |
| whatwg vs smithy | `ws://05?838f9kl043c43Lh@[7C:f:1e:8E:a0:ba:FF:d]h605...` | `0.0.0.5` | `` |
| whatwg vs smithy | `http://8/..G6WW?1%...` | `0.0.0.8` | `` |
| whatwg vs smithy | `ftp://N3i7:J7j688.48.50.5:7114604327169@8?` | `0.0.0.8` | `` |
| whatwg vs fast-uri | `https://JxUSvT@99.93.4.62:22F56^...@00?"U` | `99.93.4.62` | `0.0.0.0` |
| whatwg vs parseuri | `https://JxUSvT@99.93.4.62:22F56^...@00?"U` | `` | `0.0.0.0` |
| whatwg vs fast-uri | `data://z308V2H89C6IVs670N2@52.34.61.48:...?#` | `` | `52.34.61.48` |
| whatwg vs jsuri | `https://JxUSvT@99.93.4.62:22F56^...@00?"U` | `00` | `0.0.0.0` |
| whatwg vs domurl | `bolo://0𫚳1e65.4.17.3:77058479/,{9PwCe@?#8` | `` | `xn--01e65-qp48f.4.17.3` |
| whatwg vs ada-uri-mime | `https://JxUSvT@99.93.4.62:22F56^...@00?"U` | `` | `0.0.0.0` |
| whatwg vs trurl | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| whatwg vs ada-uri-mime | `ws://R6tBj668463bSfmPR:@68.38.1.241067	��	9p?#` | `` | `68.38.1.xn--2410679p-zt38j` |
| whatwg vs wget | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| whatwg vs haskell-network-uri | `https://JxUSvT@99.93.4.62:22F56^...@00?"U` | `0.0.0.0` | `` |
| whatwg vs crystal-uri | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| whatwg vs crystal-uri | `bolo://0𫚳1e65.4.17.3:77058479/,{9PwCe@?#8` | `` | `0𫚳1e65.4.17.3` |
| whatwg vs boost-url | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| whatwg vs poco-uri | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `08.61.1.95` | `` |
| whatwg vs swift-url | `bolo://0𫚳1e65.4.17.3:77058479/,{9PwCe@?#8` | `0𫚳1e65.4.17.3` | `` |
| whatwg vs rust-url | `ymsgr://599I3d57S7DXd1:4@0.10.85.43:0486\...` | `` | `0.10.85.43` |
| whatwg vs rust-url | `jabber://0156J7,-6bsU@31.07.67.02:006484\...?#` | `` | `31.07.67.02` |
| whatwg vs python-urllib3 | `ftp://Kds2CYszhi8H67d@08.61.1.95:76?#` | `` | `08.61.1.95` |
| javascript-legacy vs javascript-jsuri | `https://JxUSvT@99.93.4.62:22F56...@00?"U` | `99.93.4.62` | `00` |
| python-urllib-parse vs python-furl | `wss://x2xx0Z5yjQle3@0.5:4905~...?#!` | `0.0.0.5` | `` |
