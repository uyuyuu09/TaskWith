import os
from typing import Annotated
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.get.get_calendar_id import get_all_calendar
from router import user

app = FastAPI()

#access rules

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.0.41:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)

@app.get("/")
async def root():
    return {'status':'ok'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
