# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141

import math

def Accuracy_rounding(num, acc):
    d = 0
    while acc < 1:
        acc *= 10
        d += 1
    return round(num, d)

print(Accuracy_rounding(math.pi, 0.001))
