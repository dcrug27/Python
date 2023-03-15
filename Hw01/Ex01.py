# Найдите сумму цифр трехзначного числа.

number = input("Enter number: ")

print(f'{number} = {int(number[0]) + int(number[1]) + int(number[2])}')

# Можно сделать так 

# number = int(input("Enter number: "))

# number_1 = number // 100
# number_2 = number // 10 % 10
# number_3 = number % 10
# print(f'{number} = {number_1 + number_2 + number_3}')