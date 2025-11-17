from datetime import datetime

import datetime
from typing import Optional


class Board:
    def __init__(self, title:str, content: str, userid: str):
        self.userid = userid
        self.id: Optional[int] = None
        self.title = title
        self.content = content

        self.created_at: datetime = datetime.utcnow()
        self.updated_at: datetime = datetime.utcnow()

    def update(self, title: str, content: str, userid: str):
        self.userid = userid
        self.title = title
        self.content = content
        self.updated_at = datetime.utcnow()