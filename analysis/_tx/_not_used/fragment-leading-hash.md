# Fragment leading hash inclusion

**Description:** One parser includes the leading # in the fragment, the other strips it

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs go | `unknown` | `#וּ#` | `#!` |
| whatwg vs go | `unknown` | `#!%35AN>|_|#` | `#!%35AN>|_|#!` |
| ada vs python | `unknown` | `#` | `#!%35AN%3E%7C_` |
| ada vs python | `unknown` | `#1` | `#` |
| ada vs python | `unknown` | `#v4%32P%40[aE:%44:9%31:E:%66:e%3AA:3]:9ﭙB㡐%7B﷨⧒%32?%23` | `#` |
