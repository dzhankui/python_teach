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

from numpy import sqrt


RoomShape = input('Please, enter a room shape type')
if RoomShape == 'rectangle':
    a = int(input('Please, enter first side size'))
    b = int(input('Please, enter second side size'))
    Area = a * b
if RoomShape == 'circle':
    pi = 3.14
    r = int(input('Please, enter a radius'))
    Area = pi * r ** 2
if RoomShape == 'triangle':
    a = int(input('Please, enter first side size'))
    b = int(input('Please, enter second side size'))
    c = int(input('Please, enter second side size'))
# halfperimeter = hp
    hp = (a + b + c) / 2
    Area = sqrt(hp * (hp - a) * (hp - b) * (hp - c))
print(Area)

# hometask:
# update interpreter
# update numpy
# update pip