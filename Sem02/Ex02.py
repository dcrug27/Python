# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

n = int(input("Enter n: "))
fib1, fib2, count = 0, 1, 2

while fib2 < n:
    fib1, fib2 = fib2, fib1 + fib2
    count += 1

print(count) if fib2 == n else print(-1)