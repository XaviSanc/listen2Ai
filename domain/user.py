
from typing import Optional,List
from pydantic import BaseModel

from domain.playlist import Playlist

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    playlist: Optional[List[Playlist]] = None
