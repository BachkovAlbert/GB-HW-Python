# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

def List_creation(n):
    list = []
    for i in range(n):
        element = input(f'Input {i+1} integer element: ') 
        list.append(element)
    print(list)
    return list

def Sum(array):
    result = 0
    for i in range(1, len(array), 2):
        result += int(array[i])
    return result

size = int(input('Input number N: '))

print(Sum(List_creation(size)))
