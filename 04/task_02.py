# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def simple_multipliers(num):
    i = 2 
    list = []
    while i <= num:
        if num % i == 0:
            list.append(i)
            num /= i
        else:
            i += 1
    return list

print(simple_multipliers(20))
