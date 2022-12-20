# print('hello, what is your name?')
# name = input()
# print('hello '+name+', how old are you')
# age = int(input())
# age = age + 1
# print('you will be 20 in ', age, ' years.')

# LISTS     0     1      2       |---------------3----------|
# lst = ['Elias', 11, 31.877465, [12, 'закуска', 'vodka', 14]]

'''
Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
'''

# from math import sqrt
#
#
# pi = 3.14
# # print(math.tan(30))
# RoomShape = input('Please, enter a shape of the room')
# if RoomShape == 'треугольник':
#     hp = 0
#     while hp <= 0:  # (a + b) <= c or (b + c) <= a or (c + a) <= b:
#
#         a = int(input('please, enter first side size of a triange'))
#         b = int(input('please, enter second side size of a triange'))
#         c = int(input('please, enter third side size of a triange'))
#         if (a + b) <= c or (b + c) <= a or (c + a) <= b:
#             print('То, что ты ввел - это бред! Введи заново!')
#         else:
#             hp = (a + b + c) / 2  # half perimeter
#             area = sqrt(hp * (hp - a) * (hp - b) * (hp - c))
#
# elif RoomShape == 'прямоугольник':
#     while True:
#         a = int(input('please, enter first size of a rectangle'))
#         b = int(input('please, enter second size of a rectangle'))
#         if a <= 0 or b <= 0:
#             print('Неее, посмотри, че ты ввел!')
#         else:
#             area = a * b
#             break
# elif RoomShape == 'круг':
#     r = int(input('please, enter a radius of the room'))
#     area = pi * r ** 2
# print('Room area is', area)
# =======================================================================================


# x = input('say hello --> ')
# def hello():
#     return x
# print('hello,', hello())
# def add(x, y):
#     return x - y
#
#
# print(add(1, 10))
# def func(*args):
#     return sum(args)
#
#
# print(func(1, 2, 3))
# def func(a, b, c):
#     return a - (b + c)
#
#
# print(func(c=int(input('enter c --> ')), b=int(input('enter b --> ')), a=int(input('enter a --> '))))
# def func(**kwargs): #inthis case the function returns a dictionary of a variables as keys and values as values
#     return kwargs
#
#
# print(func(a=1, b=2))


# def func(a=1, b=2, c=3):
#     return a + b + c
'''
1. Написать проверку введенных значений для случаев, когда вводят букв и/или символы.
2. Переписать программу про страну Малевию с использованием функций. Функции должны вычислять площади.
'''










# ====================================================================
'''Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
первое число, второе число и операцию, после чего применяет операцию к введённым числам 
("первое число" "операция" "второе число") и выводит результат на экран.'''
# ==============================================================================
'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.'''