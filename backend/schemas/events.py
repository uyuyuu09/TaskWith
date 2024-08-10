from pydantic import BaseModel
import datetime


# # About Display 
# class UpdateDisplay(BaseModel):
#     id: int 
#     next_num: int


# About tickets 

class Event(BaseModel):
    event_name: str
    start_time: datetime
    end_time: datetime
    memo: str
    class Config:
        arbitrary_types_allowed = True