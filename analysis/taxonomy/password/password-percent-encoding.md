# Password percent-encoding

**Description:** One parser preserves or normalizes password while other applies variable percent-encoding

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2񀈠À³#?󳃶À¬À¼` | `p` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs legacy | `jms://QP1km1TV:p@Àºr7pÁje2񀈠À³#?󳃶À¬À¼` | `p` | `845%F4%8A%9F%B9EB%F0%A3%86%94%F4%87%AA%95%E2%A9%94(` |
| whatwg vs legacy | `	l://@526⸝v⠹5:936𥱟Hj2@9󾾑郐8Vl᢫𨔒𪒐a񏶧o?#0` | `936%F0%A5%B1%9FHj2` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs legacy | `data://9U6À±:&
@.h.41À­.dÁ¥.À²-91HW6q4À¹𪡂1KÁª-l񅷀765jLU1u5WL28EXMe-7À¿p𡣁#󱴲𢺺񡶿񄟤𳃁` | `&` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs legacy | `jms://QP1km1TV:p@` | `p` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs legacy | `data://9U6À±` | `&` | `%E2%8C%AF3G3b1%3A%x` |
| whatwg vs ada | `data://9U6À±:&
@.h.41À­.dÁ¥.À²-91HW6q4À¹򪃂1KÊª-l󛟰765jLU1u5WL28EXMe-7À¿p𩸁#򩂲𩷸𡓺ᬋ�򑐤𙒥` | `&` | `3%0B%E1%B6%9F74c2.88.1.20%3A0072%3E%E2%A7%AA%16&*'` |
| whatwg vs node | `wss://0xb8pmKx6k4@[a4:3:9:FF:4:7:7E:df]:5≯&6-wYv񃞲𯿠h1=Ԁo5H71j}Z55(9@1JLw5x?#` | `3%3A9%3AFF%3A4%3A7%3A7E%3Adf%5D%3A5%E2%91%BF&6-wYv%F0%A3%BF%92%E1%9F%81h1%3D%D4%80o5H71j%7DZ55(9` | `1vZM` |



| legacy vs node | `data://787: ᣸3F1@f:315􁼬34\lj45L@U1D=y!c9A/.W#8` | `%20%E1%A3%B83F1%40f%08%3A315%F4%81%BC%AC34%5Clj45L` | ` ᣸3F1|f:315􁼬34\lj45L` |
| legacy vs node | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~𯞻e,0i2IX@1j36y_82.Fv#` | `H6%40%40%3A33~%F0%AF%9E%BBe,0i2IX` | `H6@@:33~𯞻e,0i2IX` |
| legacy vs node | `jar://70odWU9.66:7AzV33629mAxq3Dn􈻝銜H93MAjU7i@52.6.7Dm0t6/E3g{^0R4I6?#` | `7AzV33629mAxq3Dn%F4%88%BB%9D%E9%8A%9CH93MAjU7i` | `7AzV33629mAxq3Dn􈻝銜H93MAjU7i` |
| legacy vs node | `wss://2񌖓A B.70Urs5T3150524mqO:87󳫍9NcP7k3j6@(58?9uVD9V#` | `87%F3%B3%AB%8D%1D9NcP7k3j6` | `87󳫍9NcP7k3j6` |
| legacy vs node | `ws://5Bwl0o1Q197LGAH:37K04G83WYx|bFJ8qZay736m94AQ~
uUx@-j-6.785-.7g6wf2`?#` | `37K04G83WYx%7CbFJ8qZay736m94AQ~
uUx` | `37K04G83WYx|bFJ8qZay736m94AQ~
uUx` |
| legacy vs whatwg | `data://787: ᳨3F1@f:315𢰬34\lj45L@U1D=y!c9A/.W#8` | `%20%E1%A3%B83F1%40f%08%3A315%F4%81%BC%AC34%5Clj45L` | ` ᳨3F1` |
| legacy vs whatwg | `wss://2𢶖3∽⌞5.70Urs5T3150524mqO:87𼺭9NcP7k3j6@(58?9uVD9V#` | `87%F3%B3%AB%8D%1D9NcP7k3j6` | `87𼺭9NcP7k3j6` |

| legacy vs rust-url | `data://787: ᣸3F1@f:315􁼬34\lj45L@U1D=y!c9A/.W#8` | `%20%E1%A3%B83F1%40f%08%3A315%F4%81%BC%AC34%5Clj45L` | ` ᣸3F1` |
| legacy vs rust-url | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~𯞻e,0i2IX@1j36y_82.Fv#` | `H6` | `H6%40%40%3A33~%F0%AF%9E%BBe,0i2IX` |
| legacy vs rust-url | `jar://70odWU9.66:7AzV33629mAxq3Dn􈻝銜H93MAjU7i@52.6.7Dm0t6/E3g{^0R4I6?#` | `7AzV33629mAxq3Dn%F4%88%BB%9D%E9%8A%9CH93MAjU7i` | `7AzV33629mAxq3Dn􈻝銜H93MAjU7i` |
| legacy vs rust-url | `wss://2􌖓A
B.70Urs5T3150524mqO:87󳫍9NcP7k3j6@(58?9uVD9V#` | `87%F3%B3%AB%8D%1D9NcP7k3j6` | `87󳫍9NcP7k3j6` |
| legacy vs rust-url | `ws://5Bwl0o1Q197LGAH:37K04G83WYx|bFJ8qZay736m94AQ~
uUx@-j-6.785-.7g6wf2`?#` | `37K04G83WYx%7CbFJ8qZay736m94AQ~uUx` | `37K04G83WYx` |
| legacy (1) vs rust-url (4) | `data://787: ࣸ3F1@f:315𗴬34\lj45L@U1D=y!c9A/.W#8` | `%20%E1%A3%B83F1%40f%08%3A315%F4%81%BC%AC34%5Clj45L` | ` ࣸ3F1` |
| legacy (1) vs rust-url (4) | `onenote://6I0Z4MRm98vq8Y5r0:H6@@:33~િʽe,0i2IX@1j36y_82.Fv#` | `H6%40%40%3A33~%F0%AF%9E%BBe,0i2IX` | `H6` |
| legacy (1) vs rust-url (4) | `jar://70odWU9.66:7AzV33629mAxq3Dn𘦝툌�H93MAjU7i@52.6.7Dm0t6/E3g{^0R4I6?#` | `7AzV33629mAxq3Dn%F4%88%BB%9D%E9%8A%9CH93MAjU7i` | `7AzV33629mAxq3Dn𘦝툌�H93MAjU7i` |
