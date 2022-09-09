# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Input number k: '))
sum = 0

# for i in range(1, k+1):
#     mus = (1 + 1/i)**i
#     print(mus, end = '+') 
    
# print('\n')

for i in range(1, k+1):
    sum += (1 + 1/i)**i
    # print(sum, end=' ')

print(f'\nThe sum is(=) {round(sum, 2)}')

