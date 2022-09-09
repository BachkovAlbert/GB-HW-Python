# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



n = int(input('Input number N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')

print(f'\nFactorial of a number(N = {n}): {factorial}')


# import math
# n = int(input('Input number N: '))
# print("Factorial of a number(N):", math.factorial(n))