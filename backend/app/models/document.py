from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    id: int
    user_id: int
    filename: str
    text: str
    training_id: Optional[int] = None
