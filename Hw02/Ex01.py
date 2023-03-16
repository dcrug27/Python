# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Enter count coins: "))
coins = []
count_0 = 0
count_1 = 0
count = 0

for i in range(n):
    coin = int(input(f'coin {i} -> '))
    coins.append(coin)

for i in range(len(coins)):
    if coins[i] > 0:
        count_1 += 1
    else:
        count_0 += 1

if count_1 > count_0:
    for i in range(len(coins)):
        if coins[i] != 1:
            coins[i] = coins[1]
            count += 1
else:
    for i in range(len(coins)):
        if coins[i] == 1:
            coins[i] = coins[0]
            count += 1

print(count)