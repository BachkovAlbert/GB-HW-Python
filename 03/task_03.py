# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:  - [1.1, 1.2, 3.1, 10.01] => 0.19

def List_creation(n):
    list = []
    for i in range(n):
        element = input(f'Input {i+1} float element: ') 
        list.append(element)
    print(list)
    return list

def Difference(array):
    new_list = []
    for i in range(len(array)):
        element = float(array[i]) % 1 
        new_list.append(element)
    return max(new_list) - min(new_list)

size = int(input('Input number N: '))

print(round(Difference(List_creation(size)), 2))
