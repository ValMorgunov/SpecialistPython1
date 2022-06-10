# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

welcome_msg = "Введите номер месяца: "
number = int(input(welcome_msg))
if number == 1:
    print("Январь")
elif number == 2:
    print("Февраль")
elif number == 3:
    print("Март")
elif number == 4:
    print("Апрель")
elif number == 5:
    print("Май")
elif number == 6:
    print("Июнь")
elif number == 7:
    print("Июль")
elif number == 8:
    print("Август")
elif number == 9:
    print("Сентябрь")
elif number == 10:
    print("Октябрь")
elif number == 11:
    print("Ноябрь")
elif number == 12:
    print("Декабрь")
else:
    print("Нарушено условие ввода")
