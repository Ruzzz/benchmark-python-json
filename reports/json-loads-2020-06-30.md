## JSON loads

#### fake-512b.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |    1.1690 |  1.0000 |
| rapidjson(n)  |    1.2306 |  1.0527 |
| rapidjson     |    1.3755 |  1.1766 |
| orjson        |    1.6423 |  1.4049 |
| hyperjson     |    2.4283 |  2.0772 |
| builtin       |    3.6664 |  3.1364 |

#### fake-5kb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |    1.4905 |  1.0000 |
| rapidjson(n)  |    1.6735 |  1.1228 |
| orjson        |    1.7074 |  1.1455 |
| rapidjson     |    1.7844 |  1.1972 |
| hyperjson     |    2.3176 |  1.5550 |
| builtin       |    3.9665 |  2.6613 |

#### fake-1mb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |    1.9728 |  1.0000 |
| rapidjson(n)  |    2.2025 |  1.1165 |
| rapidjson     |    2.3892 |  1.2111 |
| orjson        |    2.4233 |  1.2284 |
| hyperjson     |    3.2271 |  1.6358 |
| builtin       |    4.5504 |  2.3066 |

#### apache.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    1.7103 |  1.0000 |
| builtin       |    2.1644 |  1.2655 |
| ujson         |    2.2430 |  1.3115 |
| rapidjson(n)  |    2.5699 |  1.5026 |
| rapidjson     |    2.5832 |  1.5104 |
| hyperjson     |    3.1113 |  1.8192 |

#### canada.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| rapidjson(n)  |    1.5725 |  1.0000 |
| orjson        |    1.5801 |  1.0048 |
| ujson         |    2.0640 |  1.3126 |
| hyperjson     |    2.1468 |  1.3652 |
| builtin       |    3.9015 |  2.4811 |
| rapidjson     |    4.0780 |  2.5934 |

#### ctm.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    4.6633 |  1.0000 |
| ujson         |    5.8034 |  1.2445 |
| rapidjson(n)  |    6.1857 |  1.3265 |
| rapidjson     |    6.9202 |  1.4840 |
| builtin       |    7.0251 |  1.5065 |
| hyperjson     |    8.1371 |  1.7449 |

#### github.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    1.3193 |  1.0000 |
| ujson         |    1.7879 |  1.3551 |
| builtin       |    1.8630 |  1.4121 |
| rapidjson(n)  |    1.9497 |  1.4778 |
| rapidjson     |    2.0244 |  1.5344 |
| hyperjson     |    2.5570 |  1.9381 |

#### instruments.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    2.2980 |  1.0000 |
| ujson         |    2.9588 |  1.2876 |
| rapidjson(n)  |    3.4489 |  1.5008 |
| builtin       |    4.0021 |  1.7416 |
| rapidjson     |    4.3025 |  1.8723 |
| hyperjson     |    5.0621 |  2.2029 |

#### mesh.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.5445 |  1.0000 |
| rapidjson(n)  |    0.5670 |  1.0415 |
| ujson         |    0.6679 |  1.2267 |
| hyperjson     |    0.8871 |  1.6293 |
| builtin       |    1.1040 |  2.0277 |
| rapidjson     |    1.2955 |  2.3795 |

#### truenull.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |    0.2264 |  1.0000 |
| orjson        |    0.2423 |  1.0702 |
| rapidjson(n)  |    0.2494 |  1.1014 |
| rapidjson     |    0.2512 |  1.1095 |
| builtin       |    0.2619 |  1.1565 |
| hyperjson     |    0.4947 |  2.1848 |

#### tweet.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    1.2596 |  1.0000 |
| ujson         |    1.6265 |  1.2913 |
| rapidjson(n)  |    1.6363 |  1.2991 |
| rapidjson     |    1.7055 |  1.3540 |
| builtin       |    1.8269 |  1.4503 |
| hyperjson     |    2.7995 |  2.2225 |

#### twitter.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    2.2659 |  1.0000 |
| ujson         |    2.7499 |  1.2136 |
| builtin       |    3.0569 |  1.3491 |
| rapidjson(n)  |    3.2706 |  1.4434 |
| rapidjson     |    3.3837 |  1.4933 |
| hyperjson     |    4.4831 |  1.9785 |

#### Summary

| callee_name   |   mean |   median |
|:--------------|-------:|---------:|
| orjson        | 1.0712 |   1.0000 |
| rapidjson(n)  | 1.2488 |   1.2109 |
| ujson         | 1.1869 |   1.2356 |
| rapidjson     | 1.5763 |   1.4886 |
| builtin       | 1.8746 |   1.6240 |
| hyperjson     | 1.8628 |   1.8787 |

