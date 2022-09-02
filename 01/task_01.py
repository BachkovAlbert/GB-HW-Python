# Напишите программу, 
# которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input("Input number: "))

if 0 < num < 6:
    print("No")
elif 5 < num < 8: 
    print('Yes')
else: print('Input number from 1 to 7')





