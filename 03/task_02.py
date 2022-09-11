# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def List_creation(n):
    list = []
    for i in range(n):
        element = input(f'Input {i+1} integer element: ') 
        list.append(element)
    print(list)
    return list

def Proizved(array):
    new_list = []
    for i in range(len(array) // 2):
        new_list += ([int(array[i]) * int(array[-1 - i])])
    if len(array) % 2 != 0:
        new_list.append(int(array[(len(array) // 2)]) ** 2)
    return new_list

size = int(input('Input number N: '))

print(Proizved(List_creation(size)))
