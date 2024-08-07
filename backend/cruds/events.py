from typing import Annotated

from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy import desc
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from schemas import events as schemas
from models import events as models


# # about Display 
# def update_display(db: Session, next_num: int):
#     display = db.query(models.Display).get(1)
#     if display is None:
#         display = models.Display(id=1, now_num=next_num)
#         db.add(display)
#         db.commit()
#         db.refresh(display)
        
#     display = db.query(models.Display).get(1)
#     display.now_num = next_num
#     db.add(display)
#     db.commit()
#     db.refresh(display)
    

# def get_current_number(db: Session):
#     display = db.query(models.Display).get(1)
#     return display.now_num


# # about tickets 
# # type of this user is models.User
# def create_ticket(db: Session, user):
#     last_tickets = db.query(models.Ticket.number).order_by(
#                                     desc(models.Ticket.number)).first()
#     next_number = 1
#     print(last_tickets)
#     if last_tickets is not None:
#         print(last_tickets)
#         next_number = last_tickets.number + 1

#     tickes = models.Ticket(
#         number=next_number,
#         user_id=user.id,
#     )
#     db.add(tickes)
#     db.commit()
#     db.refresh(tickes)
#     return tickes

def create_event(db:Session, user, event_name, start_time, end_time, memo):
    event = models.Event(
        event_name = event_name,
        start_time = start_time,
        end_time = end_time,
        memo = memo
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event