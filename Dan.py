"""Есть корзина с яблоками (basket). К нам в гости пришло несколько человек (people).
Требуется определить, сколько целых яблок достанется каждому (count), ведь ножа-то у нас нет.
А сколько яблок останется после гостей лежать в корзине? """
# basket = int(input())       #шпаргалка
# people = int(input())
# count = basket // people    #целая часть от деления числа яблок на число людей
# print(count)                #вывод в консоль информации
# count = basket % people     #остаток от деления числа яблок на число людей (сколько яблок останется в корзине)
# print(count)                #вывод в консоль числа яблок в корзине
# =======================================================================================
'''Дано число n. С начала суток прошло n минут. Определите, 
сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
Учтите, что число n может быть больше, чем количество минут в сутках.'''

# n = int(input('how much minutes?'))
# d = n // 1440   #сутки - это 1440 минут, значит, в n содержится (n // 1440) дней
# print(d)
# n_corr = n - (d * 1440)
# hh = n_corr // 60       #часы
# mm = n_corr - hh * 60   #минуты
# print(hh)
# print(mm)
# =========================================================================================
"""В школе решили набрать три новых математических класса. 
Так как занятия по математике у них проходят в одно и то же время, 
было решено выделить кабинет для каждого класса и купить в них новые парты. 
За каждой партой может сидеть не больше двух учеников. 
Известно количество учащихся в каждом из трёх классов. 
Сколько всего нужно закупить парт чтобы их хватило на всех учеников? 
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов."""

# a = int(input('class A people amount'))
# b = int(input('class B people amount'))
# c = int(input('class C people amount'))
# d = a + b + c
# print(d, 'total amount of people')
# print(d // 2 + d % 2)
# ===========================================   шнурки  ========================================
'''Обувная фабрика собирается начать выпуск элитной модели ботинок. 
Дырочки для шнуровки будут расположены в два ряда, расстояние между рядами равно a, 
а расстояние между дырочками в ряду b. 
Количество дырочек в каждом ряду равно N. Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, 
наверх, по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного 
конца шнурка должна быть l. Какова должна быть длина шнурка для этих ботинок?'''
# a = int(input('расстояние между рядами равно:'))
# b = int(input('расстояние между дырочками в ряду:'))
# l = int(input('длина свободного конца шнурка:'))
# N = int(input('Количество дырочек в каждом ряду:'))
# x = (b * (N - 1) * 2) + ((a * 2) * N - a) + l * 2
# print(x)
# ===============================   Conditions I    =============================================
'''Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

# from numpy import sqrt
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

# дописать проверку для других форм комнаты
# zen of python
# ====================================  Conditions  II  ========================================
# text = 'Жители страны Малевии часто экспериментируют с планировкой комнат'
# print(text[-12::-1]) #start stop step
# print(text[::-1])