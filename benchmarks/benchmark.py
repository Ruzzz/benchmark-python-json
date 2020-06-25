import json
import statistics

from collections import defaultdict
from functools import partial
from itertools import chain
from pathlib import Path
from sys import getsizeof
from time import gmtime, strftime
from typing import Tuple, Iterable, Any, NamedTuple, List, Generator

import hyperjson  # https://github.com/mre/hyperjson
import orjson  # https://github.com/ijl/orjson
import rapidjson  # https://github.com/python-rapidjson/python-rapidjson
import ujson  # https://github.com/ultrajson/ultrajson

from tabulate import tabulate

from benchmarks.helpers.auto_properties_dict import AutoPropertiesDict
from benchmarks.helpers.elapsed import Elapsed
from benchmarks.helpers.fake_json import FakeJsonGenerator, JsonTypeWeights

COUNT_FACTOR = 1
ROOT_PATH = Path(__file__).resolve().parents[1]


def _fname_ts() -> str:
    return strftime('%Y-%m-%d', gmtime())


class InData(NamedTuple):
    name: str
    data: Any
    count: int


class Result(AutoPropertiesDict):
    callee: str
    benchmark: str
    elapsed: float
    factor: float


GroupedResult = List[List[Result]]
Callee = Tuple[str, callable]


def benchmark(callees: Iterable[Callee],
              data: Iterable[InData],
              verbose=True) -> GroupedResult:
    ret = []
    for benchmark_name, benchmark_data, benchmark_count in data:
        benchmark_count = round(benchmark_count * COUNT_FACTOR)
        if verbose:
            print(benchmark_name, 'count:', benchmark_count, 'size:', getsizeof(benchmark_data))

        if benchmark_count <= 0:
            continue
        callees_group = []
        for callee_name, callee in callees:
            if verbose:
                print(' -', callee_name)

            with Elapsed() as elapsed:
                for _ in range(benchmark_count):
                    callee(benchmark_data)
            callees_group.append(Result(
                callee=callee_name,
                benchmark=benchmark_name,
                elapsed=elapsed()
            ))
        ret.append(callees_group)

    if verbose:
        print()
    return ret


def generate_fake_data(as_string=False) -> Generator[InData, None, None]:
    json_generator = FakeJsonGenerator(JsonTypeWeights(string_weight=2, number_weight=2))
    for size, count in [(500, 200000),
                        (5000, 20000),
                        (1000000, 100)]:
        data = json_generator(size)
        if as_string:
            data = json.dumps(data)
        yield InData(name=f'fake-{size}', data=data, count=count)


def load_data(as_string=False) -> Generator[InData, None, None]:
    for fname, count in [('./data/apache.json', 5000),
                         ('./data/canada.json', 100),
                         ('./data/ctm.json', 800),
                         ('./data/github.json', 8000),
                         ('./data/instruments.json', 4000),
                         ('./data/mesh.json', 200),
                         ('./data/truenull.json', 10000),
                         ('./data/tweet.json', 100000),
                         ('./data/twitter.json', 1000)]:
        fname = ROOT_PATH / fname
        with open(fname) as f:
            data = f.read()
            if not as_string:
                data = json.loads(data)
        yield InData(name=fname.name, data=data, count=count)


def report_benchmark(result: GroupedResult, fname):
    report = ''
    total_factors = defaultdict(list)

    for group in result:
        group.sort(key=lambda x: x.elapsed)
        first = group[0]
        for item in group:
            item.factor = item.elapsed / first.elapsed
            total_factors[item.callee].append(item.factor)

        report += tabulate(group, headers='keys')
        report += '\n\n'

    total_info = []
    for callee, factors in total_factors.items():
        total_info.append({
            'callee': callee,
            'mean': statistics.mean(factors),
            'median': statistics.median(factors),
        })
    total_info.sort(key=lambda x: x['median'])
    report += tabulate(total_info, headers='keys')
    report += '\n\n'
    with open(fname, 'w') as f:
        f.write(report)


def benchmark_dumps():
    callees = [
        ('builtin', json.dumps),
        ('orjson', lambda d: str(orjson.dumps(d), 'utf-8')),
        ('rapidjson(n)', partial(rapidjson.dumps, number_mode=rapidjson.NM_NATIVE)),
        ('rapidjson', rapidjson.dumps),
        ('hyperjson', hyperjson.dumps),
        ('ujson', ujson.dumps),
    ]
    data = chain(generate_fake_data(), load_data())
    result = benchmark(callees, data)
    report_benchmark(result, ROOT_PATH / f'json-dumps-{_fname_ts()}.txt')


def benchmark_loads():
    callees = [
        ('builtin', json.loads),
        ('orjson', orjson.loads),
        ('rapidjson(n)', partial(rapidjson.loads, number_mode=rapidjson.NM_NATIVE)),
        ('rapidjson', rapidjson.loads),
        ('hyperjson', hyperjson.loads),
        ('ujson', ujson.loads),
    ]
    data = chain(generate_fake_data(True), load_data(True))
    result = benchmark(callees, data)
    report_benchmark(result, ROOT_PATH / f'json-loads-{_fname_ts()}.txt')


def main():
    benchmark_dumps()
    benchmark_loads()


if __name__ == '__main__':
    main()
