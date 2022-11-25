# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random
import os

os.system('cls||clear')

user_number = int(input("Введите количество элементов списка: "))
user_list = list(range(user_number))

print(user_list)

for i in range(0, len(user_list)**2):
    a = random.randint(0, len(user_list)-1)
    b = random.randint(0, len(user_list)-1)
    user_list[a], user_list[b] = user_list[b], user_list[a]


print(user_list)
