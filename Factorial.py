# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('cls||clear')

user_number = int(input("Введите число для получения факториала: "))
factorial = 1

for i in range(1, user_number):
    factorial = factorial*i
    print(f"{factorial}", end=", ")

print(factorial*user_number)
