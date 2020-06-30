## JSON dumps

#### fake-512b.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.4226 |  1.0000 |
| ujson         |    0.7370 |  1.7438 |
| rapidjson     |    1.0284 |  2.4334 |
| rapidjson(n)  |    1.0853 |  2.5680 |
| hyperjson     |    1.0892 |  2.5772 |
| builtin       |    1.4856 |  3.5154 |

#### fake-5kb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.4140 |  1.0000 |
| ujson         |    0.8862 |  2.1407 |
| hyperjson     |    1.0997 |  2.6565 |
| rapidjson(n)  |    1.3551 |  3.2734 |
| rapidjson     |    1.3813 |  3.3367 |
| builtin       |    1.6061 |  3.8798 |

#### fake-1mb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.5619 |  1.0000 |
| ujson         |    0.9957 |  1.7723 |
| hyperjson     |    1.2603 |  2.2431 |
| rapidjson(n)  |    1.6099 |  2.8654 |
| rapidjson     |    1.6471 |  2.9315 |
| builtin       |    2.3227 |  4.1340 |

#### apache.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.6360 |  1.0000 |
| hyperjson     |    1.8177 |  2.8582 |
| rapidjson(n)  |    1.8831 |  2.9611 |
| rapidjson     |    1.8835 |  2.9617 |
| ujson         |    1.9042 |  2.9942 |
| builtin       |    2.9560 |  4.6481 |

#### canada.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.4986 |  1.0000 |
| hyperjson     |    0.9992 |  2.0040 |
| ujson         |    1.7176 |  3.4446 |
| rapidjson(n)  |    5.5233 | 11.0769 |
| rapidjson     |    5.5302 | 11.0908 |
| builtin       |    5.7169 | 11.4653 |

#### ctm.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    1.0081 |  1.0000 |
| rapidjson(n)  |    1.7645 |  1.7503 |
| rapidjson     |    2.2429 |  2.2248 |
| ujson         |    2.3506 |  2.3316 |
| hyperjson     |    3.1209 |  3.0958 |
| builtin       |    4.2867 |  4.2521 |

#### github.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.5736 |  1.0000 |
| hyperjson     |    1.3880 |  2.4198 |
| ujson         |    1.4201 |  2.4758 |
| rapidjson(n)  |    1.6050 |  2.7981 |
| rapidjson     |    1.6461 |  2.8698 |
| builtin       |    2.2910 |  3.9941 |

#### instruments.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.8074 |  1.0000 |
| rapidjson(n)  |    2.0267 |  2.5100 |
| ujson         |    2.3693 |  2.9343 |
| rapidjson     |    2.4672 |  3.0556 |
| hyperjson     |    3.5087 |  4.3455 |
| builtin       |    4.0396 |  5.0029 |

#### mesh.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.4365 |  1.0000 |
| ujson         |    0.9487 |  2.1732 |
| hyperjson     |    1.0490 |  2.4031 |
| rapidjson(n)  |    2.6243 |  6.0117 |
| rapidjson     |    2.8687 |  6.5715 |
| builtin       |    2.9848 |  6.8375 |

#### truenull.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.1478 |  1.0000 |
| rapidjson(n)  |    0.3193 |  2.1602 |
| rapidjson     |    0.3236 |  2.1889 |
| builtin       |    0.5081 |  3.4373 |
| ujson         |    0.5427 |  3.6715 |
| hyperjson     |    3.2354 | 21.8866 |

#### tweet.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.5104 |  1.0000 |
| ujson         |    1.4380 |  2.8175 |
| rapidjson(n)  |    1.4978 |  2.9346 |
| rapidjson     |    1.5162 |  2.9708 |
| builtin       |    2.2467 |  4.4020 |
| hyperjson     |    2.3282 |  4.5617 |

#### twitter.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |    0.7977 |  1.0000 |
| ujson         |    1.7136 |  2.1483 |
| rapidjson(n)  |    1.8600 |  2.3319 |
| rapidjson     |    1.9291 |  2.4184 |
| hyperjson     |    2.5542 |  3.2022 |
| builtin       |    2.6380 |  3.3072 |

#### Summary

| callee_name   |   mean |   median |
|:--------------|-------:|---------:|
| orjson        | 1.0000 |   1.0000 |
| ujson         | 2.5540 |   2.4037 |
| hyperjson     | 4.5211 |   2.7574 |
| rapidjson(n)  | 3.6035 |   2.8318 |
| rapidjson     | 3.7545 |   2.9466 |
| builtin       | 4.9063 |   4.1930 |

