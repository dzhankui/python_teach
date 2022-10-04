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


# =================================== Ordered Count of Characters ==============================
"""https://www.codewars.com/kata/57a6633153ba33189e000074/train/python
Input --> string. Count the number of occurrences of each character and return it
as a list of tuples in order of appearance.
For empty output return an empty list.
example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""
#
# inp = input()
#
#
# def ordered_count(*args):
#     chars = {}
#     my_list = []
#     for i in inp:
#         chars[i] = chars.get(i, 0) + 1  # получаем {'d': 2, 'f': 1, 's': 1}
#     for i in chars:
#
#     print(my_list)
#
#
# ordered_count(inp)
# ====================================  алгоритмы и структура данных  ==========================================
"""Вводится любое число. 
Выяснить, есть ли среди чисел (т.е. в промежутке от 0 до введенного числа) кратные 10"""
# Yep = False
# inp = int(input())
# for i in range(inp-9):
#     Yep = (i % 10 == 0 or Yep)
#
# print(Yep, amount10)
#
# ===================================
"""Вводится любое трехзначное число. 
Найти, посчитать, сколько в промежутке от 0 до этого числа чисел, кратных 10"""
# inp = int(input())
# amount10 = 0
# for i in range(inp-9):
#     if i % 10 == 0:
#         amount10 += 1
#
# print(amount10)
# =================================================
'''дан список, найти из списка 2 числа, в сумме дающие k'''
# k = 7
# arr = []
# pop_arr = []
# arr = range(6)
# # rev_arr = reversed(arr)
# print(range(6))
# print(reversed(arr))
# for i in range(0, len(arr)):
#     if (arr[i] + rev_arr[i]) == k or arr[i] + rev_arr[i]) or :
#         pop_arr.append(arr[i])
#         pop_arr.append(arr[i + 1])
# print(pop_arr)
# ================  Make a simple plot  ================================
# https://pybit.es/articles/terminal-plotting-with-plotext/
from collections import Counter
from datetime import date

from dateutil.parser import parse
import plotext as plt
import requests

#
# API_URL = "https://codechalleng.es/api/articles/"
# START_YEAR = 2017
# THIS_YEAR = date.today().year
# THIS_MONTH = date.today().month
# MONTH_RANGE = range(1, 13)
#
#
# def _create_yymm_range():
#     for year in range(START_YEAR, THIS_YEAR + 1):
#         for month in MONTH_RANGE:
#             yield f"{year}-{str(month).zfill(2)}"
#             if year == THIS_YEAR and month == THIS_MONTH:
#                 break
#
#
# def get_articles_per_month(url=API_URL):
#     ym_range = _create_yymm_range()
#     cnt = Counter({ym: 0 for ym in ym_range})
#     data = requests.get(API_URL)
#     for row in data.json():
#         dt = parse(row["publish_date"])
#         if dt.year < START_YEAR:
#             continue
#         ym = dt.strftime("%Y-%m")
#         cnt[ym] += 1
#     return cnt
#
#
# def show_plot(data):
#     labels, values = zip(*data.items())
#     plt.bar(labels, values)
#     plt.title("Pybites articles published per month")
#     plt.show()
#
#
# if __name__ == "__main__":
#     data = get_articles_per_month()
#     show_plot(data)
# ============================================

# today = input("what day is it today?")
# x = "Yep!" if today == "thursday" else "Nope"
# print(x)

# choice = input("кетчуп или майонез: ")
# price = 10 if choice == "кетчуп" else 12
# print(price)
# =================================================
# random_names = ["Peter", "Ivan", "Mark", "Maksim", "Alex", "Jacob", "Abdula", "John", "Sinji"]

# m_names = []
# for name in random_names:
#     if name[0] == "J":
#         m_names.append(name)
# print(m_names)
# m_names = []
# for i, name in enumerate(random_names):
#     if name[0] != "M":
#         random_names.pop(i)
#         m_names.append(name)
#     print(random_names)
# print(m_names)
# =============================================
# def custom_sum(nums):
#     s = 0
#     for n in nums:
#         s += n
#     return s
#
#
# result = custom_sum([65, 23, 111, 1000, 7])
#
# print(result)
# ============================================
# nums = [1000, 237, 146, 90, 6]
# b = [num-7 for num in nums]
# print(b)
# # ==========================================
# numbers = [1, 2, 3, 4, 5]
# numbers_sqrt = []
# numbers_sqrt = [i**2 for i in numbers]
# for i in numbers:
#     numbers_sqrt.append(i**2)
# print(numbers_sqrt)
# =====================     еще немного о генераторах    =======================
# nums = [1000, 237,146, 90, 6]
# a = [num-7 for num in nums] # это генератор списка
# b = (num-7 for num in nums) # а здесь просто генератор
# c = list(range(10))
# print(a)
# print(b)
# print(c)
# ============================================================================
# class Dog:
#     age = 0
#     name = ""
# mumu = Dog()
# mumu.age = 10
# mumu.name = "Мума"
# print(mumu.age)
# print(mumu.name)
# ==============================================
# goofy = Dog()
# sharik = Dog()
# hatico = Dog()
# goofy.name = "Goofy"
# sharik.name = "ШариГ"
# hatico.name = "ハチ公"
# print(Dog.name is hatico.name)
# your_dog = Dog()
# print(Dog.name is your_dog.name)
# ===================    Clases    =============================
# class Human:
#     age = 0
#     name = ""
#     gender = "male"
#
# class Driver:
#     crushes = 0
#     drivingPeriod = 0
#     name = ""
#
# class ZigaNut:
#     putin = "god"
#     russia = "good"
#     money = 0
#
# class Lier:
#     lie = True
#     truth = False
#     always = True
#
# class Coach:
#     KickAss = True
#     EatDonat = True
#     Fat = False
#     Weight = 100
# ==========================================
# class Fly:
#
#     def kaka():
#         print("срёт на ручки кухни")
#
#
# SratayaMukha = Fly()
# # SratayaMukha.kaka() #working with kaka(self)
# Fly.kaka()  # working with kaka()
# ====================================================
# class Bird:
#
#     def fly(self):
#         self.fly_text = "текст, доступный только объекту"
#         print("летит")
#
#
# karasu = Bird()
# karasu.fly()
# print(karasu.fly_text)
# print(Bird.fly_text) # вызовет ошибку
# class Bird:
# =====================================================================
#     def __init__(self): # до и после слова init ставим 2 прочерка
#         self.text = "текст, доступный только объекту"
#
#     def fly(self):
#
#         print("летит")
#
#
# karasu = Bird() # вызов __init__ происходит в этот момент
#
# print(karasu.text)
# ===================================================================
# class User:
#
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def __str__(self):
#         return self.name
#
#     def __int__(self):
#         return self.money
#
#
# user = User("Марк", 420)
# print(user)
# print(int(user))
# =================================================
# class Person:
#
#     def __init__(self, person_name, person_age):
#         self.name = person_name
#         self.age = person_age
#
#     def __str__(self):
#         return 'Person name is {self.name} and age is {self.age}'
#
#
# p = Person('Andrew', 24)
# # print(p.__str__())
# ====================================   API JSON --> DICT ===================================
# import requests
#
# url = "https://api.exchangerate.host/latest"
# response = requests.get(url)
# data = response.json()
# a = data.get('rates')
# b = a.get('RUB')
# print(b)
# print(data)
# ==================================== 1-string calculator ===================================
# print(eval(input(': ')))
#   ================================= Beauty color hexagon ================================
# import turtle
#
#
# t = turtle.Pen()
# turtle.speed(100)
# turtle.bgcolor('white')
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'magenta']
# for i in range(360):
#     t.pencolor(colors[i // 150])
#     t.width(i // 100 + 1)
#     t.forward(i)
#     t.left(60)
# ==========================================    window with a button  ================================================
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.geometry('400x400')
# mybutton = ttk.Button(root, text='Hello, world!')
# mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)
# root.mainloop()
# ====================================  dict comprehensions   ================================================================
'''Идея такова, что есть 2 списка с названиями стран и названиями городов.
Позиции городов в одном списке соответствуют позициям стран в другом.
Из двух списков можно получить словарь, если в цикле указать, что для каждой пары "ключ:значение"
мы итерируемся параллельно (при помощи функции zip) по двум спискам'''
# cities = ['London', 'New York', 'Tokyo', 'Cambridge', 'Oxford']
# countries = ['UK', 'US', 'Japan', 'UK', 'UK']
# uk_cities = {city: country for city, country in zip(cities, countries) if country == 'US'}
# print(uk_cities)  # {'London': 'UK', 'Cambridge': 'UK', 'Oxford': 'UK'}
# ======================
# print('=======================')
"""Здесь показан способ создания одного словаря из двух методом добавления ** и методом union """
# **:
# cities_1 = {'New York City': 'US', 'Los Angeles': 'US'}
# cities_2 = {'London': 'UK', 'Birmingham': 'UK'}
# cities = {**cities_1, **cities_2}
# print(cities)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}
# union(|):
# cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
# cities_uk = {'London': 'UK', 'Birmingham': 'UK'}
#
# cities = cities_us|cities_uk
# print(cities)   # {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}