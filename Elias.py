# print('hello, what is your name?')
# name = input()
# print('hello '+name+', how old are you')
# age = int(input())
# age = age + 1
# print('you will be 20 in ', age, ' years.')

# LISTS     0     1      2       |---------------3----------|
# lst = ['Elias', 11, 31.877465, [12, 'закуска', 'vodka', 14]]

'''
Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
'''
#
# from math import sqrt
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
# =======================================================================================


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
1. Написать проверку введенных значений для случаев, когда вводят букв и/или символы.
2. Переписать программу про страну Малевию с использованием функций. Функции должны вычислять площади.
'''
# done
# txt='1'
# txt_float=float('2.4')
# txt_int=int('2.3')
# txt_2='vova'
#
# print(txt.isdigit())
# print(txt_float.isdigit())
# print(txt_int.isdigit())
# print(txt_2.isdigit())
'''
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
'''
#
# done
# dictionaries  datatype key-value pairs
# x={drink:USA, meat:[chicken, beef]}

'''Twelve cards with grades from 0 to 11 randomly divided among 3 players: Frank, Sam, and Tom, 4 cards each. The game consists of 4 rounds.
 The goal of the round is to move by the card with the most points.
In round 1, the first player who has a card with 0 points, takes the first turn, and he starts with that card. 
Then the second player (queue - Frank -> Sam -> Tom -> Frank, etc.) 
can move with any of his cards (each card is used only once per game, and there are no rules that require players to make only the best moves). 
The third player makes his move after the second player, and he sees the previous moves.
The winner of the previous round then makes the first move in the next round with any remaining card.
The player who wins 2 rounds first, wins the game.
Task
Return true if Frank has a chance of winning the game.
Return false if Frank has no chance.
Input
3 arrays of 4 unique numbers in each (numbers in array are sorted in ascending order). Input is always valid, no need to check.
Example
Round 1: Frank 2 5 8 11, Sam 1 4 7 10, Tom 0 3 6 9. Tom has to start from 0. Frank is risking nothing and goes 2. Sam gets lucky and wins round by throwing 4.
Round 2: Frank 5 8 11, Sam 1 7 10, Tom 3 6 9. Sam starts from 1. Tom goes 3, Frank wins with 5.
Round 3: Frank 8 11, Sam 7 10, Tom 6 9. Frank starts from 11 and wins the round either way.
Frank is the first to win 2 rounds and therefore wins the game, the answer is true.
One more example
Frank 0 1 2 3, Sam 6 7 8 11, Tom 4 5 9 10.
With these cards Frank has no chance, the answer is false.
Tip
Players can actually play DUMB moves, especially Sam and Tom.'''



















# ====================================================================
'''Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
первое число, второе число и операцию, после чего применяет операцию к введённым числам 
("первое число" "операция" "второе число") и выводит результат на экран.'''
# ==============================================================================
'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.'''