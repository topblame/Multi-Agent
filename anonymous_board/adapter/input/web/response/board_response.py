from pydantic import BaseModel
from datetime import datetime

class BoardResponse(BaseModel):
    id: int
    userid: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime