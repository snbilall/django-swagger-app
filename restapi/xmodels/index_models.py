from datetime import datetime
from decimal import Decimal
from typing import NamedTuple


class Snippet(NamedTuple):
    created: datetime
    title: str
    code: str
    linenos: int
    language: str
    style: bool
