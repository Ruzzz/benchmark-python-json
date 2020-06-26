## JSON dumps

### fake-512b.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.499733 | 1       |
| ujson        |  0.956588 | 1.9142  |
| rapidjson    |  1.27801  | 2.55739 |
| rapidjson(n) |  1.27924  | 2.55984 |
| hyperjson    |  1.48591  | 2.9734  |
| builtin      |  1.75281  | 3.50749 |

### fake-5kb.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.406524 | 1       |
| ujson        |  0.754678 | 1.85642 |
| hyperjson    |  0.996872 | 2.45218 |
| rapidjson(n) |  1.24306  | 3.05778 |
| rapidjson    |  1.27708  | 3.14146 |
| builtin      |  1.37305  | 3.37754 |

### fake-1mb.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.554202 | 1       |
| ujson        |  0.968093 | 1.74682 |
| hyperjson    |  1.42418  | 2.56979 |
| rapidjson(n) |  1.58954  | 2.86816 |
| rapidjson    |  1.63238  | 2.94546 |
| builtin      |  2.33727  | 4.21736 |

### apache.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.629915 | 1       |
| hyperjson    |  1.82538  | 2.89782 |
| ujson        |  1.85414  | 2.94348 |
| rapidjson    |  1.88337  | 2.98988 |
| rapidjson(n) |  1.88525  | 2.99287 |
| builtin      |  2.94369  | 4.67316 |

### canada.json

| callee       |   elapsed |    ratio |
|:-------------|----------:|---------:|
| orjson       |  0.495562 |  1       |
| hyperjson    |  0.997357 |  2.01258 |
| ujson        |  1.69461  |  3.41958 |
| rapidjson(n) |  5.47749  | 11.0531  |
| rapidjson    |  5.49845  | 11.0954  |
| builtin      |  5.63927  | 11.3795  |

### ctm.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.992005 | 1       |
| rapidjson(n) |  1.74665  | 1.76073 |
| rapidjson    |  2.18218  | 2.19977 |
| ujson        |  2.30588  | 2.32446 |
| hyperjson    |  3.11334  | 3.13843 |
| builtin      |  4.22117  | 4.25519 |

### github.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.570192 | 1       |
| hyperjson    |  1.3892   | 2.43637 |
| ujson        |  1.39381  | 2.44446 |
| rapidjson(n) |  1.58935  | 2.78739 |
| rapidjson    |  1.62478  | 2.84953 |
| builtin      |  2.18464  | 3.83141 |

### instruments.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.786712 | 1       |
| rapidjson(n) |  2.01107  | 2.55629 |
| ujson        |  2.32475  | 2.95502 |
| rapidjson    |  2.45303  | 3.11808 |
| hyperjson    |  3.47484  | 4.41692 |
| builtin      |  4.01021  | 5.09743 |

### mesh.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.455774 | 1       |
| ujson        |  0.955233 | 2.09585 |
| hyperjson    |  1.08532  | 2.38126 |
| rapidjson(n) |  2.65283  | 5.82049 |
| rapidjson    |  2.86774  | 6.29202 |
| builtin      |  2.9505   | 6.4736  |

### truenull.json

| callee       |   elapsed |    ratio |
|:-------------|----------:|---------:|
| orjson       |  0.148107 |  1       |
| rapidjson    |  0.31453  |  2.12367 |
| rapidjson(n) |  0.320403 |  2.16333 |
| builtin      |  0.491474 |  3.31838 |
| ujson        |  0.547112 |  3.69404 |
| hyperjson    |  3.21812  | 21.7284  |

### tweet.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.502274 | 1       |
| ujson        |  1.41528  | 2.81775 |
| rapidjson(n) |  1.50031  | 2.98704 |
| rapidjson    |  1.50912  | 3.00458 |
| builtin      |  2.19348  | 4.3671  |
| hyperjson    |  2.35034  | 4.67939 |

### twitter.json

| callee       |   elapsed |   ratio |
|:-------------|----------:|--------:|
| orjson       |  0.772852 | 1       |
| ujson        |  1.67792  | 2.17108 |
| rapidjson(n) |  1.82739  | 2.36448 |
| rapidjson    |  1.90073  | 2.45936 |
| hyperjson    |  2.51035  | 3.24816 |
| builtin      |  2.59461  | 3.35718 |

### Summary

| callee       |    mean |   median |
|:-------------|--------:|---------:|
| orjson       | 1       |  1       |
| ujson        | 2.53193 |  2.38446 |
| rapidjson(n) | 3.58096 |  2.82777 |
| hyperjson    | 4.57789 |  2.93561 |
| rapidjson    | 3.73138 |  2.96767 |
| builtin      | 4.82128 |  4.23628 |

