from pydantic import BaseModel


class Snippet(BaseModel):
    title: str
    code: str
    linenos: int
    language: str
    style: bool
