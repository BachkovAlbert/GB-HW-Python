# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Input number of coordinate quarter: '))

if num < 1 or num > 4:
    print('Input number of coordinate quarter from 1 to 4')
elif num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')

