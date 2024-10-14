import os
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, ImageMessage, PostbackEvent
from urllib.parse import parse_qsl
from line import purchase, social, search_schedule, weatherApi
# from line import insert_schedule, purchase, social, search_schedule, weatherApi

line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))

# 用於追踪用戶的對話狀態
conversation_state = {'step': None, 'data': {}}

@csrf_exempt
def callback(request):
  if request.method == 'POST':
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    
    try:
      events = parser.parse(body, signature)
      
      # 確認事件是可疊代的列表
      if not isinstance(events, list):
        return HttpResponseBadRequest("Webhook payload is not iterable")
    
    except InvalidSignatureError:
      return HttpResponseForbidden()
    except LineBotApiError:
      return HttpResponseBadRequest()
    
    # 處理每個事件
    for event in events:
      if isinstance(event, MessageEvent):
        if isinstance(event.message, TextMessage):
          mtext = event.message.text
          weatherApi.handle_user_message(event, mtext)  # 縣市或景點的天氣判斷
          
          # 根據用戶消息處理邏輯
          if mtext == '穿搭日程':
            conversation_state['step'] = 'start_time'
            search_schedule.search_Date(event)
          elif mtext == '社群互動':
            social.sendSocial(event)
          elif mtext == '採購建議':
            purchase.sendBuy(event)
          elif conversation_state['step']:
            print('conversation_state')
            # insert_schedule.handleUserInput(event, conversation_state)
          else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mtext))
        
        elif isinstance(event.message, ImageMessage):  # 如果使用者有上傳圖片
          purchase.handle_image_message(event)
      
      if isinstance(event, PostbackEvent):
        backdata = dict(parse_qsl(event.postback.data))
        action = backdata.get('action')
        
        # 根據回傳的資料處理邏輯
        if action == 'date':
          print('date')
          # insert_schedule.sendBack_date(event, backdata)
        # elif action == 'datetime':
        #   insert_schedule.sendBack_datetime(event, backdata)
        elif action == 'yes':
          print('yes')
          # insert_schedule.sendStartTime(event)
        elif action == 'no':
          print('no')
          # insert_schedule.sendNo(event)
        elif action == 'search_date':
          search_schedule.Back_search_date(event, backdata)
        elif action == 'no_insert':
          search_schedule.insert_no(event)
        elif action == 'confirm':
          purchase.sendBack_confirm(event)
        elif action == 'modify':
          purchase.sendBack_modify(event)
        elif action == 'cancel':
          purchase.sendBack_cancel(event)
        elif action == 'again':
          purchase.sendBack_again(event)
        elif action == 'color':
          purchase.sendBack_color(event)
        elif action == 'describe':
          purchase.sendBack_describe(event)
        elif action == 'top':
          purchase.sendBack_top(event)
        elif action == 'bottom':
          purchase.sendBack_bottom(event)
        elif action == 'coat':
          purchase.sendBack_coat(event)
        elif action == 'dress':
          purchase.sendBack_dress(event)
        elif action == 'suit':
          purchase.sendBack_suit(event)
        elif action == 'upload':
          purchase.sendBack_upload(event)
        elif conversation_state['step']:
          print('conversation_state')
          # insert_schedule.handleUserInput(event, conversation_state)
        else:
          line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(backdata)))
    
    return HttpResponse("OK")  # 回應 HTTP 200
  else:
    return HttpResponseBadRequest()

def handleUserMessage(event, mtext):
  if conversation_state['step']:
    print('conversation_state')
    # insert_schedule.handleUserInput(event, conversation_state)
  else:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mtext))
