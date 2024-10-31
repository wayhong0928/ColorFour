import os
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, URIAction

load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))


def sendSocial(event):  # 社群互動
    try:
        message = TextSendMessage(
            text="吉阿瓜在您的貼文中評論和按讚囉！",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=URIAction(
                            label="前往社群互動平台",
                            uri="https://wayhong0928.github.io/ColorFour-FrontEnd/templates/social_index.html",
                        )
                    ),
                ]
            ),
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤!"))
