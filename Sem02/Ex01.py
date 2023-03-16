# По данному целому неотрицательному n вычислите значение n!

n = int(input("Enter n: "))
fact = 1

while n > 0:
    fact = fact * n
    n -= 1
else:
    fact = 1
print(fact)
