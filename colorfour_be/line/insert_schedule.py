'''import datetime
import os
from django.conf import settings
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageEvent,TextMessage, ImageCarouselColumn,ImageCarouselTemplate,MessageTemplateAction
from linebot.models import DatetimePickerTemplateAction,ConfirmTemplate,PostbackTemplateAction,PostbackEvent
#from line import google_calender
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))

def sendDate(event): #穿搭日程快速選日期
  try:
    message = TemplateSendMessage(
      alt_text='選取日期',
      template=ButtonsTemplate(        
        title='快速查詢穿搭日程安排',
        text='請選擇：',
        actions=[
          DatetimePickerTemplateAction(
            label="選取日期",
            data="action=date&mode=date",
            mode="date",
            initial="2024-11-02",
            min="2024-01-01",
            max="2024-12-31"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))
    
def sendBack_date(event, backdata): #回傳日期以及確認按鈕
    try:
        if backdata.get('mode') == 'date':
            dt = '日期為：' + event.postback.params.get('date')
        message = TextSendMessage(
            text = dt            
        )
        confirm_template = TemplateSendMessage(
            alt_text='確認穿搭日程安排',
            template = ConfirmTemplate(
                text = '目前尚未有穿搭日程安排，何不趁現在建立一個呢！',  #副標題
                actions=[
                    PostbackTemplateAction(
                        label='好呀',
                        data= 'action=yes',  
                        display_text='好呀'
                    ),
                    PostbackTemplateAction(
                        label='先不用',
                        data= 'action=no',
                        display_text='先不用'            
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, [message, confirm_template])
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))


def sendNo(event): #新增穿搭日程的確認按鈕(先不要)
    try:
        message = TextSendMessage(
            text = '好的，沒關係。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
        
        
def sendStartTime(event): #新增穿搭日程的確認按鈕(好呀)
  try:
    message = TemplateSendMessage(
      alt_text='選取日期時間',
      template=ButtonsTemplate(
        title='新增穿搭日程安排',
        text='請選擇：',
        actions=[
          DatetimePickerTemplateAction(
            label="選取開始日期時間",
            data="action=start_time",
            mode="datetime",
            initial="2024-11-03T10:00",
            min="2024-01-01T00:00",
            max="2024-12-31T23:59"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))

def sendEndTime(event):
  try:
    message = TemplateSendMessage(
      alt_text='選取結束日期時間',
      template=ButtonsTemplate(
        title='新增穿搭日程安排結束時間',
        text='請選擇：',
        actions=[
          DatetimePickerTemplateAction(
            label="選取結束日期時間",
            data="action=end_time",
            mode="datetime",
            initial="2024-11-03T12:00",
            min="2024-01-01T00:00",
            max="2024-12-31T23:59"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))
        
        
def requestLocation(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='請輸入目的地')
)
def requestDescription(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='請輸入日程名稱')
)'''
   
'''def handleUserInput(event, conversation_state):
  step = conversation_state['step']

  if isinstance(event, PostbackEvent) and hasattr(event.postback, 'params'):
    if step == 'start_time':
      conversation_state['data']['start_time'] = event.postback.params['datetime']
      conversation_state['step'] = 'end_time'
      sendEndTime(event)
    elif step == 'end_time':
      conversation_state['data']['end_time'] = event.postback.params['datetime']
      conversation_state['step'] = 'location'
      requestLocation(event)
  elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
    if step == 'location':
      conversation_state['data']['location'] = event.message.text
      conversation_state['step'] = 'description'
      requestDescription(event)
    elif step == 'description':
      conversation_state['data']['description'] = event.message.text
      conversation_state['step'] = 'choose_dress'
      choose_dress(event)
    elif step == 'choose_dress':
      conversation_state['data']['dress'] = event.message.text
      conversation_state['step'] = 'request'
      #End_schedule(event)
    elif step == 'request':
      conversation_state['step'] = None
      conversation_state['data'] = {}
      line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '建立成功！'))'''
      
'''def choose_dress(event): #選擇推薦的穿搭組合
  try:
    message = TemplateSendMessage(
      alt_text='穿搭組合',
      template=ImageCarouselTemplate(
        columns=[
          ImageCarouselColumn(
            image_url='https://imgur.com/OXVtzRw.png',
            action=MessageTemplateAction(
              label='期末報告服裝',  # 與穿搭名稱相同
              text='開始時間：2024-11-03 11:00\n結束時間：2024-11-03 12:00\n目的地：中原大學\n日程名稱：期末報告\n穿搭名稱：期末報告服裝'
            )
          ),
          ImageCarouselColumn(
            image_url='https://imgur.com/5UY0qLU.png',
            action=MessageTemplateAction(
              label='表演服',  # 與穿搭名稱相同
              text='開始時間：2024-11-03 11:00\n結束時間：2024-11-03 12:00\n目的地：中原大學\n日程名稱：期末成發\n穿搭名稱：表演服'
            )
          ),
          ImageCarouselColumn(
            image_url='https://imgur.com/7oIh9Ms.png',
            action=MessageTemplateAction(
              label='約會服裝',  # 與穿搭名稱相同
              text='開始時間：2024-11-09 11:00\n結束時間：2024-11-09 15:00\n目的地：漁光島\n日程名稱：海邊約會\n穿搭名稱：約會服裝'
            )
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))

def handleUserInput(event, conversation_state):
    step = conversation_state['step']

    if isinstance(event, PostbackEvent):
        data = event.postback.data.split('&')
        action = data[0].split('=')[1]

        if action == 'start_time':
            conversation_state['data']['start_time'] = event.postback.params['datetime']
            conversation_state['step'] = 'end_time'
            sendEndTime(event)
        elif action == 'end_time':
            conversation_state['data']['end_time'] = event.postback.params['datetime']
            conversation_state['step'] = 'location'
            requestLocation(event)
    elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        if step == 'location':
            conversation_state['data']['location'] = event.message.text
            conversation_state['step'] = 'description'
            requestDescription(event)
        elif step == 'description':
            conversation_state['data']['description'] = event.message.text
            conversation_state['step'] = 'choose_dress'
            choose_dress(event)
        elif step == 'choose_dress':
            # 處理用戶選擇的穿搭
            conversation_state['data']['dress'] = event.message.text
            #google_calender.calendar_event(event, conversation_state['data'])
            conversation_state['step'] = 'complete'
            conversation_state['data'] = {}
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='建立成功！'))

#conversation_state 初始值
conversation_state = {'step': 'start_time', 'data': {}}
event = MessageEvent(reply_token='dummy_token', message=TextMessage(text='dummy_text'))

# 寫入Google日曆
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
def get_google_credentials():
    """取得使用者的 Google OAuth 憑證"""
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def create_calendar_event(event_name, location, start_time, end_time, outfit_name):
    """建立 Google 日曆活動"""
    creds = get_google_credentials()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': event_name,
        'location': location,
        'description': f'穿搭名稱：{outfit_name}\n去LineBot看穿搭圖片: https://line.me/R/ti/p/40438shuqi',
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Taipei',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Taipei',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")'''

import datetime
import os
from django.conf import settings
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageEvent, TextMessage, ImageCarouselColumn, ImageCarouselTemplate, MessageTemplateAction, DatetimePickerTemplateAction, ConfirmTemplate, PostbackTemplateAction, PostbackEvent
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime

load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))

# Google Calendar API 的範圍
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_google_credentials():
    """取得使用者的 Google OAuth 憑證"""
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', scopes=SCOPES, redirect_uri='https://upward-gorgeous-bedbug.ngrok-free.app/oauth2callback')
    credentials = flow.run_local_server(port=8080) # 每登入一次google，須重跑一次server!!!
    return credentials
  
def convert_line_datetime_to_google_format(line_datetime):
  return datetime.strptime(line_datetime, '%Y-%m-%dT%H:%M').strftime('%Y-%m-%dT%H:%M:%S')

def create_calendar_event(event_data):
    """建立 Google 日曆活動，動態抓取使用者的輸入資料"""
    creds = get_google_credentials()
    service = build('calendar', 'v3', credentials=creds)
    start_time = convert_line_datetime_to_google_format(event_data['start_time'])
    end_time = convert_line_datetime_to_google_format(event_data['end_time'])

    event = {
        'summary': event_data['description'],  # 使用者輸入的日程名稱作為標題
        'location': event_data['location'],  # 使用者輸入的地點
        'description': (
            f"穿搭名稱：{event_data['dress']}\n"
            f"去LineBot看穿搭圖片: https://line.me/R/ti/p/40438shuqi"
        ),
        'start': {
            'dateTime': start_time,  # 使用者選擇的開始時間
            'timeZone': 'Asia/Taipei', 
        },
        'end': {
            'dateTime': end_time,  # 使用者選擇的結束時間
            'timeZone': 'Asia/Taipei', 
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 30},  # 提醒設置
            ],
        },
    }

    try:
        # 呼叫 Google Calendar API 建立活動
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")

        return event_result.get('htmlLink')  # 回傳活動的連結

    except Exception as e:
        print(f"無法建立活動: {e}")
        return None


def handleUserInput(event, conversation_state):
    """處理使用者輸入，並建立 Google 日曆活動"""
    step = conversation_state['step']

    if isinstance(event, PostbackEvent):
        data = event.postback.data.split('&')
        action = data[0].split('=')[1]

        if action == 'start_time':
            conversation_state['data']['start_time'] = event.postback.params['datetime']
            conversation_state['step'] = 'end_time'
            sendEndTime(event)
        elif action == 'end_time':
            conversation_state['data']['end_time'] = event.postback.params['datetime']
            conversation_state['step'] = 'location'
            requestLocation(event)

    elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        if step == 'location':
            conversation_state['data']['location'] = event.message.text
            conversation_state['step'] = 'description'
            requestDescription(event)
        elif step == 'description':
            conversation_state['data']['description'] = event.message.text
            conversation_state['step'] = 'choose_dress'
            choose_dress(event)
        elif step == 'choose_dress':
            conversation_state['data']['dress'] = event.message.text
            event_link = create_calendar_event(conversation_state['data'])
            conversation_state['step'] = 'complete'
            conversation_state['data'] = {}
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text=f'建立成功！查看活動：{event_link}')
            )
def sendStartTime(event): #新增穿搭日程的確認按鈕(好呀)->選開始時間
  try:
    message = TemplateSendMessage(
      alt_text='選取日期時間',
      template=ButtonsTemplate(
        title='新增穿搭日程安排開始時間',
        text='請選擇：',
        actions=[
          DatetimePickerTemplateAction(
            label="選取開始日期時間",
            data="action=start_time",
            mode="datetime",
            initial="2024-11-09T11:00",
            min="2024-01-01T00:00",
            max="2024-12-31T23:59"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))
def sendEndTime(event):
    """選擇結束時間"""
    try:
        message = TemplateSendMessage(
            alt_text='選取結束日期時間',
            template=ButtonsTemplate(
                title='新增穿搭日程安排結束時間',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label="選取結束日期時間",
                        data="action=end_time",
                        mode="datetime",
                        initial="2024-11-09T15:00",
                        min="2024-01-01T00:00",
                        max="2024-12-31T23:59"
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))

def requestLocation(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入目的地')
    )

def requestDescription(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入日程名稱')
    )

def choose_dress(event):
    """選擇推薦的穿搭組合"""
    try:
        message = TemplateSendMessage(
            alt_text='穿搭組合',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://imgur.com/OXVtzRw.png',
                        action=MessageTemplateAction(
                            label='期末報告服裝',
                            text='期末報告服裝'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://imgur.com/5UY0qLU.png',
                        action=MessageTemplateAction(
                            label='表演服',
                            text='表演服'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://imgur.com/7oIh9Ms.png',
                        action=MessageTemplateAction(
                            label='約會服裝',
                            text='約會服裝'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))

# conversation_state 初始值
conversation_state = {'step': 'start_time', 'data': {}}
event = MessageEvent(reply_token='dummy_token', message=TextMessage(text='dummy_text'))
