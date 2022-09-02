# Напишите программу, 
# которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input("Input x: "))
y = float(input("Input y: "))

if x == 0 and y ==0:
    print('Input x and y > 0')
elif x == 0 and (y > 0 or y < 0):
    print('The point is on the y-axis')
elif y == 0 and (x > 0 or x < 0):
    print('The point is on the x-axis')    
elif x > 0 and y > 0: 
    print('I')
elif x < 0 and y > 0: 
    print('II')
elif x < 0 and y < 0: 
    print('III')
elif x > 0 and y <0: 
    print('IV')
  