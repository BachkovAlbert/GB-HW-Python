# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def create_list(k):
    list = []      
    for i in range(k + 1):
        list.append(random.randint(0, 100))
    return list
    
def polynomial_creation(l):
    list= l[:]
    new_list = ''
    if len(list) < 1:
        new_list = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                if list[i] == 1:
                    new_list += f'x^{len(list)-i-1}'
                else:
                    new_list += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    new_list += ' + '
                else: 
                    while list[i+1] == 0 and i != len(list) - 2:
                        if list[i + 1] == 0: 
                            new_list += ''
                        i += 1
                    if list[i+1] != 0:
                        new_list += ' + '
                    
            elif i == len(list) - 2 and list[i] != 0:
                if list[i] == 1:
                    new_list += f'x'
                else:    
                    new_list += f'{list[i]}x'
                if list[i+1] != 0:
                    new_list += ' + '

            elif i == len(list) - 1 and list[i] != 0:
                new_list += f'{list[i]} = 0'

            elif i == len(list) - 1 and list[i] == 0:
                new_list += ' = 0'
                
    return new_list

def write_file(f):
    with open('polynomial(task_04).txt', 'w') as file:
        file.write(f)

k = int(input('input natural degree k: '))

list = create_list(k)           

print(list)      
print(polynomial_creation(list))    

write_file(polynomial_creation(list))

