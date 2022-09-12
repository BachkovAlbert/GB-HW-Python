# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def Transform(n):
    t = ''
    while n != 0:
        t = str(n%2) + t
        n //= 2
    return t

num = int(input('Input integer number: '))
print(Transform(num))