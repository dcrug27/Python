eng_1, eng_2, eng_3, eng_4, eng_5, eng_8, eng_10 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'], ['d', 'g'], ['b', 'c', 'm', 'p'], ['f', 'h', 'v', 'w', 'y'], ['k'], ['j', 'x'], ['q', 'z']
rus_1, rus_2, rus_3, rus_4, rus_5, rus_8, rus_10 = ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], ['д', 'к', 'л', 'м', 'п', 'у'], ['б', 'г', 'ё', 'ь', 'я'], ['й', 'ы'], ['ж', 'з', 'х', 'ц', 'ч'], ['ш', 'э', 'ю'], ['ф', 'щ', 'ъ']
count = 0
word = input("Введите слово: ").lower()
word_list = []

for i in word:
    word_list.append(i)
print(word_list)

for i in range(len(word)):
    if word_list[i] in rus_10:
        count += 10
    elif word_list[i] in rus_8:
        count += 8
    elif word_list[i] in rus_5:
        count += 5
    elif word_list[i] in rus_4:
        count += 4
    elif word_list[i] in rus_3:
        count += 3
    elif word_list[i] in rus_2:
        count += 2
    elif word_list[i] in rus_1:
        count += 1
    elif word_list[i] in eng_10:
        count += 10
    elif word_list[i] in eng_8:
        count += 8
    elif word_list[i] in eng_5:
        count += 5
    elif word_list[i] in eng_4:
        count += 4
    elif word_list[i] in eng_3:
        count += 3
    elif word_list[i] in eng_2:
        count += 2
    elif word_list[i] in eng_1:
        count += 1
print(count)
