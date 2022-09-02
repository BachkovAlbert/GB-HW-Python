# Напишите программу, 
# которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

print('Input coordinates point А:')
x_A = float(input('x: '))
y_A = float(input('y: '))

print('Input coordinates point B:')
x_B = float(input('x: '))
y_B = float(input('y: '))

distance = math.sqrt((x_B - x_A)**2 + (y_B - y_A)**2)

print(f'Distance between A and B: {round(distance, 2)}')

