from typing import Optional,List
from enum import Enum
from pydantic import BaseModel

class VerbosityEnum(str, Enum):
    CONCISE = "CONCISE"
    IN_DEPTH = "IN-DEPTH"
    ROUND_TABLE = "ROUND TABLE"

class PoliticalEnum(str, Enum):
    LIBERAL = "LIBERAL"
    NEUTRAL = "NEUTRAL"
    CONSERVATIVE = "CONSERVATIVE"


class News(BaseModel):
    name: str
    author: str
    verbosity: VerbosityEnum
    languages: List[str]
    political_orientation: PoliticalEnum