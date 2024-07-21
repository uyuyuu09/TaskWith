from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

GET_SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_calender():
    creds = None
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

    # 現在の日時を取得
    today = datetime.datetime.utcnow()

    # 一週間後の日時を計算
    next_week = today + datetime.timedelta(days=7)

    # 日時を ISO 8601 形式に変換
    timeMin = today.isoformat() + 'Z'
    timeMax = next_week.isoformat() + 'Z'

    CALENDAR_ID = "c_7d7179e8a57398a79e70d4d38f64c9bd71704e01af3c45bb048e6bd58ab3cd63@group.calendar.google.com"

    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=timeMin, timeMax=timeMax,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == "__main__":
    get_calender()