import operations as ots
import config as cf

def start():
    city = input('Напишите название города: ')
    try:
        latitude, longitude = ots.geo_pos(city)
        
        yandex_weather_x = ots.yandex_weather(latitude, longitude, cf.token_yandex)
        print(f'Яндекс нашел город -> {yandex_weather_x["city"]}')

        for i in yandex_weather_x.keys():
            if i != 'link' and i != 'city':
                print(f'Сейчас {yandex_weather_x[i]["temp"]}C°, на небе {yandex_weather_x[i]["condition"]}.')
    except AttributeError as err:
        print(f'Город не найден, ошибка: {err}, проверте корректность названия города') 

   