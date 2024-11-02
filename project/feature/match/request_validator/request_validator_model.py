from pydantic import BaseModel

class MatchCreateModel(BaseModel):
    duration:int
    location:str

class MatchUpdateModel(BaseModel):
    duration:int