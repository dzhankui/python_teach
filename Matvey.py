"""Гоша придумал новый способ хранения текстов.
Один текст он хранит в двух документах. В одном — каждый третий символ
(они записаны слитно), а в другом — все остальные.
Дана строка. Выведи часть текста в том виде, как она хранится у Гоши в первом документе: каждый третий символ строки."""
#
#
# text = 'Один текст он хранит в двух документах. В одном — каждый третий символ'
# third = ''
#
# text = text.replace(' ', '')
# for i in range(2, len(text), 3):
#     third += text[i]
#
# print(third)
#
# for i in range(0, (len(third))):
#     if third[i] in text:
#         text = text.replace(third[i], '')
#
# print(text)
# =====================================================================================
'''n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? 
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).'''
# basket = int(input())
# people = int(input())
# print(basket // people)
# print(basket % people)
# ====================================================================================
'''Дано число n. С начала суток прошло n минут. 
Определите, сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
Учтите, что число n может быть больше, чем количество минут в сутках.'''
# n = int(input())            # day = 1440
# day = n // 1440             # how much days in inputed n
# n_corr = n - day * 1440     # corrected n in minutes
# hh = n_corr // 60
# # mm = n_corr // 60
# mm = n_corr - (hh * 60)
# print(hh)
# print(mm)
# =============================   Conditions  =======================================================
'''Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, 
на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.'''

# from numpy import sqrt
#
# RoomShape = input('введите форму комнаты')
# pi = 3.14
# while True:
#     if RoomShape == 'треугольник':
#         a = int(input())
#         b = int(input())
#         c = int(input())
#         HalfPerimeter = (a + b + c) / 2
#         Area = sqrt(HalfPerimeter * (HalfPerimeter - a) * (HalfPerimeter - b) * (HalfPerimeter - c))
#         print('площадь комнаты =', Area)
#         break
#     elif RoomShape == 'прямоугольник':
#         a = int(input())
#         b = int(input())
#         Area = a * b
#         print('площадь комнаты =', Area)
#     elif RoomShape == 'круг':
#         r = int(input('радиус?'))
#         Area = pi * r ** 2
#         print('площадь комнаты', Area)
#     else:
#         print('что за дичь ты там ввел?')

# ===================================================
# работа с текстом
# loops, generator range
# list
# 0123
# 1234
# x = 0
# while x <= 10:
#     print('Hello!')
#     x += 1 #x = x + 1
# range
'''нужны числа от 1 до 100'''
# for number in range(1, 101, 4):    #sss = start, stop, step
#     print(number)
# x = 0
# while x <= 10:
#     x += 5
#     print(x)

# text-list:
#        01234567
# txt = 'Zeppelin'
# for i in txt:
#     print(i)
# написать каждую букву дважды
# написать слово столько раз, сколько букв в слове

#        0  1  2  3        4    |----5 water---|
# lst = [1, 3, 5, 5.5, 'Hello', [1, 'vodka', 3]]
# print(lst)
# lst[5].append('beer')
# print(lst)
# list - sequence of objects
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst1 = range(1, 10)
# print(type(lst))
# print(type(lst1))

# task: 1-1000 #отдельно 10 в лист и отдельно 15 в лист
# lst10 = []
# lst15 = []
# for i in range(1001):
#     if i % 10 == 0:
#         lst10.append(i)
#     elif i % 15 == 0:
#         lst15.append(i)
# print(lst10)
# print(lst15)
# =======================================================
'''
GC-состав является важной характеристикой геномных последовательностей 
и определяется как процентное соотношение суммы всех гуанинов и цитозинов 
к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов 
G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и C 
равно 4/10*100 = 40.0 где 4 - это количество символов G и C, а 10 - это длина строки.
'''
# dna = input('input a sequence')
# c = 0
# dna = dna.lower()
# for i in dna:
#     if i == 'g' or i == 'c':
#         c += 1
# print(c/len(dna) * 100)

# knkjHBUYGUBVGvgbgcbc

# ========================================================================
# '''записать наоборот (reverse) все слова длиной 5 и более букв'''
# txt = 'и на селе паром бьёт вереск птицу сереневенько'  # immutable
# txt = txt.split()  # txt --> list
# a = ''
# for word in txt:  # for each word in list
#     if len(word) >= 5:  # if it's length >= 5
#         txt[txt.index(word)] = word[::-1]  # = txt[3]
# print(txt)
# a = ' '.join(txt)
# print(a)

#        0  1  2  3        4    |----5 water---|
# lst = [1, 3, 5, 5.5, 'Hello', [1, 'vodka', 3]]
# lst[4]
# lst[5][1]
# x = 'параллелепипед'
# x = [1, 2, 3, 4, 5]
# i = reversed([1, 2, 3, 4, 5])
# print(i)
# x.reverse()
# print(x)
# x = x[::-1]
'''
Функция в python - объект, принимающий аргументы и возвращающий значение. 
Обычно функция определяется с помощью инструкции def.
'''


# x = input('say hello --> ')
# def hello():
#     return x
# print(hello())
# def add(x, y):
#     return x - y
#
#
# print(add(1, 10))

# def func(*args):
#     return sum(args)
#
#
# print(func(1, 2, 3, 4))
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
# =================================09.12.2022============================
'''Самостоятельная работа с ментором: переписать задачу про Малевию с использованием функций'''
# finish and test the program
