# Query parsing error

**Description:** One parser fails to parse query correctly or returns empty/corrupted content while other returns normalized query

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `À%09p𥢋˃Z` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `%22U䗪` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `C%7C�뫉=;%2��������䑑JC3gO32V12o3k1334w!?` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `À£%7BÁ¥` |
| whatwg vs legacy | `https://JxUSࣸvT⭇@99.93.4.62:22F56^<o󃥙xg*6}::'25Ny`K934𦭥ꫧ8jt9@00?"U䗪` | `?%22U%E4%97%AA` | `?` |
| whatwg vs ada | `:%252F/sy3J%2534𞸋𝞂阱)𑛾3%2531cM@%254D6%252D𪂯` | `?` | `%23` |
