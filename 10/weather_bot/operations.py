from geopy import geocoders
import requests as req
import json
import config as cf

def send_welcome(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = f'Я погодабот, приятно познакомитсья, {update.effective_user.first_name}. '
                                    f'Напишите название города.')                                          

def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def yandex_weather(latitude, longitude, token_yandex: str):
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast/?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': token_yandex}, verify=False)
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}

    yandex_json = json.loads(yandex_req.text)
    yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    yandex_json['fact']['wind_dir'] = wind_dir[yandex_json['fact']['wind_dir']]

    weather = dict()
    params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    weather['fact'] = dict()
    weather['fact']['temp'] = yandex_json['fact']['temp']
    for param in params:
        weather['fact'][param] = yandex_json['fact'][param]

    weather['link'] = yandex_json['info']['url']
    weather['city'] = yandex_json['geo_object']['locality']['name']
    return weather
  
def input_text(update, context):
    city = update.message.text.lower()
    if city == 'привет':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f'Яндекс-бот-погода приветствует тебя {update.effective_user.first_name}, '
                                     f'напишите название города в котором хотите узнать погоду.')    
    else:
        try:    
            latitude, longitude = geo_pos(city)
            yandex_weather_x = yandex_weather(latitude, longitude, cf.token_yandex)
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text=f'Яндекс нашел город -> {yandex_weather_x["city"]}')

            day = {'night': 'ночью', 'morning': 'утром', 'day': 'днем', 'evening': 'вечером', 'fact': 'сейчас'}   #??
            for i in yandex_weather_x.keys():
                if i != 'link' and i != 'city':
                    time_day = day[i]
                    context.bot.send_message(chat_id=update.effective_chat.id, 
                                            text=f'Температура {time_day} {yandex_weather_x[i]["temp"]}C°'
                                                 f', на небе {yandex_weather_x[i]["condition"]}.')

            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text=f'{update.effective_user.first_name}, здесь ссылка на подробности: '
                                         f'{yandex_weather_x["link"]}')  
        except AttributeError as err:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text = f'{update.effective_user.first_name}!'
                                            f'Я не нашел такого города!'
                                            f'И получил ошибку {err}, попробуй другой город')