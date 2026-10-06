# Port stripping from authority

**Description:** One parser strips port from authority field; the other includes it, or one normalizes port representation (leading zeros, removal of default ports).

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| radix (3) vs whatwg (4) | `sLopenpgp4fpraFQ7://2W21SCB	E@5gHx.3n2u6P4401.-7l:048/;14[gՆ9𝲘87⢕M󰒔?1?󬵋4?&1?󬵋4?` | `5gHx.3n2u6P4401.-7l:048` | `5gHx.3n2u6P4401.-7l:48` |
| radix (3) vs whatwg (4) | `ms-settings-cellular://342H0@.8agD-.64.z64.091.E:1478#7򅎩2򗪞󊦱09cRGS67z3kjyg#` | `.8agD-.64.z64.091.E:1478` | `.8agD-.64.z64.091.E:1478` |
