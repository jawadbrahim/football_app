from pydantic import BaseModel
import uuid
class MatchModel(BaseModel):
    user_id:uuid.UUID
    number_of_player:int
    