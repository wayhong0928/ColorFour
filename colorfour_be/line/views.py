from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
# from testapp.models import student

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
<<<<<<< HEAD
from linebot.models import MessageEvent, TextSendMessage, TextMessage, ImageSendMessage, StickerSendMessage, MessageTemplateAction
from linebot.models import DatetimePickerTemplateAction, QuickReply, QuickReplyButton, MessageAction, URIAction,PostbackAction
from linebot.models import TemplateSendMessage, ButtonsTemplate, PostbackEvent, ImageMessage, ConfirmTemplate, FlexSendMessage
from linebot.models import PostbackTemplateAction, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, ImageComponent
from line import insert_schedule, purchase, social, search_schedule

=======
from linebot.models import MessageEvent, TemplateSendMessage, TextSendMessage, TextMessage, PostbackEvent
from linebot.models import  TextSendMessage, TemplateSendMessage, PostbackTemplateAction, ConfirmTemplate
>>>>>>> upstream/main
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_MESSAGING_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_MESSAGING_CHANNEL_SECRET)
<<<<<<< HEAD
conversation_state = {'step': None, 'data': {}}

@csrf_exempt #註解函式視圖可被跨域訪問
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8') #解碼
        try: #驗證過程
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '穿搭日程':
                        conversation_state['step'] = 'start_time'
                        search_schedule.search_Date(event)                    
                    elif mtext == '社群互動':
                        social.sendSocial(event)                
                    elif mtext == '採購建議':
                        purchase.sendBuy(event)
                    elif conversation_state['step']:
                        insert_schedule.handleUserInput(event, conversation_state)
                    else:                           
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = mtext))
                elif isinstance(event.message, ImageMessage): #如果使用者有上傳圖片
                    purchase.handle_image_message(event)
                
            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == 'date': #新增穿搭日程
                    insert_schedule.sendBack_date(event, backdata)
                elif backdata.get('action') == 'datetime':
                    insert_schedule.sendBack_datetime(event, backdata)
                elif backdata.get('action') == 'yes':
                    insert_schedule.sendStartTime(event)
                elif backdata.get('action') == 'no':    
                    insert_schedule.sendNo(event)
                elif backdata.get('action') == 'search_date': #查詢穿搭日程
                    search_schedule.Back_search_date(event, backdata)
                elif backdata.get('action') == 'no_insert':    
                    search_schedule.insert_no(event)
                elif backdata.get('action') == 'confirm':    
                    purchase.sendBack_confirm(event)
                elif backdata.get('action') == 'modify':    
                    purchase.sendBack_modify(event)
                elif backdata.get('action') == 'cancel':    
                    purchase.sendBack_cancel(event)
                elif backdata.get('action') == 'again':    
                    purchase.sendBack_again(event)
                elif backdata.get('action') == 'color':    
                    purchase.sendBack_color(event)
                elif backdata.get('action') == 'describe':    
                    purchase.sendBack_describe(event)
                elif backdata.get('action') == 'top':    
                    purchase.sendBack_top(event)
                elif backdata.get('action') == 'bottom':    
                    purchase.sendBack_bottom(event)
                elif backdata.get('action') == 'coat':    
                    purchase.sendBack_coat(event)
                elif backdata.get('action') == 'dress':    
                    purchase.sendBack_dress(event)
                elif backdata.get('action') == 'suit':    
                    purchase.sendBack_suit(event)
                elif backdata.get('action') == 'upload':    
                    purchase.sendBack_upload(event)
                elif conversation_state['step']:
                    insert_schedule.handleUserInput(event, conversation_state)
                #elif backdata.get('action') == 'project': #期末穿搭
                    #insert_schedule.End_schedule(event)
                #elif backdata.get('action') == 'showtime': #表演服
                    #insert_schedule.show(event)
                else:
                  line_bot_api.reply_message(event.reply_token, TextSendMessage(text = backdata))
        return HttpResponse() #代碼200
    else:
        return HttpResponseBadRequest()    

def handleUserMessage(event, mtext):
    if conversation_state['step']:
        insert_schedule.handleUserInput(event, conversation_state)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=mtext))
=======


# input_friend_name = False

@csrf_exempt
def callback(request):
  # global input_friend_name
  if request.method == 'POST':
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
      events = parser.parse(body, signature)
    except InvalidSignatureError:
      return HttpResponseForbidden()
    except LineBotApiError:
      return HttpResponseBadRequest()
    
    for event in events:
      if isinstance(event, MessageEvent):
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))
        if isinstance(event.message, TextMessage):
          mtext = event.message.text
          if mtext == '@傳送文字':
            sendText(event)
          else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))

      if isinstance(event, PostbackEvent): # PostbackTemplateAction，觸發 Postback 事件
        backdata = dict(parse_qsl(event.postback.data)) # 取得 Postback 資料

        if backdata.get('action') == 'Yes':
          sendYes(event)
        elif backdata.get('action') == 'No':
          sendNo(event)
        elif backdata.get('action') == 'Cancel':
          sendCancel(event)

    return HttpResponse()
  else:
    return HttpResponseBadRequest()

def sendText(event):
  try:
    message = TextSendMessage (
      text = "我是 ColorFour，\n您好！"
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '傳送文字發生錯誤！'))


def sendConfirm(event):
  try:
    message = TemplateSendMessage (
      alt_text = '確認樣板',
      template=ConfirmTemplate(
        text='你確定要購買這項商品嗎？',
        actions=[
          PostbackTemplateAction(
            label='是',
            data='action=Yes'
          ),
          PostbackTemplateAction(
            label='否',
            data='action=No'
          )
        ]
      )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤！{}'.format(e)))

def sendYes(event):
  try:
    message = TextSendMessage (
      text = "感謝您的購買，\n我們會盡快為您製作"
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤！{}'.format(e)))

def sendNo(event):
  try:
    message = TextSendMessage (
      text = "沒關係，\n請重新選擇商品"
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤！{}'.format(e)))

def sendCancel(event):
  try:
    message = TextSendMessage (
      text = "沒關係，\n我們會替您取消"
    )
    line_bot_api.reply_message(event.reply_token, message)
  except Exception as e:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤！{}'.format(e)))
>>>>>>> upstream/main
