from pydantic import BaseModel

class Training(BaseModel):
    id: int
    title: str
    description: str
