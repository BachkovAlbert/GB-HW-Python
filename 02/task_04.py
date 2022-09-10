# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input('Input number N: '))
list = []
for i in range((n*2)+1):
    element = -n + i 
    list.append(element)

print(list)
indexes = input(f'Input indices separated by a space(range from 0 to {len(list)-1}): ')
split = indexes.split(sep=' ')

result = 1
r = 0
i = 0

while r < len(split):
    if int(split[i]) > len(list) - 1:
        print(f'Input an indices number from 0 to {len(list)-1} (your indice = {split[i]})')
        r +=1
        i +=1
    else:
        result *= int(list[int(split[i])])
        i += 1
        r += 1

if result == 1:
    print() 
else:
    print(f'Product of values with selected indices (which are included in the boundary) = {result}')