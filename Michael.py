"""Дано число n. С начала суток прошло n минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках."""
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
# ============================================================================
'''Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

# ==================== Conditions (if/elif/else) ================================
x = int(input('кратно ли двум?'))
if (x % 2) == 0 and x != 24 and x < 28:
    print('да')
else:
    print('нет')