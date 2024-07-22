from fastapi import Depends, HTTPException, status, Request
from fastapi import APIRouter
from api.get.get_calendar_id import get_all_calendar
from api.get.calendar_from_id import getCalendar
from fastapi import Depends, HTTPException, status
import json


router = router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.get("/id")
async def get_calendar_id():
    """
    - get all calendar from your Google account.
    """
    data = get_all_calendar()
    # カレンダー名だけ取得する場合は以下のようにする
    # calendar_names = [item["カレンダー名"] for item in data]
    # return {"data": calendar_names}
    return {"data": data}


@router.post("/calendar")
async def get_calendar_content(request: Request):
    """
    - get calendar content.
    """
    try:
        body = await request.json()  # リクエストのボディを JSON として取得
    except:
        body = {}
    id = body.get("id")  # id を取得
    if not id:
        raise HTTPException(
            status_code=400, detail="IDが指定されていません"
        )
    data = getCalendar(id)
    return {"data": data}
