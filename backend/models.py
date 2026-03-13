from sqlalchemy import Column, Integer, String, Date
from database import Base

class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(Date)
    category = Column(String)
    image = Column(String)   # image column