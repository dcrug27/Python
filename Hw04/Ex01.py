# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Enter n: "))
m = int(input("Enter m: "))
n_list = set()
m_list = set()

for i in range(n):
    n_1 = int(input('List n: '))
    n_list.add(n_1)
for i in range(m):
    m_1 = int(input('List m '))
    m_list.add(m_1)

general_list = n_list.union(m_list)
print(general_list)