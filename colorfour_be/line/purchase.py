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

def sendBuy(event): #採購建議
    try:
        message = TextSendMessage( 
            text="請選擇要上傳的主要服裝",                                 
            quick_reply = QuickReply(
                items =[
                    QuickReplyButton(
                        action = PostbackAction(label = "上衣", data='action=top', display_text = "上衣")    
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label = "下身", data='action=bottom', display_text = "下身")
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label = "外套", data='action=coat', display_text = "外套")
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label = "洋裝", data='action=dress', display_text = "洋裝")
                    ),
                    QuickReplyButton(
                        action = PostbackAction(label = "西裝", data='action=suit', display_text = "西裝")
                    ),                       
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_top(event): #回傳上衣的次要種類
  try:
    message = TextSendMessage(
        text="請選擇要上傳的次要服裝種類",          
        quick_reply = QuickReply(
            items =[
                QuickReplyButton(
                    action = PostbackAction(label = "長袖T恤", data='action=upload', display_text = "長袖T恤")    
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "短袖T恤",  data='action=upload', display_text = "短袖T恤")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "無袖上衣",  data='action=upload', display_text = "無袖上衣")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "長袖襯衫",  data='action=upload', display_text = "長袖襯衫")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "短袖襯衫",  data='action=upload', display_text = "短袖襯衫")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "帽T/大學T",  data='action=upload', display_text = "帽T/大學T")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "針織衫",   data='action=upload', display_text = "針織衫")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "毛衣",  data='action=upload', display_text = "毛衣")
                ),                       
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))
    
def sendBack_upload(event): #選完次要種類後，機器人回傳上傳圖片
  try:
    message = TextSendMessage(text="請上傳服飾圖片~")
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_bottom(event): #回傳下身的次要種類
  try:
    message = TextSendMessage(            
        quick_reply = QuickReply(
            items =[
                QuickReplyButton(
                    action = PostbackAction(label = "長裙", data='action=upload',display_text = "長裙")    
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "短裙", data='action=upload',display_text = "短裙")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "連身裙", data='action=upload',display_text = "連身裙")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "吊帶褲", data='action=upload',display_text = "吊帶褲")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "牛仔褲", data='action=upload',display_text = "牛仔褲")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "一般長褲", data='action=upload',display_text = "一般長褲")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "短褲",  data='action=upload',display_text = "短褲")
                ),                      
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_coat(event): #回傳外套的次要種類
  try:
    message = TextSendMessage(            
        quick_reply = QuickReply(
            items =[
                QuickReplyButton(
                    action = PostbackAction(label = "外套", data='action=upload',display_text = "外套")    
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "大衣", data='action=upload',display_text = "大衣")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "風衣", data='action=upload',display_text = "風衣")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "皮夾克", data='action=upload',display_text = "皮夾克")
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "羽絨外套", data='action=upload',display_text = "羽絨外套")
                ),                   
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))


def sendBack_dress(event): ##回傳洋裝的次要種類
  try:
    message = TextSendMessage(            
        quick_reply = QuickReply(
            items =[
                QuickReplyButton(
                    action = PostbackAction(label = "洋裝", data='action=upload',display_text = "洋裝")    
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "禮服", data='action=upload',display_text = "禮服")
                ),                   
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_suit(event): #回傳西裝的次要種類
  try:
    message = TextSendMessage(            
        quick_reply = QuickReply(
            items =[
                QuickReplyButton(
                    action = PostbackAction(label = "西裝外套", data='action=upload',display_text = "西裝外套")    
                ),
                QuickReplyButton(
                    action = PostbackAction(label = "西裝褲", data='action=upload',display_text = "西裝褲")
                ), 
                QuickReplyButton(
                    action = PostbackAction(label = "西裝裙", data='action=upload',display_text = "西裝裙")
                ),                   
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
  except:
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))


def handle_image_message(event): #錯的採購建議樣板
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目左至右
            header=BoxComponent(
                layout='vertical',  # 垂直
                contents=[
                    TextComponent(text='採購建議', weight='bold', size='xl'),
                ]
            ),
            hero=ImageComponent(
                url='https://imgur.com/t1Jsp0p.png',
                size='full',
                aspect_ratio='650:650',  #長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='您上傳的服飾描述為：', size='md'),
                    BoxComponent(
                        layout='horizontal',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    TextComponent(
                                        text='米白色上衣，並有紅色GAP字樣。', size='sm', color='#666666', flex=2
                                    ),
                                    TextComponent(
                                        text='若沒問題請點選確定以進行採購建議演算法。', size='sm', color='#666666', flex=2
                                    ),
                                ],
                            ),
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        spacing='md',
                        contents=[
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=PostbackAction(
                                    label='重新辨識', data='action=again', display_text='重新辨識'),

                            ),
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=PostbackAction(
                                    label='修改描述', data='action=modify', display_text='修改描述'),
                            )
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        spacing='md',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=PostbackAction(
                                    label='確定', data='action=confirm', display_text='確定'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=PostbackAction(
                                    label='取消', data='action=cancel', display_text='取消'),
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ColorFour 2024',size='sm', color='#888888', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="採購建議", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
      line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

def sendBack_again(event): #重新辨識->對的採購建議樣板
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目左至右
            header=BoxComponent(
                layout='vertical',  # 垂直
                contents=[
                    TextComponent(text='採購建議', weight='bold', size='xl'),
                ]
            ),
            hero=ImageComponent(
                url='https://imgur.com/t1Jsp0p.png',
                size='full',
                aspect_ratio='650:650',  # 長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='您上傳的服飾描述為：', size='md'),
                    BoxComponent(
                        layout='horizontal',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[
                                    TextComponent(
                                        text='白色上衣，並有粉紅色GAP字樣。', size='sm', color='#666666', flex=2
                                    ),
                                    TextComponent(
                                        text='請點選確定進行比對。', size='sm', color='#666666', flex=2
                                    ),
                                ],
                            ),
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        spacing='md',
                        contents=[
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=PostbackAction(
                                    label='重新辨識', data='action=again', display_text='重新辨識'),

                            ),
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=PostbackAction(
                                    label='修改描述', data='action=modify', display_text='修改描述'),
                            )
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        spacing='md',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=PostbackAction(
                                    label='確定', data='action=confirm', display_text='確定'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=PostbackAction(
                                    label='取消', data='action=cancel', display_text='取消'),
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ColorFour 2024',size='sm', color='#888888', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="採購建議", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_modify(event): #修改描述的樣板按鈕
    try:
        message = TemplateSendMessage(
            alt_text='修改描述',
            template = ButtonsTemplate(
                title = '修改描述樣板', #主標題
                text = '請選擇:',  #副標題
                actions=[
                    PostbackTemplateAction(
                        label='顏色',
                        data= 'action=color'
                    ),
                    PostbackTemplateAction(
                        label='描述',
                        data= 'action=describe'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_color(event): #採購建議修改描述_顏色
    try:
        message = TextSendMessage(
            text="請輸入顏色"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))



def sendBack_describe(event): #修改描述_描述
    try:
        message = TextSendMessage(
            text="請重新描述"
        ),
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))


def sendBack_confirm(event): #採購建議的確認按鈕
    try:
        message = TextSendMessage(
            text="該服飾重複率約 50%\n適合程度為 70%"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))

def sendBack_cancel(event): #採購建議的取消
    try:
        text1 = '您已取消採購建議。'
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '發生錯誤!'))