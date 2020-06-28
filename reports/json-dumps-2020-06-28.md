## JSON dumps

### fake-512b.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.473276 | 1       |
| ujson         |  0.879569 | 1.85847 |
| hyperjson     |  1.39849  | 2.95492 |
| rapidjson     |  1.86071  | 3.93155 |
| rapidjson(n)  |  1.89898  | 4.01241 |
| builtin       |  2.25303  | 4.76049 |

### fake-5kb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.404353 | 1       |
| ujson         |  0.800402 | 1.97946 |
| hyperjson     |  1.08275  | 2.67774 |
| rapidjson(n)  |  1.29006  | 3.19042 |
| rapidjson     |  1.30772  | 3.23411 |
| builtin       |  1.58975  | 3.93159 |

### fake-1mb.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.55777  | 1       |
| ujson         |  0.989831 | 1.77462 |
| hyperjson     |  1.25669  | 2.25306 |
| rapidjson(n)  |  1.62855  | 2.91974 |
| rapidjson     |  1.6556   | 2.96825 |
| builtin       |  2.35696  | 4.22568 |

### apache.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.643859 | 1       |
| rapidjson     |  1.88414  | 2.92632 |
| rapidjson(n)  |  1.88739  | 2.93138 |
| ujson         |  1.91712  | 2.97754 |
| hyperjson     |  1.94463  | 3.02027 |
| builtin       |  2.9655   | 4.60582 |

### canada.json

| callee_name   |   elapsed |    ratio |
|:--------------|----------:|---------:|
| orjson        |  0.527664 |  1       |
| hyperjson     |  0.997849 |  1.89107 |
| ujson         |  1.70171  |  3.22498 |
| rapidjson     |  5.48297  | 10.391   |
| rapidjson(n)  |  5.54573  | 10.51    |
| builtin       |  5.67545  | 10.7558  |

### ctm.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |   0.9988  | 1       |
| rapidjson(n)  |   1.74767 | 1.74976 |
| rapidjson     |   2.21141 | 2.21406 |
| ujson         |   2.315   | 2.31778 |
| hyperjson     |   3.10726 | 3.11099 |
| builtin       |   4.29246 | 4.29761 |

### github.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.566375 | 1       |
| ujson         |  1.40717  | 2.48451 |
| hyperjson     |  1.45163  | 2.56301 |
| rapidjson(n)  |  1.59111  | 2.80929 |
| rapidjson     |  1.62674  | 2.87219 |
| builtin       |  2.19684  | 3.87877 |

### instruments.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.814104 | 1       |
| rapidjson(n)  |  2.05214  | 2.52073 |
| ujson         |  2.34315  | 2.8782  |
| rapidjson     |  2.49675  | 3.06686 |
| hyperjson     |  3.59825  | 4.41989 |
| builtin       |  4.04319  | 4.96643 |

### mesh.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.43776  | 1       |
| ujson         |  0.982093 | 2.24345 |
| hyperjson     |  1.04956  | 2.39757 |
| rapidjson(n)  |  2.60379  | 5.94799 |
| rapidjson     |  2.85918  | 6.5314  |
| builtin       |  2.93982  | 6.7156  |

### truenull.json

| callee_name   |   elapsed |    ratio |
|:--------------|----------:|---------:|
| orjson        |  0.14982  |  1       |
| rapidjson     |  0.314163 |  2.09693 |
| rapidjson(n)  |  0.317222 |  2.11735 |
| builtin       |  0.484453 |  3.23356 |
| ujson         |  0.538865 |  3.59674 |
| hyperjson     |  3.18511  | 21.2595  |

### tweet.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.501781 | 1       |
| ujson         |  1.42425  | 2.83839 |
| rapidjson(n)  |  1.48957  | 2.96856 |
| rapidjson     |  1.5136   | 3.01646 |
| builtin       |  2.19983  | 4.38404 |
| hyperjson     |  2.36858  | 4.72034 |

### twitter.json

| callee_name   |   elapsed |   ratio |
|:--------------|----------:|--------:|
| orjson        |  0.783495 | 1       |
| ujson         |  1.73375  | 2.21283 |
| rapidjson(n)  |  1.89307  | 2.41618 |
| rapidjson     |  1.95661  | 2.49729 |
| hyperjson     |  2.59704  | 3.31469 |
| builtin       |  2.63347  | 3.36118 |

### Summary

| callee_name   |    mean |   median |
|:--------------|--------:|---------:|
| orjson        | 1       |  1       |
| ujson         | 2.53225 |  2.40115 |
| rapidjson(n)  | 3.67448 |  2.92556 |
| hyperjson     | 4.54859 |  2.98759 |
| rapidjson     | 3.8122  |  2.99236 |
| builtin       | 4.92638 |  4.34083 |

