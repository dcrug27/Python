# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

ticket = input("Enter ticket number: ")


if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
    print("Yes")
else:
    print("No")

# Можно сделать так

# ticket = int(input("Enter ticket number: "))

# ticket_1 = ticket // 100000
# ticket_2 = ticket // 10000 % 10
# ticket_3 = ticket // 1000 % 10
# ticket_4 = ticket // 100 % 10
# ticket_5 = ticket // 10 % 10
# ticket_6 = ticket % 10

# if (ticket_1 + ticket_2 + ticket_3) == (ticket_4 + ticket_5 + ticket_6):
#     print("Yes")
# else:
#     print("No")