# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    fib = [0]
    f = 0
    s = 1
    t = 1
    for i in range(n):
        fib.append(t)
        t = f+s
        f = s
        s = t
    return fib

def Nega_Fibonacci(n):
    neg_fib = []
    f = 0
    s = 1
    t = 1
    for i in range(n):
        neg_fib.append(t)
        t = f-s
        f = s
        s = t
    neg_fib.reverse()
    return neg_fib

num = int(input('Input integer number: '))
print(Nega_Fibonacci(num) + Fibonacci(num))



