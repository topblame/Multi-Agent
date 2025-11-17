from pydantic import BaseModel

class CreateBoardRequest(BaseModel):
    userid: str
    title: str
    content: str