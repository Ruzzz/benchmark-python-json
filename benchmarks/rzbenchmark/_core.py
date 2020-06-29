import statistics
from collections import defaultdict
from sys import getsizeof
from timeit import default_timer
from typing import Any, Iterable, Optional, Tuple, Union

from ._defs import (
    AnyCallee,
    AnyInData,
    ByDataReport,
    CallableAny,
    Report,
    ReportItem,
    Summary,
    SummaryItem,
)


class Estimator:

    def __call__(self, callee: CallableAny, data: Any, count_of_call: int) -> float:
        with Estimator.Elapsed() as elapsed:
            for _ in range(count_of_call):
                callee(data)
        return elapsed()

    class Elapsed:
        __slots__ = '_start', 'dx'

        FLOAT_FMT = '.3f'

        def __init__(self):
            self._start = 0
            self.dx = 0

        def __enter__(self):
            self._start = default_timer()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.dx = default_timer() - self._start

        def __call__(self, fmt=None) -> Union[float, str]:
            return self.dx if fmt is None else format(self.dx, fmt)


class ByDataSummary:

    def __init__(self):
        self.by_data_ratios = defaultdict(list)

    def __call__(self, by_data_report: ByDataReport):
        for x in by_data_report:
            self.by_data_ratios[x.callee_name].append(x.ratio)

    def calc_summary(self) -> Summary:
        ret = []
        for callee_name, ratios in self.by_data_ratios.items():
            ret.append(SummaryItem(
                callee_name=callee_name,
                mean=statistics.mean(ratios),
                median=statistics.median(ratios)
            ))
        ret.sort(key=lambda x: x.median)
        return ret


def benchmark(callees: Iterable[AnyCallee],
              dataset: Iterable[AnyInData],
              count_factor=1.0,
              estimator=None,
              summary=None,
              verbose=True) -> Tuple[Report, Optional[Any]]:
    """
    :param callees:
    :param dataset:
    :param count_factor:
    :param estimator: Default is Estimator()
    :param summary: None, False or summary object, default is ByDataSummary()
    :param verbose:
    :return:
    """

    # pylint: disable=too-many-arguments, too-many-locals
    if estimator is None:
        estimator = Estimator()
    if summary is None:
        summary = ByDataSummary()
    ret = {}

    for data_name, data, count_of_call in dataset:
        count_of_call = round(count_of_call * count_factor)
        if verbose:
            print(data_name, 'count of call:', count_of_call, 'size of data:', getsizeof(data))

        if count_of_call <= 0:
            continue
        group = []
        for callee_name, callee in callees:
            if verbose:
                print(' -', callee_name)

            elapsed = estimator(callee, data, count_of_call)
            group.append(ReportItem(callee_name=callee_name, elapsed=elapsed))

        group.sort(key=lambda x: x.elapsed)
        first = group[0]
        for item in group:
            item.ratio = item.elapsed / first.elapsed

        if summary:
            summary(group)
        ret[data_name] = group

    if verbose:
        print()

    return ret, summary.calc_summary() if summary else None
