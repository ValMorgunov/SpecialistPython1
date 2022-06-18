# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов
import random

n = int(input("n: "))
numbers = []
number = 0
summa = 0
for _ in range(n):
    number = random.randint(-10, 10)
    if number > 0:
        summa += number
    numbers.append(number)
print(numbers)
print(summa)
