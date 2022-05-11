# Дано трехзначное число. Пользуясь только операциями с числами, вычислите сумму его цифр.
# Например: 145 -> 1 + 4 + 5 = 10
#посчитать сумму введенных цифр 1
# n = input()
# print(type(n))
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# print(getSum(n))
#посчитать сумму введенных цифр 2
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
#create sequence of strings
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
my_dict = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
print(my_dict.keys())


