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
# =============================================================================================
'''Каждое имя из 4 букв нужно реверсировать (записать наоборот)'''
# lst = ['Матвей', 'ашаМ', 'Полина', 'Арина', 'ашаП']
# lst2 = []
# for elem in lst:
#     if len(elem) == 4:
#         lst2.append(elem[::-1])
# print(lst2)
# ===================================================================
'''Каждое второе слово реверсировать (запистаь наоборот)'''
#
txt = 'Дано число n. С начала суток прошло n минут.\
Определите, сколько часов и минут будут показывать электронные часы в этот момент.\
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).\ ' \
      'Учтите, что число n может быть больше, чем количество минут в сутках.'
# x = 0
# while x <= 100:
#     print(x)
#     x += 1

# LISTS  0     1      2      ---------------3-------------
# lst = ['Dan', 11, 31.877465, [12, 'закуска', 'vodka', 14]]
# print(lst[0])
# print(lst[3][2])
# lst[3].append('beer')
# # print(lst)
# # print(len(lst))
# # print(lst.clear())
# lst_copy = lst.copy()
# print(lst_copy)
# print(lst_copy[3])
# print(lst_copy.pop(3))
# print(lst_copy)
# print(lst_copy[3].index('закуска'))
# lst1 = [0, 1, 2, [0, 1, [0, 1, 2, 3, 'k'], 3, 4]]
# print(lst1[3][2][4])
# lst_copy.insert(3, 'martini')
# print(lst_copy)
# my_list = ['Матвей', 'ашаМ', 'Полина', 'Арина', 'ашаП']
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list[1:3:])
# ==============    strings, tuples, list    ============
# students += ['Olga']
# print(students)
# students += 'Olga'
# print(students)
# ---------------        exersice
'''
GC-состав является важной характеристикой геномных последовательностей 
и определяется как процентное соотношение суммы всех гуанинов и цитозинов 
к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов 
G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и C 
равно 4/10*100 = 40.0 где 4 - это количество символов G и C, а 10 - это длина строки.
'''
# dna = input('enter a dna sequence:')  # bla-bla-bla
# # lower all symbols in dna:
# dna = dna.lower()
# print(dna)
# counterGC = 0
# # fillin' up GC with sum of c & g:
# for element in dna:
#     if element == 'g' or element == 'c':
#         counterGC += 1
# print(counterGC / len(dna) * 100)
# print(type(counterGC / len(dna) * 100))
# ijhjgghCccGfFFvFrssdrjhvjgfxsztwdsccccg
# ===================================================================================
# students = ["мАША", "коля", "СаШа", "дАшА"]
# забыла: петя, Игорь
# составить правильный список: все имена с большой буквы (остальные буквы имени - маленькие)
# добавить потеряшек с именами, записанными по правилам
# упорядочить всех по алфавиту

# while True:
#
#     forgotten = input("Введи одну потеряшку и нажми ввод: ")
#     students.append(forgotten.strip())
#     x = int(input('input 1 and press enter to continue, enter 0 and press enter to finish enter the students'))
#     if x == 1:
#         continue
#     elif x == 0:
#         break
# for i in range(len(students)):
#     students[i] = students[i].title()
# students.sort()
# print(students)
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)
# ======================================== for loop training ==========================
'''Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. 
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
Числа a, b, c и d являются натуральными и не превосходят 10, a<=b, c<=d.'''
# a = int(input('a = '))  #
# b = int(input('b = '))  #
# c = int(input('c = '))  #
# d = int(input('d = '))  #
# list_1 = []
# list_2 = []
# list_3 = []
# for i in range(a, b + 1):
#     list_1.append(i)
# for i in range(c, d + 1):
#     list_2.append(i)
# for i in range(len(list_1)):
#     for j in range(len(list_2)):
#         list_3.append(list_1[i] * list_2[j])
#
# print(list_3)
# if i = i-1:
# next row
# print(list_3[:len:])


# Денис выполняет программу самостоятельно
# добавить проверку введенных данных на условия a<=b, c<=d
a = int(input('enter a first digit -->'))
b = int(input('enter a second digit -->'))
c = int(input('enter a third digit -->'))
d = int(input('enter a fourth digit -->'))
# list_of_results = [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6],
#     [4, 5, 6, 7]
# ]
# example:
# [   1  2  3  4] - x
# [1  1  2  3  4]
# [2  2  4  6  8]
# [3  3  6  9  12]
# [4  4  8  12 16]
#  y

# list_of_results.clear()
# 1 заполнить значениями (результатами умножения)
# 2 print it all row by row
# 3 строки соответствуют интервалу a-b, столбцы соответствуют интервалу c-d
# # for i in range(len(list_of_results)):
#     print(list_of_results[i])
#  there is solvation is only for the square things, where len(lst) = len(lst2)
list_of_results = []
tmp = []
lst = [] # - row
for i in range(a, b+1): #filling lst with numbers a to b
    lst.append(i)
lst2 = [] # - column
for i in range(c, d+1): #filling lst2 with numbers c to d
    lst2.append(i)
for i in range(len(lst)):
    tmp.append(lst[i] * lst2[i]) #multiply lst digits by lst2 digits
    list_of_results.append(tmp)
#  print list_of_results (list by list)
for i in list_of_results:
    print(i)
# =========================================================================
# next approach must be for the non-square tasks i.e. when len(lst) != len(lst)
# example: a,b = 2-4 c,d = 1-5
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# ---------------or---------------
# [2, 3, 4]
# [4, 6, 8]
# [6, 9, 12]
# [8, 12, 16]
# [10, 15, 20]