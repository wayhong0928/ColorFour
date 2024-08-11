import datetime
import os
from dotenv import load_dotenv
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageEvent,TextMessage, ImageCarouselColumn,ImageCarouselTemplate,MessageTemplateAction,ImageSendMessage
from linebot.models import DatetimePickerTemplateAction,ConfirmTemplate,PostbackTemplateAction,PostbackEvent


load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))
def search_Date(event): #穿搭日程快速選日期
  try:
    message = TemplateSendMessage(
      alt_text='選取日期',
      template=ButtonsTemplate(        
        title='快速查詢穿搭日程安排',
        text='請選擇：',
        actions=[
          DatetimePickerTemplateAction(
            label="選取日期",
            data="action=search_date&mode=date",
            mode="date",
            initial="2024-06-21",
            min="2024-01-01",
            max="2024-12-31"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))
    
def Back_search_date(event, backdata): #回傳日期以及確認按鈕
    try:
        if backdata.get('mode') == 'date':
            dt = '日期為：' + event.postback.params.get('date')
        message = [
          TextSendMessage(
            text = dt            
          ),
          ImageSendMessage( #SE報告照片
              original_content_url = "https://imgur.com/OXVtzRw.png", 
              preview_image_url = "https://imgur.com/OXVtzRw.png"
          ),
          TextSendMessage(
            text = "日程名稱：SE期末報告\n開始時間：2024-06-21 10:00\n結束時間：2024-06-21 12:00\n地點：中原大學\n活動：SE期末報告\n穿搭名稱：期末報告服裝"            
          ),
          TemplateSendMessage(
            alt_text='確認是否要新增穿搭日程安排',
            template = ConfirmTemplate(
              text = '要不要新增其他穿搭日程呢~',  #副標題
              actions=[
                PostbackTemplateAction(
                    label='好呀',
                    data= 'action=yes',  
                    display_text='好呀'
                ),
                PostbackTemplateAction(
                    label='先不用',
                    data= 'action=no_insert',
                    display_text='先不用'            
                )
              ]
            )
          )
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
        

def insert_no(event): #日程安排的確認按鈕(先不要)
    try:
        message = TextSendMessage(
            text = '好的，沒關係。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
        
'''        
def sendStartTime(event):
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
            initial="2024-06-21T10:00",
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
            initial="2024-06-21T12:00",
            min="2024-01-01T00:00",
            max="2024-12-31T23:59"
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{e}'))
        
def sendBack_datetime(event, backdata): #回傳日期時間
    try:
        if backdata.get('mode') == 'datetime':
            dt = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M') #讀取日期時間
            dt = dt.strftime('{d}%Y-%m-%d\n{t}%H:%M').format(d='日期為:', t='時間為:') #轉為字串
        message = TextSendMessage(
            text = dt            
        )
        line_bot_api.reply_message(event.reply_token, message)

    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
        
def requestLocation(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='請輸入地點')
)
def requestDescription(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='請輸入活動')
)
def choose_dress(event): #推薦的穿搭組合
  try:
      message = [
        TextSendMessage(
          text = '請選擇日程穿搭'
        ),
        TemplateSendMessage(
          alt_text='穿搭組合',
          template = ImageCarouselTemplate(
            columns=[
              ImageCarouselColumn(
                  image_url = 'https://imgur.com/OXVtzRw.png',
                  action = MessageTemplateAction(
                    label='期末報告服裝', #與穿搭名稱相同
                    text='日程名稱：SE期末報告\n開始時間：2024-06-21 10:00\n結束時間：2024-06-21 12:00\n地點：中原大學\n活動：SE期末報告\n穿搭名稱：期末報告服裝'                        
                  )
              ),
              ImageCarouselColumn(
                  image_url = 'https://imgur.com/5UY0qLU.png',
                  action = MessageTemplateAction(
                    label='表演服', #與穿搭名稱相同
                    text='日程名稱：期末成發\n開始時間：2024-06-21 10:00\n結束時間：2024-06-21 10:00\n地點：中原大學\n活動：期末成發\n穿搭名稱：表演服'                       
                  )
              )              
            ]
          )
        ),
        TextSendMessage(
          text = '建立成功！'
        )
      ]
      line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
def choose_dress(event): #推薦的穿搭組合
  try:
      message = [
        TextSendMessage(
          text = '請選擇日程穿搭'
        ),
        TemplateSendMessage(
          alt_text='穿搭組合',
          template = ImageCarouselTemplate(
            columns=[
              ImageCarouselColumn(
                  image_url = 'https://imgur.com/OXVtzRw.png',
                  action = PostbackTemplateAction(
                        label='期末報告服裝', #與穿搭名稱相同
                        display_text='期末報告服裝',
                        data= 'action=project'                        
                    )
              ),
              ImageCarouselColumn(
                  image_url = 'https://imgur.com/5UY0qLU.png',
                  action = PostbackTemplateAction(
                        label='表演服', #與穿搭名稱相同
                        display_text='表演服',
                        data= 'action=showtime'                        
                    )
              )              
            ]
          )
        )
      ]
      line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def End_schedule(event):
  message = TextSendMessage(text = '日程名稱：SE期末報告\n開始時間：2024-06-21 10:00\n結束時間：2024-06-21 12:00\n地點：中原大學\n活動：SE期末報告\n穿搭名稱：期末報告服裝')
  line_bot_api.reply_message(event.reply_token, message)

def show(event):
  message = TextSendMessage(text = '日程名稱：期末成發\n開始時間：2024-06-21 10:00\n結束時間：2024-06-21 10:00\n地點：中原大學\n活動：期末成發\n穿搭名稱：表演服')
  line_bot_api.reply_message(event.reply_token, message)
     
def handleUserInput(event, conversation_state):
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
      line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '建立成功！'))
      
'''