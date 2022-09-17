# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random
from sympy import *


def create_list(k):
    tsil = []      
    for i in range(k + 1):
        tsil.append(random.randint(2, 100))
    return tsil
    
def polynomial_creation(l):
    tsil= l[:]
    new_list = ''
    if len(tsil) < 1:
        new_list = ''          
    else:
        for i in range(len(tsil)):
            if i != len(tsil) - 1 and tsil[i] != 0 and i != len(tsil) - 2:
                if tsil[i] == 1:
                    new_list += f'*x**{len(tsil)-i-1}'
                else:
                    new_list += f'{tsil[i]}*x**{len(tsil)-i-1}'
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
                    new_list += f'{tsil[i]}*x'
                if tsil[i+1] != 0:
                    new_list += ' + '

            elif i == len(tsil) - 1 and tsil[i] != 0:
                new_list += f'{tsil[i]}'                

            elif i == len(tsil) - 1 and tsil[i] == 0:       
                new_list += ''                          
                
    return new_list

def write_file(n, f):
    with open(n, 'w') as file:
        file.write(f)

k = int(input('input natural degree k1: '))
k_2 = int(input('input natural degree k2: '))

tsil = create_list(k)
tsil_2 = create_list(k_2)           

# print(tsil)      
# print(polynomial_creation(tsil))    

# print(tsil_2)      
# print(polynomial_creation(tsil_2)) 

write_file('polynomial_1(task_05).txt', polynomial_creation(tsil))
write_file('polynomial_2(task_05).txt', polynomial_creation(tsil_2))

with open('polynomial_1(task_05).txt', 'r') as file:
    pol_1 = file.readlines()
with open('polynomial_2(task_05).txt', 'r') as file:
    pol_2 = file.readlines()

pol_1 = ''.join(pol_1)
pol_2 = ''.join(pol_2)

print(pol_1)
print(pol_2)

pol_1 = sympify(pol_1)
pol_2 = sympify(pol_2)

print(pol_1 + pol_2)

sum = str(pol_1 + pol_2) + ' = 0'
write_file('sum_polynomial(task_05).txt', sum )

