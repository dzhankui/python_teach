'''
Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
'''

# from math import sqrt
#
# room_shape = input("please enter room shape")
# room_area = 0
# p = 3.14
# if room_shape == "rectangle":
#     FirstSide = int(input("please enter a size side"))
#     second_side = int(input("please enter b size side"))
#     room_area = FirstSide * second_side
# elif room_shape == "triangle":
#     while True:
#         first_side = int(input("please enter first_side size side --> "))
#         second_side = int(input("please enter second_side size side --> "))
#         third_side = int(input("please enter third_side size side --> "))
#         if first_side >= (second_side + third_side) or second_side >= (first_side + third_side) or third_side >= (second_side + first_side):
#             print("incorrect triangle.please enter new triangle")
#         else:
#             hp = (first_side + second_side + third_side) / 2  # HalF perimeter
#             room_area = sqrt(hp * (hp - first_side) * (hp - second_side) * (hp - third_side))
#             break
# elif room_shape == "circle":
#     radius = int(input("please enter a radius"))
#     room_area = p * radius ** 2
# print(room_area)
# =============================================================================================================================
'''Functions'''
# def michael(a, b, c):
#      return (a + b) / c
# #
# #
# print(michael(1000,2000,3))
# print(michael(int(input()), int(input()), int(input())))
'''
1. Написать проверку введенных значений для circle и для rectangle.
2. Переписать программу про страну Малевию с использованием функций. Функции должны вычислять площади.
'''
'''
Функция в python - объект, принимающий аргументы и возвращающий значение. 
Обычно функция определяется с помощью инструкции def.
'''

# from math import sqrt
#
# room_shape = input("please enter room shape")
# room_area = 0
# p = 3.14
# if room_shape == "rectangle":
#     FirstSide = int(input("please enter a size side"))
#     second_side = int(input("please enter b size side"))
#     room_area = FirstSide * second_side
# elif room_shape == "triangle":
#     while True:
#         first_side = int(input("please enter first_side size side --> "))
#         second_side = int(input("please enter second_side size side --> "))
#         third_side = int(input("please enter third_side size side --> "))
#         if first_side >= (second_side + third_side) or second_side >= (first_side + third_side) or third_side >= (second_side + first_side):
#             print("incorrect triangle.please enter new triangle")
#         else:
#             hp = (first_side + second_side + third_side) / 2  # HalF perimeter
#             room_area = sqrt(hp * (hp - first_side) * (hp - second_side) * (hp - third_side))
#             break
# elif room_shape == "circle":
#     radius = int(input("please enter a radius"))
#     room_area = p * radius ** 2
# print(room_area)
# =======================================================================================================
'''
Функция в python - объект, принимающий аргументы и возвращающий значение. 
Обычно функция определяется с помощью инструкции def.
'''

# x = input('say hello --> ')
# def hello():
#     return x
# print('hello,', hello())
# def add(x, y):
#     return x - y
#
#
# print(add(1, 10))
# def func(*args):
#     return sum(args)
#
#
# print(func(1, 2, 3))
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
'''
1. Исправить и/или дописать программу про Малевию
2. Решить задачу:
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.
'''

# ====================================================================================
#        0  1  2  3        4    |---5 secret---|
# lst = [1, 3, 5, 5.5, 'Hello', [1, 'vodka', 3]]

# lst=[]
# for i in range(101):
#     lst.append(i)
# lst.append(90)
# lst.sort()
# print(lst)

# ----------------------------------------------

#
# i = 0
# x = 0
# while i != 10:
#     x += 1  # x=x+1
#     print(x)
#     i += 1

# --------------------------------------# lst[4]
# lst[5][1]
# x = 'параллелепипед'
# x = [1, 2, 3, 4, 5]
# i = reversed([1, 2, 3, 4, 5])
# print(i)
# x.reverse()
# print(x)
# x = x[::-1]

# ---------
'''
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
'''



# i = [1, 3, 5, 6]
# x = (1, 3, 5, 6)
# print(i)# list
# print(x)# tuple
# i.pop()
# print(i)
