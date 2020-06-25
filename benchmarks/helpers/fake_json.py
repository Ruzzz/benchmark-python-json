import itertools
import random
import string
import sys

from bisect import bisect
from enum import auto, IntEnum
from typing import NamedTuple, Iterable, Tuple


def _chance(value):
    return random.random() <= value


class _UnicodeStringGenerator:
    CYRILLIC_RANGE = (0x0400, 0x04FF)

    def __init__(self,
                 unicode_ranges: Iterable[Tuple[int, int]] = None,
                 use_ascii_letters=True):
        if not unicode_ranges:
            unicode_ranges = [self.CYRILLIC_RANGE]
        self.alphabet = [
            chr(code_point)
            for x in unicode_ranges
            for code_point in range(x[0], x[1] + 1)
        ]
        if use_ascii_letters:
            self.alphabet.extend(string.ascii_letters)
        self.alphabet.append(' ')

    def __call__(self, length: int):
        return ''.join(random.choice(self.alphabet) for _ in range(length))


class _JsonTypeKind(IntEnum):
    String = 0
    Number = auto()
    Boolean = auto()
    Null = auto()
    Object = auto()
    Array = auto()


class JsonTypeWeights(NamedTuple):
    string_weight: int = 1
    number_weight: int = 1
    boolean_weight: int = 1
    null_weight: int = 1
    object_weight: int = 1
    array_weight: int = 1


class FakeJsonGenerator:

    def __init__(self, json_type_weights: JsonTypeWeights = None):
        self._cum_type_weights = list(itertools.accumulate(json_type_weights or JsonTypeWeights()))
        self._string_generator = _UnicodeStringGenerator()

    def __call__(self, approximate_size: int):

        def add_elemenet_(parent_, k_, v_):
            if isinstance(parent_, dict):
                parent_[k_] = v_
            elif isinstance(parent_, list):
                parent_.append(v_)
            else:
                raise ValueError('dict or list')

        if approximate_size < 1:
            approximate_size = 1
        ret = dict()
        current_size = 0
        parents = [ret]
        while current_size < approximate_size:
            if len(parents) > 1 and _chance(0.3):
                parents.pop()

            length = random.randint(5, 10)
            indent = self.random_indent(length)
            current_size += length

            parent = parents[-1]

            type_kind = self.choices(self._cum_type_weights)
            if type_kind == _JsonTypeKind.String:
                length = random.randint(5, 100)
                value = self._string_generator(length)
                add_elemenet_(parent, indent, value)
                current_size += length

            elif type_kind == _JsonTypeKind.Number:
                value = self.random_number()
                add_elemenet_(parent, indent, value)
                current_size += 4

            elif type_kind == _JsonTypeKind.Null:
                add_elemenet_(parent, indent, None)
                current_size += 1

            elif type_kind == _JsonTypeKind.Boolean:
                value = _chance(0.5)
                add_elemenet_(parent, indent, value)
                current_size += 1

            elif type_kind == _JsonTypeKind.Object:
                nested = dict()
                add_elemenet_(parent, indent, nested)
                parents.append(nested)

            elif type_kind == _JsonTypeKind.Array:
                nested = list()
                add_elemenet_(parent, indent, nested)
                parents.append(nested)

        return ret

    @staticmethod
    def random_indent(length: int) -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    @staticmethod
    def random_number():
        if _chance(0.5):
            return random.random() * sys.maxsize
        return random.randint(0, sys.maxsize)

    @staticmethod
    def choices(cum_weights):
        return bisect(cum_weights, random.random() * cum_weights[-1], 0, len(cum_weights) - 1)
