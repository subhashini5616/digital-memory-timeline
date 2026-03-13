from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    title: str
    description: str
    date: date
    category: str
    image: str | None = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True