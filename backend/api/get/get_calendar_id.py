import datetime
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from fastapi import Depends, HTTPException, status


def get_all_calendar():
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

    all_calendar = []
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar in calendar_list['items']:
            calendar_data = {
                "id": calendar["id"],
                "カレンダー名": calendar["summary"]
            }
            all_calendar.append(calendar_data)
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break

    return all_calendar
