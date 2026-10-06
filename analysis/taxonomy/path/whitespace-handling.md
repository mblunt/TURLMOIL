# Whitespace Handling

**Description:** Parsers differ on whether whitespace characters (tabs, newlines, spaces, control chars) in the path are stripped, percent-encoded, or left raw.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|

| javascript-whatwg vs javascript-parse-uri | `ms-sttoverlay://ms-sttoverlay://SS19m05: ,@-q-:6)7Ah21;eUh9;9B35):0n?#` | `//SS19m05:%20%07%7F,@-q-:6)7Ah21;eUh9;9B35):0n` | `//SS19m05:%20,@-q-:6)7Ah21;eUh9;9B35):0n` |
| javascript-whatwg vs javascript-parse-uri | `https://J:G7\t@9.95.9.93:60)%6M2UuZ9(Z3NX^yMO.9.?#88V66W[` | `//J:G7%09@9.95.9.93:60)%6M2UuZ9(Z3NX%5EyMO.9.` | `//J:G7@9.95.9.93:60)%6M2UuZ9(Z3NX%5EyMO.9.` |
| javascript-whatwg vs javascript-url-parse | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
test/1S2]Tjva9D{0?#` | `//SIJ8Uau5YOu979XGK%0B%0B0033x82x@9%E2%AA%B13365test/1S2]Tjva9D%7B0` | `//SIJ8Uau5YOu979XGK0033x82x@9
test/1S2]Tjva9D{0` |
| javascript-whatwg vs javascript-urijs | `https://https://J:G7	@9.95.9.93:60x%6M2UuZ9?#88V66W[` | `//J:G7%09@9.95.9.93:60x%6M2UuZ9` | `//J:G7	@9.95.9.93:60x%6M2UuZ9` |
| javascript-whatwg vs javascript-url-parse | `https://https://Na1P408[33:E:49:F:ee:df:DC:e2]385l@x466KK;?#` | `//Na1P408[33:E:49:F:ee:df:DC:e2]385l@x466KK;` | `//Na%0C%171P408[33:E:49:F:ee:df:DC:e2]385l@%0Bx466KK;` |
| javascript-whatwg vs javascript-urijs | `ftp://ftp://4c8j8k2LN2g4gttpz5l	xyz@54.5.3.42:75CdO16?#` | `//4c8j8k2LN2g4gttpz5l%09xyz@54.5.3.42:75CdO16` | `//4c8j8k2LN2g4gttpz5l	xyz@54.5.3.42:75CdO16` |
| javascript-whatwg vs javascript-fast-url-parser | `https://https://J:G7	@9.95.9.93:60x%6M2UuZ9?#88V66W[` | `//J:G7@9.95.9.93:60x%6M2UuZ9` | `//J:G7%09@9.95.9.93:60x%6M2UuZ9` |
| javascript-whatwg vs javascript-fast-url-parser | `ms-sttoverlay://ms-sttoverlay://SS19m05: ,@-q-:6)7Ah21;eUh9;9B35):0n?#` | `//SS19m05:%20,@-q-:6)7Ah21;eUh9;9B35):0n` | `//SS19m05:%20%07%7F,@-q-:6)7Ah21;eUh9;9B35):0n` |
| csharp-systemuri vs rust-url | `lastfm://vQ931tsj0/../dhqo914crJ@-7zZ54:827
?2P5#` | `/dhqo914crJ@-7zZ54:827%0A` | `/dhqo914crJ@-7zZ54:827` |
| csharp-systemuri vs rust-url | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504x!yz]?#` | `//M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504x%0D!yz]` | `//M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504x!yz]` |
| csharp-systemuri vs rust-url | `data:///...1l4Vt76p7E08EnuFZ
ak282Qm25.U928qq8:1D68v30j?#` | `/...1l4Vt76p7E08EnuFZ%0Aak282Qm25.U928qq8:1D68v30j` | `/...1l4Vt76p7E08EnuFZak282Qm25.U928qq8:1D68v30j` |
| javascript-uri-js vs javascript-url-parse | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365 KNi+*e!cI/1S2]Tjva9D{0?#` | `//SIJ8Uau5YOu979XGK0033x82x@9⪱3365 KNi+*e!cI/1S2]Tjva9D{0` | `//SIJ8Uau5YOu979XGK%0B%0B0033x82x@9%E2%AA%B13365-%F1%9D%B1%B4%20KNi+*e!cI/1S2]Tjva9D%7B0` |
| javascript-uri-js vs javascript-url-parse | `ftp://ftp://4c8j8k2LN2g4gttpz5l	𧸚xyz@54.5.3.42:75CdO16GrNsPV2ev?#` | `//4c8j8k2LN2g4gttpz5l𧸚xyz@54.5.3.42:75CdO16GrNsPV2ev` | `//4c8j8k2LN2g4gttpz5l%F0%A7%B8%9A%E2%B2%90%F4%8E%A7%95^[ %F3%BE%BD%81%F0%A7%AA%96%03H%20%F0%AE%BE%9A@54.5.3.42:75CdO16GrNsPV2ev` |
| javascript-legacy vs javascript-fast-url-parser | `https://E294t85xyz@
5E3abcwHxyz567?#` | `%205E%0D3abcwHxyz567` | `%205E3abcwHxyz567` |
| javascript-legacy vs javascript-fast-url-parser | `https://M5524Txyzl0j@6-40S18n2Q683:3001{:xyzF02-p	7?#` | `%7B:xyzF02-p7` | `/:3001%7B:xyzF02-p%097` |
| javascript-whatwg vs csharp-systemuri | `ws://hrl49V3Q50/...8f77gTbO:5T@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250⪼
C58?#` | `/...8f77gTbO:%0D5T@H4t%F0%A0%AB%A9%F0%A9%8E%A1@xvk.K-.M.5..96U37-N:3250%E2%AA%BC%0AC58` | `/...8f77gTbO:5T@H4t%F0%A0%AB%A9%F0%A9%8E%A1@xvk.K-.M.5..96U37-N:3250%E2%AA%BCC58` |
| javascript-whatwg vs csharp-systemuri | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
⪱3365-abc KNi+*e!cI/1S2]Tjva9D{0?#` | `//SIJ8Uau5YOu979XGK%0B%0B0033x82x@9%0D%E2%AA%B13365-abc KNi+*e!cI/1S2]Tjva9D%7B0` | `//SIJ8Uau5YOu979XGK%0B%0B0033x82x@9%E2%AA%B13365-abc KNi+*e!cI/1S2]Tjva9D%7B0` |
| javascript-whatwg vs csharp-systemuri | `https://https://J:G7	@9.95.9.93:60)?#` | `//J:G7@9.95.9.93:60)` | `//J:G7%09@9.95.9.93:60)` |
| csharp-systemuri vs elixir-uri | `ws://hrl49V3Q50/...8f77gTbO:5T@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250⪼
C58?#` | `/...8f77gTbO:%0D5T@H4t%F0%A0%AB%A9%F0%A9%8E%A1@xvk.K-.M.5..96U37-N:3250%E2%AA%BC%0AC58` | `/...8f77gTbO:5T@H4t𠫩𩎡@xvk.K-.M.5..96U37-N:3250⪼
C58` |
| csharp-systemuri vs elixir-uri | `https://189q46u/...r62h66SP2ksO	𦾻4nZ3G81tolVKM@322N8QX8?#` | `/...r62h66SP2ksO%09%F0%B6%BE%9B4nZ3G81tolVKM@322N8QX8` | `/...r62h66SP2ksO	𦾻4nZ3G81tolVKM@322N8QX8` |
| java-okhttp vs rust-url | `https://https://51xyz
	#gYIkh15L@:^4;74cr3?#` | `//51xyz%0C%0B` | `//51xyz
` |
| java-okhttp vs rust-url | `https://file://M8d3V2U_z@xyzabc:9504xyz!abc]#xyz?#` | `//M8d3V2U_z@xyzabc:9504xyz%0D!abc]` | `//M8d3V2U_z@xyzabc:9504xyz!abc]` |
| csharp-systemuri vs rust-url | `lastfm://vQ931tsj0/../dhqo@-7zZ54:827
?5abc?#` | `/dhqo@-7zZ54:827%0A` | `/dhqo@-7zZ54:827` |
| csharp-systemuri vs rust-url | `http://https://8Lxyz
9F@[A:e:6:E:4d:e:f:d1]:4026abc?#` | `//8Lxyz%0A9F@[A:e:6:E:4d:e:f:d1]:4026abc` | `//8Lxyz9F@[A:e:6:E:4d:e:f:d1]:4026abc` |
| csharp-systemuri vs rust-url | `data://file://5n1F@1L50.-.HYi04189.-gq:3167jDk192~8k7/0Zu428Yk?` | `//5n1%0DF@1L50.-.HYi04189.-gq:3167jDk192~8k7/0Zu428Yk` | `//5n1F@1L50.-.HYi04189.-gq:3167jDk192~8k7/0Zu428Yk` |
