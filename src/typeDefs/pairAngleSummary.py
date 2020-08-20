from typing import TypedDict
import datetime as dt


class IPairAngleSummary(TypedDict):
    pairName: str
    dataDate: dt.datetime
    angularLim: float
    violPerc: float
    maxDeg: float
    minDeg: float
    dataType: str
