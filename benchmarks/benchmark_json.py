import json

from functools import partial
from itertools import chain
from pathlib import Path
from time import gmtime, strftime
from typing import Generator

import hyperjson  # https://github.com/mre/hyperjson
import orjson  # https://github.com/ijl/orjson
import rapidjson  # https://github.com/python-rapidjson/python-rapidjson
import ujson  # https://github.com/ultrajson/ultrajson

from .helpers.fake_json import FakeJsonGenerator, JsonTypeWeights
from .rzbenchmark import benchmark, report_as_md_table, Callee, InData, Report, Summary

COUNT_FACTOR = 1
ROOT_PATH = Path(__file__).resolve().parents[1]


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


def save_as_md_table(fname, title: str, report: Report, summary: Summary = None):
    content = report_as_md_table(title, report, summary)

    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    with open(str(fname) + '.md', 'w') as f:
        f.write(content)


def save_as_json(fname, report: Report, summary: Summary = None):
    content = {'report': report}
    if summary:
        content['summary'] = summary

    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    with open(str(fname) + '.json', 'w') as f:
        f.write(json.dumps(content))


def benchmark_dumps():
    op_title = 'dumps'
    callees = [
        Callee('builtin', json.dumps),
        Callee('orjson', lambda d: str(orjson.dumps(d), 'utf-8')),
        Callee('rapidjson(n)', partial(rapidjson.dumps, number_mode=rapidjson.NM_NATIVE)),
        Callee('rapidjson', rapidjson.dumps),
        Callee('hyperjson', hyperjson.dumps),
        Callee('ujson', ujson.dumps),
    ]
    dataset = chain(generate_fake_data(), load_data())
    report, summary = benchmark(callees, dataset, COUNT_FACTOR)

    now = strftime('%Y-%m-%d', gmtime())
    fname = ROOT_PATH / f'reports/json-{op_title}-{now}'
    save_as_md_table(fname, f'JSON {op_title}', report, summary)
    save_as_json(fname, report, summary)


def benchmark_loads():
    op_title = 'loads'
    callees = [
        Callee('builtin', json.loads),
        Callee('orjson', orjson.loads),
        Callee('rapidjson(n)', partial(rapidjson.loads, number_mode=rapidjson.NM_NATIVE)),
        Callee('rapidjson', rapidjson.loads),
        Callee('hyperjson', hyperjson.loads),
        Callee('ujson', ujson.loads),
    ]
    dataset = chain(generate_fake_data(True), load_data(True))
    report, summary = benchmark(callees, dataset, COUNT_FACTOR)

    now = strftime('%Y-%m-%d', gmtime())
    fname = ROOT_PATH / f'reports/json-{op_title}-{now}'
    save_as_md_table(fname, f'JSON {op_title}', report, summary)
    save_as_json(fname, report, summary)


def main():
    benchmark_dumps()
    benchmark_loads()


if __name__ == '__main__':
    main()
