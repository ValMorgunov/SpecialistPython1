# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    len_ticket_number = 6
    ticket_number = str(ticket_number).ljust(len_ticket_number, "0")
    return int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[3]) + int(
        ticket_number[4]) + int(ticket_number[5])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(4367510))
