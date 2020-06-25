from timeit import default_timer
from typing import Union


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
