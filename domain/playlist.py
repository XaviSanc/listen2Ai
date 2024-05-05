from typing import Optional,List
from pydantic import BaseModel

class Playlist(BaseModel):
    name: str
    likes: int
    news_list: Optional[List[New]] = None