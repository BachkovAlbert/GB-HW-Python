# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:   - 0,56 -> 11

string = '0.56'

char_list = [i for i in string]
char_list.remove('.')

res = sum(map(int, char_list))

print(f'{string} -> {res}')