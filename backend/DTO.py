from pydantic import BaseModel, Field
from typing import List

from datetime import datetime

# HTTP Bodies

class TravelProject(BaseModel):
    name: str
    description: str | None

    start_date: datetime | None
    
    note: str = Field(default="")
    places: List[str]

class PlaceNote(BaseModel):
    place_id: str
    note: str

class Auth(BaseModel):
    username: str
    password: str
