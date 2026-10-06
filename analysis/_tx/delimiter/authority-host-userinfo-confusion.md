# Authority Host Userinfo Confusion

**Description:** Userinfo parsed as part of authority differently—@ ambiguity or userinfo/host boundary

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| uripara vs node | `https://4=M@[8f:D8:2f:4A:C2:67:26:50]:326178O?4?#` | `4=M@[8f:D8:2f:4A:C2:67:26:50]:326178O` | `462Y96W9@88-97.8--6n3NY15n7x:90)2n12j0Amk38_'D08L4` |
| php-http vs ada | `snews://H9ExᕙV穹
%4Ė𩵧hY5LcF@[3:3:b:3B:8E:d:69:f]:84\b1G9258{53$De1Mp28?#` | `[3:3:b:3b:8e:d:69:f]:84` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99:32206` |
| whatwg vs legacy | `unknown` | `%0C` | `` |
| whatwg vs legacy | `unknown` | `%04` | `` |
| whatwg vs legacy | `unknown` | `` | `%10` |
