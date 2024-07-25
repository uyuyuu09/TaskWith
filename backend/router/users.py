from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

import database
from schemas import users as schemas
from models import users as models
from cruds import users as crud


models.Base.metadata.create_all(bind=database.engine)  

router = router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(database.db_session)],
    responses={404: {"description": "Not found"}},
)

@router.post('/create')
async def create_user(req:schemas.CreateUser, 
                        db: Session = Depends(database.db_session)):
    """
    create new user by email, password, name
    """
    #make new user
    if not req:
        raise HTTPException(status_code=400, detail="user request is null")
    #try:
    create_user_model = crud.create_user(db, req)
    #except:
        #raise HTTPException(status_code=400, detail="failed to make new user")

    return create_user_model


@router.post('/token')
async def login_for_access_token(req: schemas.UserLogin, db: Session = Depends(database.db_session)):
    """
    - get access token by logining(email and password)
    - in default, token is expired within 10000000000000 minutes
    """
    user = crud.authenticate_user(db, req.email, req.password,)
    
    if not user:
        raise HTTPException(status_code=400, detail='Could not validate user')
    
    token = crud.create_access_token(user.email, user.id)


    return {'access_token': token, 'token_type':'bearer'}



@router.get('/me')
async def user_info(current_user: models.User = Depends(crud.get_current_user)):
    return current_user
