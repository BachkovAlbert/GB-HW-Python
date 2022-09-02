# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input("Input x: ")
y = input("Input y: ")
z = input("Input z: ")

function_1 = not (x or y or z)
function_2 = not x and not y and not z

if function_1 == function_2: print('True')
else: print('False') 

