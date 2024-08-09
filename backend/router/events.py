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


@router.post("/create_event")
async def create_event(req: schemas.Event,
                       db: Session = Depends(database.db_session),
                       user: User = Depends(get_current_user)):
    event = crud.create_event(db, user, req)
    return event