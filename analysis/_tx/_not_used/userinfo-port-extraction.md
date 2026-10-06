# Userinfo or port extraction differences

**Description:** One parser includes userinfo or port in authority, while other extracts only host, or one fails to parse.

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs userfriendlyurl | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `lm5E4nQ8-6o.6Q0Bij6:4` |
| whatwg vs userfriendlyurl | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `/.` |
| whatwg vs userfriendlyurl | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `-S9gK:798` |
| whatwg vs userfriendlyurl | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `2%EF%BC%8E87%EF%BC%8E39%EF%BC%8E99:32206` |
| whatwg vs userfriendlyurl | `mms://7l90:\M5.i91-E3-4328c.-3g:􍇰
#÷愣􆬤` | `7l90` | `3%EA%B8%A0%F0%A1%8D%8E:6200` |

| radix vs jsprim | `go://5j7TF3XR퐊큛ȴȤ@2203횙o20O/../A2CqL?` | `2203%F3%99%B9%A8o20O` | `5j7TF3XR퐊큛ȴȤ@2203횙o20O` |
