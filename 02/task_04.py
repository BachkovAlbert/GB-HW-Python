# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random


# n = int(input('Input number N: '))
# array = [-n, n]
# random.cchoices(-n,n)

# print(array)



# list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# print(random.choice(list))

# print(random.randint(-5, 5))

# print(random.randrange(-2, 2)) 

# print (random.sample(list,2))


# list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]



n = int(input('Input number N: '))
list = []
for i in range(n*2):
    element = -n
    list.append(element)

print(list)