from dataclasses import dataclass
import uuid
from datetime import datetime

@dataclass
class MatchDataClass:
    id:uuid.UUID
    user_id:uuid.UUID
    number_of_player:int
    created_at:datetime
