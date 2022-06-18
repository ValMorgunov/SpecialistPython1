# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("first:"))  # Первое число
second_number = int(input("second:"))  # Второе число
if first_number > second_number:
    first_number, second_number = second_number, first_number
div_3 = []
while first_number < second_number:
    if first_number % 3 == 0:
        div_3.append(str(first_number))
    first_number += 1
print(", ".join(div_3))
