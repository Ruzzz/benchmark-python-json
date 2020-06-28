from typing import NamedTuple, Any, List, Dict

from ._helpers import AutoPropertiesDict


class Callee(NamedTuple):
    callee_name: str
    callee: callable


class InData(NamedTuple):
    name: str  # name of data ('data grouped' benchmark name)
    data: Any
    count_of_call: int


class ReportItem(AutoPropertiesDict):
    callee_name: str
    elapsed: float
    ratio: float


class SummaryItem(AutoPropertiesDict):
    callee_name: str
    mean: float
    median: float


ByDataReport = List[ReportItem]
Report = Dict[str, ByDataReport]  # [name of data] = ByDataReport
Summary = List[SummaryItem]
