from typing import Optional,List
from pydantic import BaseModel

from domain.new import News

class Playlist(BaseModel):
    name: str
    likes: Optional[int] = 0
    news_list: Optional[List[News]] = None