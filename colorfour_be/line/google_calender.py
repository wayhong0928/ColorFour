from flask import Flask, redirect, url_for, session, request
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from datetime import datetime
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage
import os
import json

app = Flask(__name__)
app.secret_key = 'https://policies.google.com/terms?hl=zh-TW'

# 設定 OAuth 2.0 憑證
CLIENT_SECRETS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Step 1: 跳轉到 Google 授權頁面
@app.route('/authorize')
def authorize():
  # 創建 OAuth 授權流程
  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
  
  flow.redirect_uri = url_for('oauth2callback', _external=True)
  
  # 跳轉到 Google 的 OAuth 2.0 授權頁面
  authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
  
  session['state'] = state
  return redirect(authorization_url)

# Step 2: OAuth 回調，處理 Google 返回的授權碼
@app.route('/oauth2callback')
def oauth2callback():
  state = session['state']
  
  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
  flow.redirect_uri = url_for('oauth2callback', _external=True)

  # 用授權碼取得 token
  authorization_response = request.url
  flow.fetch_token(authorization_response=authorization_response)

  # 將 token 存到 session，或存到你的資料庫
  credentials = flow.credentials
  session['credentials'] = credentials_to_dict(credentials)
  
  # 儲存 token 到 json 或資料庫
  save_token_to_database(session['credentials'])
  
  return redirect(url_for('calendar_event'))

def convert_line_datetime_to_google_format(line_datetime):
  return datetime.strptime(line_datetime, '%Y-%m-%dT%H:%M').strftime('%Y-%m-%dT%H:%M:%S')

# Step 3: 用 token 建立 Google 行事曆事件
@app.route('/calendar_event')
def calendar_event(event, data):
  # 取得使用者的 token
  credentials = google.oauth2.credentials.Credentials(**session['credentials'])
  service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

  start_time = convert_line_datetime_to_google_format(data['start_time'])
  end_time = convert_line_datetime_to_google_format(data['end_time'])
  
  # 建立 Google 行事曆事件
  event = {
    'summary': 'User Calendar Event',
    'description': data['description'],
    'location': data['location'],
    'start': {
      'dateTime': start_time,
      'timeZone': 'Asia/Taipei',
    },
    'end': {
      'dateTime': end_time,
      'timeZone': 'Asia/Taipei',
    },
    'reminders': {
      'useDefault': True,
    },
    
  }

  event_result = service.events().insert(calendarId='primary', body=event).execute()
  line_bot_api.reply_message(event.reply_token, TextSendMessage(text='建立成功！')) # type: ignore
  
  return f"Event created: {event_result.get('htmlLink')}"


# Helper function: 將 token 轉換為 dict 格式
def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

# Helper function: 將 token 儲存到資料庫
def save_token_to_database(token_dict):
    with open('token.json', 'w') as token_file:
        json.dump(token_dict, token_file)

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)