from pydantic import BaseModel

class RagAccess(BaseModel):
    user_id: int
    training_id: int
