# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

numbers = []
n = int(input("n: ")) - 1
i = 0
summ = 0
while i <= n:
    numbers.append(random.randint(-100, 100))
    if int(numbers[i]) > 0 and int(numbers[i]) % 2 == 0:
        summ += int(numbers[i])
    i += 1
print(numbers)
print(summ)
