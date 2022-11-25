# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

import os
os.system('cls||clear')

length_of_list = int(
    input("Введите количество элементов последовательности (1 + 1 / n)**n : "))

user_list = []
sum_of_numbers_in_list = 0

for i in range(1, length_of_list+1):
    user_list.append(round(((1+1/i)**i), 2))
    sum_of_numbers_in_list = sum_of_numbers_in_list + ((1+1/i)**i)

print(user_list)
print(round(sum_of_numbers_in_list, 3))
