from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

from utils.date import get_current_date

# #Display model
# class Display(Base):
#     __tablename__ = "display"
#     id = Column(Integer, primary_key=True)
#     now_num = Column(Integer)

# #tickes(整理券)
# class Ticket(Base):
#     __tablename__ = "tickets"
#     id = Column(Integer, primary_key=True)
#     number = Column(Integer, unique=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     created_at = Column(DateTime, default=get_current_date())

#     # user = relationship("User", back_populates="tickets")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    event_name = Column(String, unique=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    memo = Column(String(100))
    created_time = Column(DateTime, default=get_current_date())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="events")
