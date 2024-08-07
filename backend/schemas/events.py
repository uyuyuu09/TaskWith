from pydantic import BaseModel


# # About Display 
# class UpdateDisplay(BaseModel):
#     id: int 
#     next_num: int


# About tickets 

class Event(BaseModel):
    id: int
    event_name: str
    start_time: str
    end_time: str
    memo: str