from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
# from testapp.models import student

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TemplateSendMessage, TextSendMessage, TextMessage, PostbackEvent
from linebot.models import  TextSendMessage, TemplateSendMessage, PostbackTemplateAction, ConfirmTemplate
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_MESSAGING_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_MESSAGING_CHANNEL_SECRET)


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
