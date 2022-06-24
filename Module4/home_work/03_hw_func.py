# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

import random


def check(x1, y1, x2, y2, r1, r2):
    return (y1 - x1) ** 2 + (y2 - x2) ** 2 > (r2 - r1) ** 2


x1, y1, x2, y2, r1, r2 = [random.randint(1, 30) for i in range(6)]
print(check(x1, y1, x2, y2, r1, r2))
print((y1 - x1) ** 2 + (y2 - x2) ** 2)
print((r2 - r1) ** 2)
