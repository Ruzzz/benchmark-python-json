## JSON loads

### fake-512b.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| ujson        |   1.07366 | 1       |
| rapidjson(n) |   1.17244 | 1.092   |
| rapidjson    |   1.22949 | 1.14514 |
| orjson       |   1.53646 | 1.43104 |
| hyperjson    |   2.36333 | 2.20119 |
| builtin      |   3.36872 | 3.1376  |

### fake-5kb.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| ujson        |   1.49669 | 1       |
| rapidjson(n) |   1.64586 | 1.09966 |
| orjson       |   1.68428 | 1.12534 |
| rapidjson    |   1.84215 | 1.23081 |
| hyperjson    |   2.62557 | 1.75425 |
| builtin      |   3.79367 | 2.5347  |

### fake-1mb.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| ujson        |   1.98813 | 1       |
| rapidjson(n) |   2.17079 | 1.09187 |
| orjson       |   2.21765 | 1.11544 |
| rapidjson    |   2.33399 | 1.17396 |
| hyperjson    |   3.20157 | 1.61034 |
| builtin      |   4.31349 | 2.16962 |

### apache.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   1.73378 | 1       |
| builtin      |   2.21708 | 1.27875 |
| ujson        |   2.25927 | 1.30309 |
| rapidjson    |   2.56814 | 1.48124 |
| rapidjson(n) |   2.5997  | 1.49944 |
| hyperjson    |   3.0831  | 1.77825 |

### canada.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   1.62322 | 1       |
| rapidjson(n) |   1.62744 | 1.0026  |
| ujson        |   2.08461 | 1.28424 |
| hyperjson    |   2.14488 | 1.32137 |
| builtin      |   3.93968 | 2.42707 |
| rapidjson    |   4.1002  | 2.52596 |

### ctm.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   4.57388 | 1       |
| ujson        |   5.87768 | 1.28505 |
| rapidjson(n) |   6.17932 | 1.351   |
| rapidjson    |   6.92899 | 1.5149  |
| builtin      |   7.02196 | 1.53523 |
| hyperjson    |   8.05174 | 1.76037 |

### github.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   1.34867 | 1       |
| ujson        |   1.75791 | 1.30343 |
| builtin      |   1.84029 | 1.36452 |
| rapidjson(n) |   1.92355 | 1.42625 |
| rapidjson    |   1.98188 | 1.4695  |
| hyperjson    |   2.48691 | 1.84396 |

### instruments.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   2.30303 | 1       |
| ujson        |   3.10792 | 1.34949 |
| rapidjson(n) |   3.32241 | 1.44262 |
| builtin      |   3.902   | 1.69429 |
| rapidjson    |   4.26696 | 1.85276 |
| hyperjson    |   5.21585 | 2.26477 |

### mesh.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.563903 | 1       |
| rapidjson(n) |  0.626535 | 1.11107 |
| ujson        |  0.700556 | 1.24233 |
| hyperjson    |  0.960004 | 1.70243 |
| builtin      |  1.1074   | 1.96382 |
| rapidjson    |  1.41312  | 2.50597 |

### truenull.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| ujson        |  0.224341 | 1       |
| orjson       |  0.244418 | 1.08949 |
| rapidjson    |  0.249284 | 1.11118 |
| rapidjson(n) |  0.254347 | 1.13375 |
| builtin      |  0.261114 | 1.16391 |
| hyperjson    |  0.492331 | 2.19457 |

### tweet.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   1.22825 | 1       |
| ujson        |   1.59926 | 1.30206 |
| rapidjson(n) |   1.62635 | 1.32412 |
| rapidjson    |   1.73822 | 1.4152  |
| builtin      |   1.94302 | 1.58194 |
| hyperjson    |   2.86946 | 2.33622 |

### twitter.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |   2.22697 | 1       |
| ujson        |   2.656   | 1.19265 |
| builtin      |   3.04015 | 1.36515 |
| rapidjson(n) |   3.21547 | 1.44388 |
| rapidjson    |   3.59227 | 1.61308 |
| hyperjson    |   4.48714 | 2.01491 |

### Summary

| callee       |    mean |   median |
|:-------------|--------:|---------:|
| orjson       | 1.06344 |  1       |
| rapidjson(n) | 1.25152 |  1.22893 |
| ujson        | 1.18853 |  1.26329 |
| rapidjson    | 1.58664 |  1.47537 |
| builtin      | 1.85138 |  1.63811 |
| hyperjson    | 1.89855 |  1.81111 |

