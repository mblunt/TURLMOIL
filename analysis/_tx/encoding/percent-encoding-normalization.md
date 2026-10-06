# Percent-encoding case or normalization

**Description:** Differences in how userinfo is percent-encoded or normalized in authority

| Pair | URL | value_a | value_b |
|------|-----|---------|---------|
| whatwg vs legacy | `data://787: ᣸3F1@f:315􃁬34\lj45L@U1D=y!c9A/.W#8` | `U1D=y!c9A` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs legacy | `apt://9KrJFVkX2745kec⫨V0CgY7k8f9NCG-6Ay8f0.FP1:6379?#` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1:6379` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs legacy | `data://787` | `U1D=y!c9A` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs legacy | `apt://9KrJFVkX2745kec` | `9KrJFVkX2745kec%EE%9A%A5%E2%AB%A8V0CgY7k8f9NCG-6Ay8f0.FP1:6379` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs legacy | `dtn://K)5@nKI.Zv08` | `66z%F2%B1%B8%87%F4%81%97%BE` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs legacy | `market://E0U` | `E0U%F1%97%8C%98_%13%F0%A7%99%AE%E2%99%B4` | `d892-2M8jL50%F4%87%A6%8F%E2%8D%903QJI84Ab5B2P743P` |
| whatwg vs python | `go://5j7TF3XR񊳉
ࣼ␕
40xvr@2203��o20O/../A2CqL?#
q6%F3%BD%A3%B1%E2%AA%A8%1F` | `2203%F3%99%B9%A8o20O` | `01Y91NHir0%EC%92%9Cy%F1%B2%98%A58%F3%B7%9F%99Y4` |
| whatwg vs python | `Giris.lwzxconicap://q6򍖡⪨/cG348g@25。2。8。5.85.3.86:820𞣹
2UtY8ui631j10130849?#` | `q6%F3%BD%A3%B1%E2%AA%A8%1F` | `01Y91NHir0%EC%92%9Cy%F1%B2%98%A58%F3%B7%9F%99Y4` |
| uripara vs php-http | `data://4444r� 2@9rM� H3F574l69.1mg-y
3� #ᴵ 07!2Oun0Ya1692h3~f4u4T?#` | `9rM%EF%BD%A1H3F574l69.1mg-y%1B3%F1%82%9B%9F` | `52.9.3.6411;5` |
| legacy vs jsprim | `go://5j7TF3XR𫓉
󰲨🦕🂐40xvr@2203𒖙ੈo20O/../A2CqL?#` | `2203%F3%99%B9%A8o20O` | `5j7TF3XR𫓉
󰲨🦕🂐40xvr@2203𒖙ੈo20O` |
| legacy vs jsprim | `dtn://K)5@nKI.Zv08-4-6F9R0A95:16@66z𚚇𑟾?#~n\sp` | `66z%F2%B1%B8%87%F4%81%97%BE` | `K)5@nKI.Zv08-4-6F9R0A95:16@66z𚚇𑟾` |
| legacy vs jsprim | `onenote://Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J?#wy` | `%043324G845648oko2d9s8J` | `Dau2OPU1AA160YYvo83:2q0r65Q18xZ3X@3324G845648oko2d9s8J` |
