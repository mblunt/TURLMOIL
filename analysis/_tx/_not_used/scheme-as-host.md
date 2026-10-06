# Scheme Parsed as Host

**Description:** A URL with a double-scheme pattern (e.g. http://https://...) causes one parser to extract the inner scheme (with or without its colon) as the host value, while another parser resolves the authority differently.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| perl-uri vs rust-url | `http://https://8L...[A:e:6:E:4d:e:f:d1]:4026...` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9...` | `http` | `http:` |
| perl-uri vs rust-url | `http://file://340`...` | `file:` | `file` |
| perl-uri vs rust-url | `http://ftp://3Z28...80155jYLqM1BW/...` | `ftp:` | `ftp` |
| js-whatwg vs perl-uri | `https://https://J:G7	@9.95.9.93:60)%6M2UuZ9...` | `https` | `https:` |
| js-whatwg vs perl-uri | `wss://wss://3:@...@ib6Oz1R2n` | `wss:` | `wss` |
| js-whatwg vs perl-uri | `wss://wss://7...@...` | `wss` | `wss:` |
| perl-uri vs rust-url | `http://https://8L...@[A:e:6:E:4d:e:f:d1]:4026...` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9...` | `http` | `http:` |
| perl-uri vs rust-url | `http://file://340`...` | `file:` | `file` |
| perl-uri vs rust-url | `http://ftp://3Z28...@[4:a:E:F4:2F:6:B:eF]...` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `http://ftp://k3YON7E1bPA9FJa0k0K...@...#` | `ftp` | `ftp:` |
| perl-uri vs rust-url | `https://https://51...@...` | `https` | `https:` |
| perl-uri vs python-urllib3 | `http://https://8L...@[A:e:6:E:4d:e:f:d1]:4026...` | `https` | `https:` |
| perl-uri vs python-urllib3 | `ws://http://SIJ8Uau5...` | `http` | `http:` |
| perl-uri vs python-urllib3 | `http://file://340`...` | `file:` | `file` |
| perl-uri vs python-urllib3 | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41...` | `file` | `file:` |
| perl-uri vs python-urllib3 | `file://7:/. lhG@Z72-Ix2v133...` | `7` | `7:` |
| perl-uri vs python-urllib3 | `http://https://8L...@[A:e:6:E:4d:e:f:d1]:4026...` | `https` | `https:` |
| perl-uri vs python-urllib3 | `ws://http://SIJ8Uau5YOu979...@9...` | `http` | `http:` |
| perl-uri vs python-urllib3 | `http://file://340`...` | `file:` | `file` |
| perl-uri vs python-urllib3 | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?...` | `file` | `file:` |
| perl-uri vs python-urllib3 | `http://ftp://3Z28...80155jYLqM1BW/...` | `ftp` | `ftp:` |
| perl-uri vs python-urllib3 | `file://ftp://557GZy...` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `http://https://8L...@[A:e:6:E:4d:e:f:d1]:4026...` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9...KNi+*e!cI/...` | `http` | `http:` |
| perl-uri vs rust-url | `http://ftp://3Z28...80155jYLqM1BW/...` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `https://https://J:G7	@9.95.9.93:60...` | `https:` | `https` |
| perl-uri vs rust-url | `https://file://M8d3V2U_z@530FD.R-o4.X06Bw4-x:9504...` | `file:` | `file` |
| perl-uri vs rust-url | `https://https://51...@:^4;74cr3:6...` | `https` | `https:` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `https:` | `https` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `file:` | `file` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `http` | `http:` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `ftp` | `ftp:` |
| perl-uri vs rust-url | `...(double-scheme URL)...` | `wss:` | `wss` |
| perl-uri vs rust-url | `http://https://8L...@[A:e:6:E:4d:e:f:d1]:4026...` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9...KNi+*e!cI/...` | `http` | `http:` |
| perl-uri vs rust-url | `http://file://340...-MhGLd54l6GF33.1.75.6:...` | `file:` | `file` |
| perl-uri vs rust-url | `http://https://8L⸔
🊔ﴀ9F@[A:e:6:E:4d:e:f:d1]:4026...?#` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9...?#` | `http` | `http:` |
| perl-uri vs rust-url | `http://ftp://3Z28...?#` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `wss://wss://3:@...@ib6Oz1R2n?` | `wss:` | `wss` |
| perl-uri vs rust-url | `https://https://J:G7\t@9.95.9.93:60...?#88V66W[` | `https:` | `https` |
| perl-uri vs rust-url | `http://https://8L...└@[A:e:6:E:4d:e:f:d1]:4026...` | `https:` | `https` |
| perl-uri vs rust-url | `ws://http://SIJ8Uau5YOu979XGK0033x82x@9
...` | `http` | `http:` |
| perl-uri vs rust-url | `http://file://340`...-MhGLd54l6GF33.1.75.6:...` | `file:` | `file` |
| perl-uri vs rust-url | `wss://file://dH9L2huC728V:b8Y5E9@[5:2D:3D:B:2A:7:68:ea]:41?...` | `file:` | `file` |
| perl-uri vs rust-url | `http://ftp://3Z28...80155jYLqM1BW/...` | `ftp:` | `ftp` |
| perl-uri vs rust-url | `https://https://J:G7	@9.95.9.93:60...` | `https:` | `https` |
