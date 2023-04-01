import random
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

rand_list=[]

for i in range(20):
    rand_list.append(random.randint(-50,50))
print(rand_list)

min_number = int(input("Enter min number: "))
max_number = int(input("Enter max number: "))

for i in range(len(rand_list)):
    if min_number <= rand_list[i] <= max_number:
        print(i)