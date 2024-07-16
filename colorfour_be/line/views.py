from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import json
import requests
# from testapp.models import student

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, ImageSendMessage, StickerSendMessage, MessageTemplateAction
from linebot.models import DatetimePickerTemplateAction, QuickReply, QuickReplyButton, MessageAction, URIAction,PostbackAction
from linebot.models import TemplateSendMessage, ButtonsTemplate, PostbackEvent, ImageMessage, ConfirmTemplate, FlexSendMessage
from linebot.models import PostbackTemplateAction, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, ImageComponent
from line import insert_schedule, purchase, social, search_schedule

from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_MESSAGING_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_MESSAGING_CHANNEL_SECRET)
conversation_state = {'step': None, 'data': {}}

@csrf_exempt
def callback(request):
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

def line_callback(request):
	# 處理回調邏輯
	return HttpResponse('Callback handled')

def line_login(request):
  code = request.GET.get('code')
  state = request.GET.get('state')
  # 處理登錄邏輯，例如交換授權碼和獲取用戶資料
  if code:
    try:
      # 交換授權碼獲取訪問令牌的邏輯
      # user_info = some_function_to_get_user_info(code)

      # 登錄成功後重定向到本地前端頁面，附加 loginResult 參數
      return HttpResponseRedirect(f'https://wayhong0928.github.io/ColorFour-FrontEnd/index.html?loginResult=success')
    except Exception as e:
      # 登錄失敗的邏輯
      return HttpResponseRedirect(f'http://localhost:8080?loginResult=failure')
    return HttpResponse('No code or state provided')