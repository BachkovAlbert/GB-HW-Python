# Player VS Bot

import random 

def input_amount(name):
    status = False
    while not status:
        amt = input(f'{name}, введите сколько конфет возьмете (от 1 до {candy_max_size}): ')
        try:
            amt = int(amt)
        except:
            print ('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if amt >= 1 and amt <= candy_max_size:
            status = True
        else:
            print(f'{name}, ввел не корректное количество конфет.')
    return amt

def result_intermediate(name, amt, count, t_candy):
    print(f'Игрок ({name}) взял {amt} конфет/(-ы)/(-у), теперь у него {count} конфет. Осталось на столе {t_candy} конфет')

player_1 = input('Введите имя первого игрока: ')
player_3 = 'Bot'


count_1 = 0
count_3 = 0

table_candy = int(input('Введите количество конфет на столе: ')) 
candy_max_size = int(input('Введите максимальное количество конфет которые можно взять за ход: ')) 

rndm = random.randint(1,2)
print(f'{rndm} игрок ходит первым')

while table_candy > 0:     
    if rndm == 1:
        amount_1 = input_amount(player_1)
        table_candy -= amount_1
        count_1 += amount_1
        result_intermediate(player_1, amount_1, count_1, table_candy)
        position = player_1 
        rndm = 2
    elif rndm == 2:    
        amount_3 = random.randint(1, candy_max_size)
        table_candy -= amount_3
        count_3 += amount_3
        result_intermediate(player_3, amount_3, count_3, table_candy)
        position = player_3 
        rndm = 1
    
print(f'победил игрок {position}')