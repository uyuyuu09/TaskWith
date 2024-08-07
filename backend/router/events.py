from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

import database
from schemas import events as schemas
from models import events as models
from cruds import events as crud

from cruds.users import get_current_user
from models.users import User


models.Base.metadata.create_all(bind=database.engine)  

router = APIRouter(
    prefix="/events",
    tags=["events"],
    dependencies=[Depends(database.db_session)],
    responses={404: {"description": "Not found"}},
)

# # about display
# @router.put("/display_update")
# async def update_display(req: schemas.UpdateDisplay, db: Session = Depends(database.db_session)):
#     #try:
#     crud.update_display(db, req.next_num)
#     #except:
#     #    raise HTTPException(status_code=400, detail="Fail to update tickets number")

#     return {'status': "OK"}


# @router.get("/display_current_number")
# async def get_current_number(db: Session = Depends(database.db_session)):
#     try:
#         current_number =  crud.get_current_number(db)

#     except:
#         raise HTTPException(status_code=400, detail="Fail to get display number")

#     return {"status": "OK", "current_number": current_number}

# # about tickets
# @router.post("/create_ticket")
# async def create_ticket(db: Session = Depends(database.db_session), 
#                         user: User = Depends(get_current_user)):
#     #try:
#     ticket = crud.create_ticket(db, user)

#     #except:
#         #raise HTTPException(status_code=400, detail="Fail to create tickets")

#     return {"status": "OK", "ticket": ticket}

@router.post("/create_event")
async def create_event(req: schemas.Event,
                       db: Session = Depends(database.db_session),
                       user: User = Depends(get_current_user)):
    event = crud.create_event(db, user, req.event_name, req.start_time, req.end_time, req.memo)
    return event