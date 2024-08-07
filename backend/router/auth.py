from fastapi import APIRouter, HTTPException, status, Query, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv, dotenv_values
import json
import os
import uuid

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

load_dotenv()

