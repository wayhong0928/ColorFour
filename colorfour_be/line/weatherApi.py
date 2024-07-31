import os
from django.conf import settings
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, BubbleContainer, BoxComponent, TextComponent, ImageComponent, ButtonComponent
from linebot.models import PostbackAction, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction
from linebot.models import QuickReply, QuickReplyButton, MessageAction, URIAction


load_dotenv()
line_bot_api = LineBotApi(settings.LINE_MESSAGING_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_MESSAGING_CHANNEL_SECRET)
