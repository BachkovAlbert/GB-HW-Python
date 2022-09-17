# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def create_list(k):
    tsil = []      
    for i in range(k + 1):
        tsil.append(random.randint(0, 100))
    return tsil
    
def polynomial_creation(l):
    tsil= l[:]
    new_list = ''
    if len(tsil) < 1:
        new_list = 'x = 0'
    else:
        for i in range(len(tsil)):
            if i != len(tsil) - 1 and tsil[i] != 0 and i != len(tsil) - 2:
                if tsil[i] == 1:
                    new_list += f'x^{len(tsil)-i-1}'
                else:
                    new_list += f'{tsil[i]}x^{len(tsil)-i-1}'
                if tsil[i+1] != 0:
                    new_list += ' + '
                else: 
                    while tsil[i+1] == 0 and i != len(tsil) - 2:
                        if tsil[i + 1] == 0: 
                            new_list += ''
                        i += 1
                    if tsil[i+1] != 0:
                        new_list += ' + '
                    
            elif i == len(tsil) - 2 and tsil[i] != 0:
                if tsil[i] == 1:
                    new_list += f'x'
                else:    
                    new_list += f'{tsil[i]}x'
                if tsil[i+1] != 0:
                    new_list += ' + '

            elif i == len(tsil) - 1 and tsil[i] != 0:
                new_list += f'{tsil[i]} = 0'

            elif i == len(tsil) - 1 and tsil[i] == 0:
                new_list += ' = 0'
                
    return new_list

def write_file(f):
    with open('polynomial(task_04).txt', 'w') as file:
        file.write(f)

k = int(input('input natural degree k: '))

tsil = create_list(k)           

print(tsil)      
print(polynomial_creation(tsil))    

write_file(polynomial_creation(tsil))

