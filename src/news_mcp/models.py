from dataclasses import dataclass
from pydantic import BaseModel


class ResponseModel(BaseModel):
    title: str
    link: str
    date: str
    description: str
    content: str


@dataclass
class RequestTags:
    title: str = "title"
    link: str = "link"
    pubDate: str = "pubDate"
    description: str = "description"
