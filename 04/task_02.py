# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def Simple_Multipliers(num):
    i = 2 
    list = []
    while i <= num:
        if num % i == 0:
            list.append(i)
            num /= i
        else:
            i += 1
    return list

print(Simple_Multipliers(20))
