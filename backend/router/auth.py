from fastapi import APIRouter, HTTPException, status, Query, Request
from fastapi.responses import RedirectResponse
from api.get.get_calendar_id import get_all_calendar
from api.get.calendar_from_id import getCalendar
from dotenv import load_dotenv, dotenv_values
import json
import os
import uuid
import requests

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

load_dotenv()

