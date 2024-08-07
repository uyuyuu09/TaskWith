from datetime import datetime, timezone
from typing import Annotated

from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

import database
from schemas import users as schemas
from models import users as models

load_dotenv()

# to hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# SECRET
SECRET_KEY = os.getenv('SECRET_KEY')
# jwt algorithm
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

# hash raw password
def create_password_hash(user_password: str):
    return pwd_context.hash(user_password)


# Is input password correct?
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# gen token
def create_access_token(email:str, user_id: int, expires_delta: timedelta = timedelta(minutes=1)):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# make an user
def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(
        # name=user.name,
        email=user.email,
        password=user.password
    )
    # to hashnize
    db_user.password = create_password_hash(db_user.password)
    # add to db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # return user infomation
    return db_user


def get_user_by_email(db: Session, email:str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return False

    return user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get('sub')
        user_id: int = payload.get('id')
        if email is None or user_id is None:
            raise HTTPException(status_code=400, detail='Could not validate user')
        
        db = database.db_session()
        user = get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=400, detail='Could not validate user')
        
    except:
        raise HTTPException(status_code=400, detail='Could not validate user')
    
    #return {'email':email, 'user_id': user_id}
    return user
