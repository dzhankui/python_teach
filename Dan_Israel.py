# http://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/apples/
'''Есть корзина с яблоками (basket). К нам в гости пришло несколько человек (people).
Требуется определить, сколько целых яблок достанется каждому (count), ведь ножа-то у нас нет.
А сколько яблок останется после гостей лежать в корзине?'''
# apple = int(input('Input apples amount'))    # количество яблок
# people = int(input('Input amount of people'))    #количество людей
# print('Каждый получит по', apple // people, 'яблок')  # сколько яблок каждому
# print('In the basket',...,'apples')
# ==============================================================================
'''Дано число n. С начала суток прошло n минут. Определите, 
сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
Учтите, что число n может быть больше, чем количество минут в сутках.'''

# n = int(input())
# n_corr = n % 1440
# hh = n_corr // 60
# mm = n_corr % 60
# print(hh)
# print(mm)
# =============================================================================
'''В школе решили набрать три новых математических класса. 
Так как занятия по математике у них проходят в одно и то же время, было решено выделить 
кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников. 
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на 
всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.'''

# first_class = int(input('please enter amount of students in 1-st class'))
# second_class = int(input('please enter amount of students in 2-nd class'))
# third_class = int(input('please enter amount of students in 3-rd class'))
# tables = (first_class + second_class + third_class) // 2 + (first_class + second_class + third_class) % 2
# print(tables)
# =============================================================================
'''Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

# from numpy import sqrt
#
#
# RoomShape = input('Please, enter a room shape type')
# if RoomShape == 'rectangle':
#     a = int(input('Please, enter first side size'))
#     b = int(input('Please, enter second side size'))
#     Area = a * b
# if RoomShape == 'circle':
#     pi = 3.14
#     r = int(input('Please, enter a radius'))
#     Area = pi * r ** 2
# if RoomShape == 'triangle':
#     a = int(input('Please, enter first side size'))
#     b = int(input('Please, enter second side size'))
#     c = int(input('Please, enter second side size'))
# # halfperimeter = hp
#     hp = (a + b + c) / 2
#     Area = sqrt(hp * (hp - a) * (hp - b) * (hp - c))
# print(Area)
#
# =======================================================
'''вывести на экран 100 строк со значением от 1 до 100'''
# for number in range(0, 100, 5): #start, stop, step
#     print(number)
#  доделать 1, 5, 10 ... 100

# 0 1 2 3 4 так считает компьютер (индексы)
# 1 2 3 4 5 так считают люди

# ===============================
#           01234567
# for p in 'Zeppelin':
#     print(p, 'Yankee')
# ===============================
# list 0  1     2         3    indexes
# lst = [2, 4, 'hello', [1, 2, 3]]
# print(lst[3])
# print(lst[0])
# x = 1
# while x <= 10:
#     print(x)
#     x += 5  # x = x + 1
#
# ==========================

# loops while, break, continue

# for in else elif
# lst1 = [2, 4, 'hello', [1, 2, 3]]
# txt = 'Жители страны Малевии часто экспериментируют'

# lst = range(1, 100)          #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in lst:
#     if i % 2 == 0:
#         print(i)
# for i in txt:
#     print(i)
# for i in txt:
#     if i == 'и':
#         print(i)
# =================================================================
'''
GC-состав является важной характеристикой геномных последовательностей 
и определяется как процентное соотношение суммы всех гуанинов и цитозинов 
к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов 
G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и C 
равно 4/10*100 = 40.0 где 4 - это количество символов G и C, а 10 - это длина строки.
'''
dna = input('please input a dna sequence')
dna = dna.lower()  # explanation
counter = 0
for i in dna:
    if i == 'g' or i == 'c':
        counter += 1  # increase by 1
percent = (counter / len(dna)) * 100
print(percent, '%')

# GbvfCvbggvbgGc
# kjbjgoovgcggcbgcdxcg
