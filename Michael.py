"""Дано число n. С начала суток прошло n минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках."""
from math import sqrt

# n = int(input())  # general amount of minutes
# day = n // 1440
# n_corr = n - day*1440
# hh = n_corr // 60
# mm = n_corr % 60
#
#
# # print(day)  9876
# # print(n_corr) 5678
# print(hh)
# print(mm)
# ==================== Conditions (if/elif/else) ================================
'''Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

from math import sqrt

pi = 3.14
shape = input('please, enter a roomshape')
if shape == 'треугольник':
    a = int(input('please enter first side of a triangle'))
    b = int(input('please enter second side of a triangle'))
    c = int(input('please enter third side of a triangle'))
    p = (a + b + c) / 2
    area = sqrt(p * (a - p) * (b - p) * (c - p))
    print(p)
elif shape == 'круг':
    r = int(input('enter a radius'))
    area = pi * r ** 2
elif shape == 'прямоугольник':
    a = int(input('enter a first side size'))
    b = int(input('enter a second side size'))
    area = a * b

print('площадь', shape, "а", area, "кв.м")
