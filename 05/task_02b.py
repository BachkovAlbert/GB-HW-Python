# Player VS Smart Bot

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
    print(f'Игрок ({name}) взял {amt} конфет/(-ы)/(-у), теперь у него {count} конфет. На столе осталось {t_candy} конфет/(-ы)/(-a)')

def smart_bot(t_candy, candy_m_s):
    if t_candy % (candy_m_s + 1) == 0:
        return random.randint(1, candy_m_s)
    else:
        return t_candy % (candy_m_s + 1)

player_1 = input('Введите имя первого игрока: ')
player_4 = 'Smart Bot'

count_1 = 0
count_4 = 0

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
        amount_4 = smart_bot(table_candy, candy_max_size)
        table_candy -= amount_4
        count_4 += amount_4
        result_intermediate(player_4, amount_4, count_4, table_candy)
        position = player_4 
        rndm = 1

print(f'победил игрок {position}')