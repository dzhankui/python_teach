# Дано трехзначное число. Пользуясь только операциями с числами, вычислите сумму его цифр.
# Например: 145 -> 1 + 4 + 5 = 10
# посчитать сумму введенных цифр 1
# n = input()
# print(type(n))
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# print(getSum(n))
# посчитать сумму введенных цифр 2
# n = int(input("Enter a number:"))
# tot = 0
# while (n > 0):
#     dig = n % 10  # остаток от деления 12345 на 10 = 5
#     tot = tot + dig  # добавляем этот остаток в total
#     n = n // 10  # целочисленное деление - число становится короче: // - тут возвращает 1234, пихаем его в n и заново
# print("The total sum of digits is:", tot)
# a = 17 % 3
# b = 7 // 3
# print(a)
# print(b)
# избавляемся от знака
# a = ['+5', '10', 'cukf']
# b = a[0].split('+', 1)[1]
# a.insert(0, b)
# # c = a.append(b)
# print(a)
# print(b)
# from emoji import emojize
# print(emojize(":thumbs_up:"))

# from geopy import GoogleV3
# place = "221b Baker Street, London"
# location = GoogleV3().geocode(place)
# print(location.address)
# print(location.location)
# even/odd:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# evens = [x for x in numbers if x % 2 == 0]
# odds = [y for y in numbers if y not in evens]
# print(evens)
# print(odds)

# welcome to the
# cities = ['London', 'Moscow', 'New York']
# def visit(city):
#     print("Welcome to the", city)
# for city in cities:
#     visit(city)
# =====================================================
# dns = {
# 'mail.ru': '94.100.180.201',
# 'geekbrains.ru': '178.248.232.209',
# 'amazon.com': '205.251.242.103'
# }
# for item in dns:
#     print(item)
# print('google.com' in dns)
#
# for key, val in dns.items():
#     print(val)
# ====================================================
# create sequence of strings
# cities = ('Paris', 'Athens', 'madrid')
# place = ['Europe', 'Angora', 'Romania']
# #create the dictionary, `my_dictionary`, using the fromkeys() method
# my_dictionary = dict.fromkeys(cities, place)
#
# print(my_dictionary)
# {'Paris': None, 'Athens': None, 'Madrid': None}
# =====================================================
# my_string = "d gAs"
# crop_string = my_string.replace(' ', '')
# print(crop_string)
# =====================================================
# def show_user(name, *args, **kwargs):
#     print(f'Пользователь {name}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')
# show_user('Иван', 'Иванов', age=25)
# ======================================================
# my_dict = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
# print(sorted(my_dict.keys()))
# ======================================================

# def split(str):
#     return [char for char in str]
#
#
# result = ''
# str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# str = "g fmnc wms bgblr rpylqjyrc gr zw fylb." \
#       "rfyrq ufyr amknsrcpq ypc dmp. \
#       bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
#       sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# str = "pythonchallenge.com/pc/def/map.html"
# for ch in str:
#     if ch == ' ' or ch == '.' or ch == "'" or ch == '(' or ch == ')' or ch == '/':
#         result += ch
#     elif ch == 'y':
#         result += 'a'
#     elif ch == 'z':
#         result += 'b'
#     else:
#         result += chr(ord(ch) + 2)
#
# print(result)
# ==================================вариант 2=======================================
# s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.  lmu ynnjw ml rfc spj."
# s = "http://www.pythonchallenge.com/pc/def/map.html"
# o = ""
# for x in s:
#     if ord('a') <= ord(x) <= ord('z'):
#         o += chr((ord(x) + 2 - ord('a')) % 26 + ord('a'))
#     else:
#         o += x
# print(o)
#
# url = "http://www.pythonchallenge.com/pcc/def/map.html"
# rslt_url = ''
# for x in s:
#
#     charCode = ord(x)
#     if charCode + 2 < ord('z'):
#         if charCode + 2 >= ord('a'):
#             charCode = ord(x) + 2
#     else:
#         charCode = charCode - 24
#
#     rslt_url += chr(charCode)
# print(rslt_url)
# ==================================================================
# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# d = {add: sub, sub: add}
# print(d[add](2, 1))
# ===========================================================================================
# print(...) #Ellipsis
# Катя узнала, что ей для сна надо XX минут.
# В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
# Помогите Кате определить, на какое время ей поставить будильник,
# чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
# На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
# MinsToSleep = int(input())
# HourLayDown = int(input())
# MinsLayDown = int(input())
#
# SetMins = (MinsToSleep + MinsLayDown) % 60 #
# SetHours = (MinsToSleep + MinsLayDown) // 60 + HourLayDown #
# print(SetHours)
# print(SetMins)

# n % 10 остаток от деления на 10
# n = n // 10  целочисленное деление (берется только целая часть от деления на число, дробная отбрасывается)
# ============================================================================================================
# x = 5
# y = 10
# print(y > x * x or 2 * x <= y and x < y)
# ===========================================================================================================
# a = True
# b = False
# print((a and b) or (not a)) and (not b)
# ===========================================================================================================
# A = int(input())
# B = int(input())
# H = int(input())
# if B >= H >= A:
#     print('Это нормально')
# elif B < H:
#     print('Пересып')
# elif H < A:
#     print('Недосып')
# ==========================================================================================================
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Високосный')
# else:
#     print('Обычный')
# =========================================================================================================
# from numpy import sqrt
#
# a = int(input())
# b = int(input())
# c = int(input())
# p = a + b + c
# S = sqrt(p * (p - a) * (p - b) * (p - c))
# print(S)
# ========================================================================================================
# from numpy import infty
# x = int(input())
# if (-15) < x <= 12 or (14 < x < 17) or (19 <= x < +infty):
#     print('True')
# else:
#     print('False')
# ========================================================================================================
# FirstDigit = float(input())
# SeconDigit = float(input())
# Operation: str = input()
# Result = 0
# if SeconDigit == 0 and (Operation == '/' or Operation == 'div' or Operation == 'mod'):
#     print('Деление на 0!')
# elif Operation == '/':
#     Result = FirstDigit / SeconDigit
#     print(Result)
# elif Operation == '*':
#     Result = FirstDigit * SeconDigit
#     print(Result)
# elif Operation == 'mod':
#     Result = FirstDigit % SeconDigit
#     print(Result)
# elif Operation == 'pow':
#     Result = FirstDigit ** SeconDigit
#     print(Result)
# elif Operation == 'div':
#     Result = FirstDigit // SeconDigit
#     print(Result)
# ===========================================================================================================
# from numpy import sqrt
#
# RoomShape = str(input())
# pi = 3.14
# if RoomShape == 'треугольник':
#     Area = 0
#     a = abs(float(input()))
#     b = abs(float(input()))
#     c = abs(float(input()))
#     HalfPerimeter = (a + b + c) / 2
#     if c >= (a + b) or b >= (a + c) or a >= (b + c):
#         print("it is an impossible shape. Screw you! There is no result!")
#     else:
#         Area = sqrt((HalfPerimeter * (HalfPerimeter - a) * (HalfPerimeter - b) * (HalfPerimeter - c)))
#         print(Area)
# elif RoomShape == 'прямоугольник':
#     a = abs(float(input()))
#     b = abs(float(input()))
#     Area = a * b
#     print(Area)
#
# elif RoomShape == 'круг':
#     r = abs(float(input()))
#     Area = pi * r ** 2
#     print(Area)
#
# else:
#     print('в названии фигуры ты ошибся')
#     ================================================================

# a = int(input())
# b = int(input())
# c = int(input())
# d = sorted([a, b, c], reverse=True)
# print(d[(len(d) - 1)])
# print(d[0])
# print(d[1])

#   ===========================================================================
# todo решить в т.ч. при помощи str, обрабатывая символы строки (изначально введенное число - строка)
# В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу,
# по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".#
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.#
# Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
# для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
# # В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

#           ========= solvation using numbers =========
# p = 'программист'
# o = 'ов'
# a = 'а'
#
# InputNumber = abs(int(input()))
# print(InputNumber // 10)
# print(InputNumber % 10)
# #    =========    программист     =========
# if InputNumber == 1 or (InputNumber % 10 == 1 and 981 >= InputNumber > 11):
#     print(InputNumber, p)
#
#
# #    =========    программиста    =========
# elif InputNumber // 100 == 0 or (1 < InputNumber % 10 < 5 and InputNumber % 11 != 0):
#     print(InputNumber, p + a)
#
# #    =========    программистов     =========
# # todo for 11, 12, 13, 14 & etc + x00
# elif InputNumber % 11 == 0 and InputNumber
#
# #  11
# InputNumber % 10 == 1
# InputNumber // 10 ==1
# # xx1
# (InputNumber % 100) % 11 == 0
# #  12
# (InputNumber % 100) % (3 and 4) == 0


# elif 1 < (InputNumber % 10) <= 6 and InputNumber // 10 == (1 or 2 or 3):
#     print(InputNumber, p + o)

#    =========    реализовать в виде вложенных условий, типа, принцип "отсева" введенного значения    =========
#  выяснить, лучшее ли это решение алгоритмически?
# if InputNumber % 100 == 0:
#     if InputNumber % 10 ==0:
#         if InputNumber % (2 or )

#   ===================     swapinGame   ======================
# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# words = input()
# wordSplit = words.split()
#
#
# def reverse(*args):
#     for word in wordSplit:
#         if len(word) >= 5:
#             wordSplit[wordSplit.index(word)] = word[::-1]
#     print(' '.join(map(str, wordSplit)))
#
#
# reverse(words)
# ===================================   Count by X  ==============================
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array (or list in Python, Haskell or Elixir).

# def count_by(x, n):
#     arr = []
#     s = 0
#     if x != 0 or n != 0:
#         for i in range(x, (x * n) + 1, x):
#             s += x
#             arr.append(s)
#
#         return arr
#     else:
#         print('ошибка! 0 вводить нельзя!')
#
#
# print(count_by(1, 10))

# =================================== Ordered Count of Characters ==============================
"""https://www.codewars.com/kata/57a6633153ba33189e000074/train/python
Input --> string. Count the number of occurrences of each character and return it
as a list of tuples in order of appearance.
For empty output return an empty list.
example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""
# =================================================
arr = ['d', 'f', 's', 'd']


def ord_count(*args):
    chars = {}
    for i in arr:
        chars[i] = chars.get(i, 0) + 1  # получаем {'d': 2, 'f': 1, 's': 1}
    print(chars)


ord_count(arr)

# ==============================================

# ============================================      ==================================================
"""Creating a list of integers:"""
# integers = list(range(10))
# print(f'* List: {integers}')
#
"""Creating a tuple of integers:"""
# numbers = tuple(integers)
# print(f'* Tuple: {numbers}')
"""Creating dictionary:"""
# items = [('zero', 0), ('one', 1), ('two', 2)]
# words = dict(items)
# print(f'* Dict: {words}')
"""element of a dictionary:"""
# print(words['zero'])
# print(words['one'])
# print(words['two'])
"""Creating a set:"""
# evens = (-2, 4, 2, 0, 2, -4, 4)
# unique_evens = set(evens)
# print(f'* Set: {unique_evens}')
# =======================================================
"""list --> to array numpy:"""
# import numpy as np
# import pandas as pd
#
# numbers = [1, 2, 3, 4, 5, 6]
# num_array = np.array(numbers)
# print(f'* Numpy Array:', num_array, '\n')
"""list --> pd Series:"""
# names = ['joe', 'pit', 'sam']
# names_series = pd.Series(names)
# print('* pd Series: \n', names_series, '\n')
"""dictionary --> to data frame:"""
# grades = {'name': names, 'grade': [99, 100, 98]}
# grades_df = pd.DataFrame(grades)
# print('* pd DataFrame:\n', grades_df)
# ====================================================
"""представления списков, словарей, множеств (отличаются лишь скобки):"""

# numbers = list(range(-3, 4))
# print(f'initial iterable {numbers}')
"""списки:"""
# [expression for item in iterable if optional_condition]:
# squares_list = [x*x for x in numbers]
# print(f'* listcomp: {squares_list}')
"""словари:"""
# {key_exp: value_expr for item in iterable if optinal_condition}:
# squares_dict = {x: x*x for x in numbers if x % 2 == 0}
# print(f'* dictcomp: {squares_dict}')
"""множества:"""
# {expression for item in iterable if optional_condition}:
# squares_set = {x*x for x in numbers}
# print(f'* setcomp: {squares_set}')
# ===================================       Generators     =====================================
'''using less memory 'cause generators aren't use it for upload all elements in'''
# squares_gen = (x*x for x in range(1000000))
# print(f'* size of Generator: {squares_gen.__sizeof__()}')
# var = 2, 3
# print(var)
#
# l = list('cde')
# l.extend('fgh')
# print(l)
# a = ['cpp', 'go', 'php', 'js', 'java']
# print(sorted(a))
# print(''.split(' '))
# ======================= подсчет числа раз встречи слов в предложении ===========================
"""Для каждого слова из введенной строки программа выводит одно целое число — количество повторов этого слова 
в тексте с учетом позиции и регистра. Числа выводятся на одной строке, через пробел."""
# my_str = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон Хьюстон у нас проблема'
# d = {}
# # print(my_str.split())
# for i in my_str.split():
#     d[i] = d.get(i, 0) + 1
#     print(d[i], end=' ')
# ====================================================
'''Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the string should be retained.'''
# def revercing(*args):
#     for i in inp:

# =====================================================================================
'''https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:
[]        -->  "no one likes this"
["Peter"] -->  "Peter likes this"
'''
# def LikeNames (*args):
#     if i in
