import os
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, ImageSendMessage
from linebot.models import DatetimePickerTemplateAction, ConfirmTemplate, PostbackTemplateAction


load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINE_MESSAGING_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_MESSAGING_CHANNEL_SECRET"))


def search_Date(event):  # 穿搭日程快速選日期
    try:
        message = TemplateSendMessage(
            alt_text="選取日期",
            template=ButtonsTemplate(
                title="快速查詢穿搭日程安排",
                text="請選擇：",
                actions=[
                    DatetimePickerTemplateAction(
                        label="選取日期",
                        data="action=search_date&mode=date",
                        mode="date",
                        initial="2024-11-02",
                        min="2024-01-01",
                        max="2024-12-31",
                    )
                ],
            ),
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=f"發生錯誤！{e}")
        )


def Back_search_date(event, backdata):  # 回傳日期以及確認按鈕
    try:
        if backdata.get("mode") == "date":
            dt = "日期為：" + event.postback.params.get("date")
        message = [
            TextSendMessage(text=dt),
            ImageSendMessage(  # 報告照片
                original_content_url="https://imgur.com/OXVtzRw.png",
                preview_image_url="https://imgur.com/OXVtzRw.png",
            ),
            TextSendMessage(
                text="開始時間：2024-11-02 8:00\n結束時間：2024-11-02 17:00\n目的地：台大體育館\n日程名稱：專題報告\n穿搭名稱：期末報告服裝"
            ),
            TemplateSendMessage(
                alt_text="確認是否要新增穿搭日程安排",
                template=ConfirmTemplate(
                    text="要不要新增其他穿搭日程呢~",  # 副標題
                    actions=[
                        PostbackTemplateAction(
                            label="好呀", data="action=yes", display_text="好呀"
                        ),
                        PostbackTemplateAction(
                            label="先不用",
                            data="action=no_insert",
                            display_text="先不用",
                        ),
                    ],
                ),
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤!"))


def insert_no(event):  # 日程安排的確認按鈕(先不要)
    try:
        message = TextSendMessage(text="好的，沒關係。")
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤!"))
