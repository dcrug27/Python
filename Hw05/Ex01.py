# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return (1)
    elif b == 1:
        return(a)
    else:
        return(a * degree(a, b - 1))

a = int(input("Enter number: "))
b = int(input("Enter degree: "))
print(degree(a, b))