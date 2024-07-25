from pydantic import BaseModel


# user login
class UserLogin(BaseModel):
    email: str
    password: str

# make an user
class CreateUser(BaseModel):
    # name: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str 
