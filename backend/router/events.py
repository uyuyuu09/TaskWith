from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

import database
from schemas import tickets as schemas
from models import tickets as models
from cruds import tickets as crud

from cruds.users import get_current_user
from models.users import User

models.Base.metadata.create_all(bind=database.engine)  

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
    dependencies=[Depends(database.db_session)],
    responses={404: {"description": "Not found"}},
)

# about display
@router.put("/display_update")
async def update_display(req: schemas.UpdateDisplay, db: Session = Depends(database.db_session)):
    #try:
    crud.update_display(db, req.next_num)
    #except:
    #    raise HTTPException(status_code=400, detail="Fail to update tickets number")

    return {'status': "OK"}


@router.get("/display_current_number")
async def get_current_number(db: Session = Depends(database.db_session)):
    try:
        current_number =  crud.get_current_number(db)

    except:
        raise HTTPException(status_code=400, detail="Fail to get display number")

    return {"status": "OK", "current_number": current_number}

# about tickets
@router.post("/create_ticket")
async def create_ticket(db: Session = Depends(database.db_session), 
                        user: User = Depends(get_current_user)):
    #try:
    ticket = crud.create_ticket(db, user)

    #except:
        #raise HTTPException(status_code=400, detail="Fail to create tickets")

    return {"status": "OK", "ticket": ticket}
