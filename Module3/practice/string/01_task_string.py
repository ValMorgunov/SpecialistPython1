# Для регистрации на сайте, пользователи часто вводят Имя и Фамилию с маленькой буквы.
# Напишите мини-программу, которая будет запрашивать у пользователя имя и фамилию
# и заменять первые буквы буквами в верхнем регистре.
# Измененные данные(имя и фамилию) вывести на экран.

name = input("Имя: ")
surname = input("Фамилия: ")
name=name[0].upper()+name[1:]
surname=surname[0].upper()+surname[1:]

print(name, surname)
