# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def deletion_of_repetitions(list):
    lst = []
    i = 0
    while i < len(list):
        count = list.count(list[i])
        if count == 1:
            lst.append(list[i])
        i += 1
    return lst

print(deletion_of_repetitions([1, 1, 2, 3, 4, 5, 5]))

