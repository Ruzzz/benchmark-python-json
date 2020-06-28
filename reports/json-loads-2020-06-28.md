## JSON loads

### fake-512b.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |  0.804319 | 1       |
| rapidjson(n)  |  0.981083 | 1.21977 |
| rapidjson     |  1.05281  | 1.30895 |
| orjson        |  1.40376  | 1.74528 |
| hyperjson     |  1.97686  | 2.4578  |
| builtin       |  3.47531  | 4.32081 |

### fake-5kb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |   1.50261 | 1       |
| rapidjson(n)  |   1.6032  | 1.06694 |
| orjson        |   1.63428 | 1.08762 |
| rapidjson     |   1.7928  | 1.19312 |
| hyperjson     |   2.36933 | 1.57681 |
| builtin       |   4.38159 | 2.91598 |

### fake-1mb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |   1.95164 | 1       |
| rapidjson(n)  |   2.04021 | 1.04538 |
| orjson        |   2.12726 | 1.08999 |
| rapidjson     |   2.27856 | 1.16751 |
| hyperjson     |   3.12168 | 1.59952 |
| builtin       |   4.58189 | 2.34772 |

### apache.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   1.73101 | 1       |
| builtin       |   2.13914 | 1.23578 |
| ujson         |   2.2302  | 1.28838 |
| rapidjson(n)  |   2.54066 | 1.46773 |
| rapidjson     |   2.62743 | 1.51786 |
| hyperjson     |   3.10076 | 1.7913  |

### canada.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| rapidjson(n)  |   1.52759 | 1       |
| orjson        |   1.5634  | 1.02344 |
| ujson         |   2.0459  | 1.33929 |
| hyperjson     |   2.10509 | 1.37804 |
| builtin       |   3.89265 | 2.54822 |
| rapidjson     |   4.03046 | 2.63844 |

### ctm.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   4.61497 | 1       |
| ujson         |   5.57674 | 1.2084  |
| rapidjson(n)  |   5.96386 | 1.29228 |
| rapidjson     |   6.87359 | 1.48941 |
| builtin       |   7.17646 | 1.55504 |
| hyperjson     |   7.88272 | 1.70807 |

### github.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   1.33526 | 1       |
| ujson         |   1.81755 | 1.36119 |
| builtin       |   1.86248 | 1.39484 |
| rapidjson(n)  |   1.95643 | 1.46521 |
| rapidjson     |   2.02601 | 1.51732 |
| hyperjson     |   2.60756 | 1.95285 |

### instruments.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   2.43005 | 1       |
| ujson         |   2.94963 | 1.21381 |
| rapidjson(n)  |   3.37076 | 1.38712 |
| builtin       |   4.01915 | 1.65394 |
| rapidjson     |   4.36644 | 1.79685 |
| hyperjson     |   5.26694 | 2.16742 |

### mesh.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.541251 | 1       |
| rapidjson(n)  |  0.55749  | 1.03    |
| ujson         |  0.661779 | 1.22268 |
| hyperjson     |  0.871127 | 1.60947 |
| builtin       |  1.0874   | 2.00905 |
| rapidjson     |  1.30779  | 2.41623 |

### truenull.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| ujson         |  0.225518 | 1       |
| orjson        |  0.238425 | 1.05723 |
| rapidjson(n)  |  0.247323 | 1.09668 |
| rapidjson     |  0.250948 | 1.11276 |
| builtin       |  0.257093 | 1.14001 |
| hyperjson     |  0.495177 | 2.19573 |

### tweet.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   1.27525 | 1       |
| ujson         |   1.61155 | 1.26371 |
| rapidjson(n)  |   1.61898 | 1.26954 |
| rapidjson     |   1.70108 | 1.33392 |
| builtin       |   1.85939 | 1.45807 |
| hyperjson     |   2.86963 | 2.25026 |

### twitter.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   2.31976 | 1       |
| ujson         |   2.72414 | 1.17432 |
| builtin       |   3.20882 | 1.38325 |
| rapidjson(n)  |   3.22017 | 1.38815 |
| rapidjson     |   3.4342  | 1.48041 |
| hyperjson     |   4.56345 | 1.96721 |

### Summary

| callee_name   |    mean |   median |
|:--------------|--------:|---------:|
| orjson        | 1.08363 |  1       |
| ujson         | 1.17265 |  1.21111 |
| rapidjson(n)  | 1.2274  |  1.24466 |
| rapidjson     | 1.58107 |  1.48491 |
| builtin       | 1.99689 |  1.60449 |
| hyperjson     | 1.88787 |  1.87207 |

