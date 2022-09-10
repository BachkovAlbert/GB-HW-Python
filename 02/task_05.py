# Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Input size list: '))
list = []

for i in range(n):
    element = input(f'Input {i+1} element: ')
    list.append(element)

print(f'Initial list: {list}')
random.shuffle(list)
print(f'Jumbled list: {list}')