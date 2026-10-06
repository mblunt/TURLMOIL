# Scheme colon handling

**Description:** One parser includes the trailing colon in scheme, the other excludes it

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| legacy vs curl | `go://5j7TF3XR` | `go:` | `go` |
| legacy vs curl | `soldatpwid://...` | `soldatpwid:` | `soldatpwid` |
| legacy vs curl | `wss://file://...` | `wss:` | `wss` |
| legacy vs curl | `file:/%2F...` | `file:` | `file` |
| legacy vs curl | `http://558:...` | `http:` | `http` |
| legacy vs curl | `http://tB9maq36Xi...` | `http:` | `http` |
| legacy vs curl | `file:////DSZj0MUIs...` | `file:` | `file` |
| legacy vs curl | `data://S1u68...` | `data:` | `data` |
| legacy vs curl | `ws://do2ycs037T...` | `ws:` | `ws` |
| legacy vs curl | `http://ftp://3Z28...` | `http:` | `http` |
| legacy vs curl | `https://https://51...` | `https:` | `https` |
| legacy vs curl | `dnsm8t:Y@...` | `dnsm8t:` | `dnsm8t` |
| legacy vs curl | `https://0a48...` | `https:` | `https` |
| legacy vs curl | `ftp://9𦄴...` | `ftp` | `ftp:` |
| legacy vs curl | `ms-settingsthingsms-walk-to://...` | `ms-settingsthingsms-walk-to:` | `ms-settingsthingsms-walk-to:` |
| legacy vs curl | `data://9m4...` | `data:` | `data` |
| legacy vs curl | `data://file://...` | `data:` | `data` |
| legacy vs curl | `data://data://...` | `data:` | `data` |
| legacy vs curl | `http://Sh7/...` | `http:` | `http` |
| legacy vs curl | `ws://ftp://...` | `ws:` | `ws` |
| legacy vs curl | `ws://http://...` | `ws:` | `ws` |
| legacy vs curl | `slopenpgp4fprafq7://...` | `slopenpgp4fprafq7:` | `slopenpgp4fprafq7` |
| legacy vs curl | `https://https://J:...` | `https:` | `https` |
