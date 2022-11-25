# 4 Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.

import os
os.system('cls||clear')

user_number = int(input("Введите число для создания списка: "))
user_list = list(range(-user_number, user_number+1))
product_of_numbers_in_list = 1

print(user_list)


for i in range(user_number*2+1):
    product_continue = input("Хотите продолжать дальше умножать?: y/n\n")
    if product_continue == "n":
        break
    else:
        element_number = int(
            input(f"Введите номер элемента от {1} до {user_number*2+1}: "))
        product_of_numbers_in_list = product_of_numbers_in_list * \
            user_list[element_number-1]


print(f"Произведение элементов равно: {product_of_numbers_in_list}")
