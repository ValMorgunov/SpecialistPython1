# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
import random


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


xa, ya, xb, yb, xc, yc = [random.randint(1, 30) for i in range(6)]
name_min_line = "AB"
if distance(xa, ya, xb, yb) > distance(xb, yb, xc, yc) < distance(xa, ya, xc, yc):
    name_min_line = "BC"
elif distance(xa, ya, xb, yb) > distance(xa, ya, xc, yc):
    name_min_line = "AC"
print("Самый короткий отрезок:", name_min_line)  # Выводим название отрезка, например “АС”.
