# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Player VS Player

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
    print(f'Игрок ({name}) взял {amt} конфет/(-ы)/(-у), теперь у него {count} конфет. На столе осталось {t_candy} конфет/(-a)')

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

count_1 = 0
count_2 = 0

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
        amount_2 = input_amount(player_2)
        table_candy -= amount_2
        count_2 += amount_2
        result_intermediate(player_2, amount_2, count_2, table_candy)
        position = player_2 
        rndm = 1

print(f'Победил игрок {position}')

# Что-бы выйграть первому ходившему игроку, при условии что игрок сделалавший последний ход выигрывает:
#    надо что-бы количество конфет {table_candy} делилось на ({candy_max_size} +1) без остатка (кратное) во время хода второго игрока.
#   (Если будет количество конфет {table_candy} сразу делится на ({candy_max_size} +1) без остатка, 
#   то если второй игрок знает эту методику то выйграет, если нет, первый игрок знающий эту методику сможет подстроится что-бы выйграть)

# Что-бы выйграть первому ходившему игроку, при условии что игрок сделалавший последний ход проигрывает:
#    надо что-бы количество конфет {table_candy} делилось на (({candy_max_size} +1) без остатка (кратное))  + 1 к {table_candy}  во время хода второго игрока.

