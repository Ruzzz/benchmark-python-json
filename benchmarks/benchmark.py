import json
import statistics

from collections import defaultdict
from functools import partial
from itertools import chain
from pathlib import Path
from sys import getsizeof
from time import gmtime, strftime
from typing import Any, Generator, Iterable, List, NamedTuple, Tuple, Dict

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


class InData(NamedTuple):
    name: str  # name of data (data grouped benchmarks name)
    data: Any
    count_of_call: int


class ReportItem(AutoPropertiesDict):
    callee: str
    elapsed: float
    ratio: float


class SummaryItem(AutoPropertiesDict):
    callee: str
    mean: float
    median: float


Callee = Tuple[str, callable]  # name of researched object, as well as this object itself
Report = Dict[str, List[ReportItem]]  # name of data
Summary = List[SummaryItem]


def benchmark(callees: Iterable[Callee],
              dataset: Iterable[InData],
              verbose=True) -> Report:
    ret = {}
    for data_name, data, count_of_call in dataset:
        count_of_call = round(count_of_call * COUNT_FACTOR)
        if verbose:
            print(data_name, 'count of call:', count_of_call, 'size of data:', getsizeof(data))

        if count_of_call <= 0:
            continue
        group = []
        for callee_name, callee in callees:
            if verbose:
                print(' -', callee_name)

            with Elapsed() as elapsed:
                for _ in range(count_of_call):
                    callee(data)
            group.append(ReportItem(callee=callee_name, elapsed=elapsed()))

        group.sort(key=lambda x: x.elapsed)
        ret[data_name] = group

    if verbose:
        print()
    return ret


def generate_fake_data(as_string=False) -> Generator[InData, None, None]:
    json_generator = FakeJsonGenerator(JsonTypeWeights(string_weight=2, number_weight=2))
    values = [
        (512, 200000, '512b'),
        (5 * 1024, 20000, '5kb'),
        (1024 * 1024, 100, '1mb')
    ]
    for size, count, name in values:
        data = json_generator(size)
        if as_string:
            data = json.dumps(data)
        yield InData(name=f'fake-{name}.json', data=data, count_of_call=count)


def load_data(as_string=False) -> Generator[InData, None, None]:
    values = [
        ('data/apache.json', 5000),
        ('data/canada.json', 100),
        ('data/ctm.json', 800),
        ('data/github.json', 8000),
        ('data/instruments.json', 4000),
        ('data/mesh.json', 200),
        ('data/truenull.json', 10000),
        ('data/tweet.json', 100000),
        ('data/twitter.json', 1000)
    ]
    for fname, count in values:
        fname = ROOT_PATH / fname
        with open(fname) as f:
            data = f.read()
            if not as_string:
                data = json.loads(data)
        yield InData(name=fname.name, data=data, count_of_call=count)


def calc_summary(report: Report) -> Summary:
    ratios = defaultdict(list)
    for _, group in report.items():
        group.sort(key=lambda x: x.elapsed)
        first = group[0]
        for item in group:
            item.ratio = item.elapsed / first.elapsed
            ratios[item.callee].append(item.ratio)

    ret = []
    for callee, ratios in ratios.items():
        ret.append(SummaryItem(
            callee=callee,
            mean=statistics.mean(ratios),
            median=statistics.median(ratios)
        ))
    ret.sort(key=lambda x: x.median)
    return ret


def report_as_table(report: Report, summary: Summary, fname, title):
    content = f'## {title}\n\n'
    for data_name, group in report.items():
        content += f'### {data_name}\n\n'
        content += tabulate(group, headers='keys', tablefmt='pipe')
        content += '\n\n'

    content += '### Summary\n\n'
    content += tabulate(summary, headers='keys', tablefmt='pipe')
    content += '\n\n'

    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    with open(fname, 'w') as f:
        f.write(content)


def report_as_json(report: Report, summary: Summary, fname):
    content = {
        'report': report,
        'summary': summary,
    }
    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    with open(fname, 'w') as f:
        f.write(json.dumps(content))


def benchmark_dumps():
    callees = [
        ('builtin', json.dumps),
        ('orjson', lambda d: str(orjson.dumps(d), 'utf-8')),
        ('rapidjson(n)', partial(rapidjson.dumps, number_mode=rapidjson.NM_NATIVE)),
        ('rapidjson', rapidjson.dumps),
        ('hyperjson', hyperjson.dumps),
        ('ujson', ujson.dumps),
    ]
    dataset = chain(generate_fake_data(), load_data())
    report = benchmark(callees, dataset)
    summary = calc_summary(report)
    now = strftime('%Y-%m-%d', gmtime())
    report_as_table(report, summary, ROOT_PATH / f'reports/json-dumps-{now}.md', 'JSON dumps')
    report_as_json(report, summary, ROOT_PATH / f'reports/json-dumps-{now}.json')


def benchmark_loads():
    callees = [
        ('builtin', json.loads),
        ('orjson', orjson.loads),
        ('rapidjson(n)', partial(rapidjson.loads, number_mode=rapidjson.NM_NATIVE)),
        ('rapidjson', rapidjson.loads),
        ('hyperjson', hyperjson.loads),
        ('ujson', ujson.loads),
    ]
    dataset = chain(generate_fake_data(True), load_data(True))
    report = benchmark(callees, dataset)
    summary = calc_summary(report)
    now = strftime('%Y-%m-%d', gmtime())
    report_as_table(report, summary, ROOT_PATH / f'reports/json-loads-{now}.md', 'JSON loads')
    report_as_json(report, summary, ROOT_PATH / f'reports/json-loads-{now}.json')


def main():
    benchmark_dumps()
    benchmark_loads()


if __name__ == '__main__':
    main()
