from dataclasses import dataclass
from datetime import datetime
import uuid
@dataclass
class MatchDataClass:
    id:uuid.UUID
    duration:int
    location:str
    date:datetime
@dataclass
class UpdateMatch:
    id:uuid.UUID
    duration:int