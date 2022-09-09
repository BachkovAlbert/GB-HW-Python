# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:   - 0,56 -> 11

number = input('Input float positive number: ')
sum = 0
for i in number:
    if i != ',' and i != '.' and i != ' ':
        sum += int(i)
print(sum)
