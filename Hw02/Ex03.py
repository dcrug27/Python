# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter n: "))
d = 1
for i in range(n):
    d = d * 2
    if d < n:
        print(d)
