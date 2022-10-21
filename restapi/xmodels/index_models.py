from datetime import datetime

from pydantic import BaseModel


class Snippet(BaseModel):
    created: datetime
    title: str
    code: str
    linenos: int
    language: str
    style: bool
