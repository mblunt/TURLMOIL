# IPv6 Zero-Group Compression

**Description:** One parser elides consecutive all-zero groups in an IPv6 address using '::' (zero compression / RFC 5952), while another retains the explicit zeros, resulting in different host strings for the same address.

| Pair | URL | host_a | host_b |
|------|-----|--------|--------|
| java-uri vs java-galimatias | `ftp://Y:f4mY2Mzg1@[a6:2:f:B0:2f:0:D:57]:38...?#q5` | `[a6:2:f:B0:2f:0:D:57]` | `a6:2:f:b0:2f::d:57` |
