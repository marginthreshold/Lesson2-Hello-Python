# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

import os
os.system('cls||clear')

user_number = input('Введите любое число:')
sum_of_digits = 0


for i in range(len(user_number)):
    if user_number[i].isdigit() == 1:
        sum_of_digits += int(user_number[i])

print(f'Сумма всех цифр равна: {sum_of_digits}')
