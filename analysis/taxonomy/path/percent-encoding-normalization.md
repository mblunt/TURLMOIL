# Percent Encoding Normalization

**Description:** Parsers differ on whether percent-encoded sequences in paths are normalized (e.g. double-encoded %25XX decoded to %XX, or uppercase/lowercase), vs left as-is.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|
| python-urllib3 vs python-yarl | `⚐ms%252D%2565n%2572ollment%2563i%2564git://1t8r%2570%2558%256A4h7@f%252F%2540%254F31Uk1.v%2566?#` | `⚐ms%252D%2565n%2572ollment%2563i%2564git://1t8r%2570%2558%256A4h7@f%252F%2540%254F31Uk1.v%2566` | `⚐ms%2D%65n%72ollment%63i%64git://1t8r%70%58%6A4h7@f%2F%40%4F31Uk1.v%66` |
| python-urllib3 vs python-yarl | `i%2568xxp%2573V://test?#` | `i%2568xxp%2573V://test` | `i%68xxp%73V://test` |
| python-urllib3 vs python-yarl | `%25%25377s%2573%253A%252F%25%2532F7F)>p%25376%25309@test.example.com?#` | `%25%25377s%2573%253A%252F%25%2532F7F)>p%25376%25309@test.example.com` | `%%377s%73%3A%2F%%32F7F)>p%376%309@test.example.com` |
| python-yarl vs python-requests | `⚐ms%252D%2565n%2572ollment%2563i%2564git://1t8r%2570%2558%256A4h7@fW573B?#` | `⚐ms%25252D%252565n%252572ollment%252563i%252564git://1t8r%252570%252558%25256A4h7@fW573B` | `⚐ms%2D%65n%72ollment%63i%64git://1t8r%70%58%6A4h7@fW573B` |
| python-yarl vs python-requests | `ms-help%3A//GVKw1kN850242I167xyz@f9.0c83.q836i%3A31%0B?#` | `ms-help%3A%2F%2FGVKw1kN850242I167xyz@f9.0c83.q836i%253A31%250B` | `ms-help://GVKw1kN850242I167xyz@f9.0c83.q836i:31` |
| python-yarl vs python-requests | `%6Ds-h%65lp:%2F/G%56K%771kN8%350242I167@f9.%30c83.q836i%3A31?#` | `ms-help:%2F/GVKw1kN850242I167@f9.0c83.q836i%3A31` | `ms-help://GVKw1kN850242I167@f9.0c83.q836i:31` |
| python-urllib3 vs python-furl | `file:/%2FV%546%58%72C_382IV%33L?#` | `/%2FV%546%58%72C_382IV%33L` | `/%252FV%25546%2558%2572C_382IV%2533L` |
| python-urllib3 vs python-furl | `[fax%3A/%2F0s2%39%3306xyz@%3A835E)C4%322]3%52je%32872?#` | `%5Bfax%253A/%252F0s2%2539%253306xyz@%253A835E)C4%25322%5D3%2552je%2532872` | `[fax%3A/%2F0s2%39%3306xyz@%3A835E)C4%322]3%52je%32872` |
| python-urllib3 vs python-rfc3986 | `ms-whiteboard-cmdVipnk|mapsdav://p47:xyz@xn--6o[5-mm6bs1013q:9]:18Hl2QNzA09n356e8|83?n` | `ms-whiteboard-cmdVipnk|mapsdav://p47:xyz@xn--6o[5-mm6bs1013q:9]:18Hl2QNzA09n356e8|83` | `ms-whiteboard-cmdVipnk%7Cmapsdav://p47:xyz@xn--6o[5-mm6bs1013q:9]:18Hl2QNzA09n356e8%7C83` |
