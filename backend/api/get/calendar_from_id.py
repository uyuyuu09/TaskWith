import datetime
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from fastapi import Depends, HTTPException, status


def getCalendar(id: str):
    GET_SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    # 以下2つのjsonファイルはbackend/直下
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', GET_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_oauth.json', GET_SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    today = datetime.datetime.utcnow()
    next_week = today + datetime.timedelta(days=7)

    # 日時を ISO 8601 形式に変換
    timeMin = today.isoformat() + 'Z'
    timeMax = next_week.isoformat() + 'Z'

    CALENDAR_ID = id
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=timeMin,
        timeMax=timeMax,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    content = []
    if not events:
        print('表示する内容がありません。')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        content.append({"開始時間": start, "イベント名": event['summary']})
    return content
