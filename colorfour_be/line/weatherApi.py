import os, json, time,requests
from django.conf import settings
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, BubbleContainer, BoxComponent, TextComponent, ImageComponent, ButtonComponent
from linebot.models import PostbackAction, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction
from linebot.models import QuickReply, QuickReplyButton, MessageAction, URIAction


load_dotenv()
line_bot_api = LineBotApi(settings.LINE_MESSAGING_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_MESSAGING_CHANNEL_SECRET)
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
CWB_API_KEY = os.getenv('CWB_API_KEY')

conversation_state = {'step': None, 'data': {}}

def handle_user_message(event, mtext):
  if conversation_state['step'] is None:
    if mtext.lower() == '天氣':
      conversation_state['step'] = 'choose_location_type'
      send_location_type_quick_reply(event)
  elif conversation_state['step'] == 'choose_location_type':
    if mtext == '縣市':
      conversation_state['step'] = 'input_city'
      line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入縣市'))
    elif mtext == '景點':
      conversation_state['step'] = 'choose_spot'
      send_spot_quick_reply(event)
  elif conversation_state['step'] == 'input_city':
    conversation_state['data']['city'] = mtext
    conversation_state['step'] = 'input_district'
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入區域'))
  elif conversation_state['step'] == 'choose_spot':  
    spot_name = mtext
    if spot_name in ['玉山', '合歡山', '拉拉山', '梨山']:
      lat, lon = get_place_coordinates(spot_name)
      if lat and lon:
        weather_info = get_weather_by_coordinates(lat, lon)
        reply = f'{spot_name} 的天氣狀況如下：\n{weather_info}'
      else:
        reply = f'無法取得 {spot_name} 的準確位置和天氣資訊。'
    else:
      reply = f'無法識別的景點：{spot_name}'
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    conversation_state['step'] = None
    conversation_state['data'] = {}
    
  elif conversation_state['step'] == 'input_district':
    conversation_state['data']['district'] = mtext
    city = conversation_state['data']['city']
    district = conversation_state['data']['district']
    reply = get_weather_info(city, district)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    conversation_state['step'] = None
    conversation_state['data'] = {}
    
def send_location_type_quick_reply(event):
  message = TextSendMessage(
    text='請選擇縣市或景點',
    quick_reply=QuickReply(
      items=[
        QuickReplyButton(action=MessageAction(label='縣市', text='縣市')),
        QuickReplyButton(action=MessageAction(label='景點', text='景點'))
      ]
    )
  )
  line_bot_api.reply_message(event.reply_token, message)

def send_spot_quick_reply(event):
  message = TextSendMessage(
    text='請選擇景點',
    quick_reply=QuickReply(
      items=[
        QuickReplyButton(action=MessageAction(label='玉山', text='玉山')),
        QuickReplyButton(action=MessageAction(label='合歡山', text='合歡山')),
        QuickReplyButton(action=MessageAction(label='拉拉山', text='拉拉山')),
        QuickReplyButton(action=MessageAction(label='梨山', text='梨山'))
      ]
    )
  )
  line_bot_api.reply_message(event.reply_token, message)    

def get_weather_info(city, district): # 縣市行政區的天氣
  try:
    code = os.getenv('CWB_API_KEY')
    if not code:
      raise Exception("CWB_API_KEY is not set in the environment variables")

    urls = [
      f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization={code}',
      f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={code}'
    ]

    result = None
    for url in urls:
      response = requests.get(url)
      if response.status_code != 200:
        raise Exception(f"Error fetching data from {url}, status code: {response.status_code}")
      data = response.json()
      if 'records' not in data:
        raise Exception(f"Invalid response structure: {data}")

      stations = data['records']['Station'] # 抓A0001.json中Station的值
      for station in stations:
        if station['GeoInfo']['CountyName'] == city and station['GeoInfo']['TownName'] == district:
          print(f"Processing station in {city}, {district}") #終端機輸出結果
          weather_element = station.get('WeatherElement', {})
          print(f"Weather element: {weather_element}")  
          
          weather = weather_element.get('Weather', '未知') # 抓A0001.json的值
          temp = weather_element.get('AirTemperature', '未知')
          humid = weather_element.get('RelativeHumidity', '未知')
          
          result = f'{city}{district}。\n目前天氣狀況：{weather}\n溫度：{temp} 度，相對濕度：{humid}%。'
          break

    if not result:
      result = '找不到該區域的氣象資訊'
  except Exception as e:
    result = f'抓取失敗：{str(e)}'
  return result 

def get_place_coordinates(spot_name): #景點經緯度位置
    try:
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        if not api_key:
            raise Exception("GOOGLE_MAPS_API_KEY is not set in the environment variables")
        
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            'address': spot_name,
            'key': api_key,
            'language': 'zh-TW'
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Error fetching data from Google Maps API, status code: {response.status_code}")
        
        data = response.json()
        
        results = data.get('results', [])
        if not results:
            return None, None
        
        location = results[0]['geometry']['location']
        lat = location['lat']
        lon = location['lon']
        
        return lat, lon
    except Exception as e:
        print(f'抓取失敗：{str(e)}')
        return None, None

def get_weather_by_coordinates(lat, lon): #景點天氣
  try:
    code = os.getenv('CWB_API_KEY')
    if not code:
      raise Exception("CWB_API_KEY is not set in the environment variables")

    url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={code}'

    response = requests.get(url)
    if response.status_code != 200:
      raise Exception(f"Error fetching data from CWB API, status code: {response.status_code}")
    
    data = response.json()
    if 'records' not in data or 'location' not in data['records']:
      raise Exception(f"Invalid response structure: {data}")
    
    stations = data['records']['location']
    weather_info = None

    for station in stations:
      station_lat = float(station['StationLatitude'])
      station_lon = float(station['StationLongitude'])

      if abs(station_lat - lat) < 0.3 and abs(station_lon - lon) < 0.3:
        weather_element = {elem['elementName']: elem['elementValue'] for elem in station['weatherElement']}
        temp = weather_element.get('AirTemperature', '未知')
        humid = weather_element.get('RelativeHumidity', '未知')
        weather = weather_element.get('Weather', '未知')
        
        weather_info = f'天氣：{weather}\n溫度：{temp} 度\n相對濕度：{humid}%'
        break

    if not weather_info:
      weather_info = '找不到該位置的氣象資訊'
  except Exception as e:
    weather_info = f'抓取失敗：{str(e)}'

  return weather_info