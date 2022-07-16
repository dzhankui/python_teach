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
# # str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# str = "g fmnc wms bgblr rpylqjyrc gr zw fylb." \
#       "rfyrq ufyr amknsrcpq ypc dmp. \
#       bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
#       sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# # str = "pythonchallenge.com/pc/def/map.html"
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
from numpy import sqrt

RoomShape = str(input())
pi = 3.14
if RoomShape == 'треугольник':
    Area = 0
    a = abs(float(input()))
    b = abs(float(input()))
    c = abs(float(input()))
    HalfPerimeter = (a + b + c) / 2
    if c >= (a + b) or b >= (a + c) or a >= (b + c):
        print("it is an impossible shape. Screw you! There is no result!")
    else:
        Area = sqrt((HalfPerimeter * (HalfPerimeter - a) * (HalfPerimeter - b) * (HalfPerimeter - c)))
        print(Area)
elif RoomShape == 'прямоугольник':
    a = abs(float(input()))
    b = abs(float(input()))
    Area = a * b
    print(Area)

elif RoomShape == 'круг':
    r = abs(float(input()))
    Area = pi * r ** 2
    print(Area)

else:
    print('в названии фигуры ты ошибся')
