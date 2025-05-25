# print("I'm "+'Vova', "I'm", '20'+'5', "y.o.")
# print(4*2) #
# print(4**2) # square of 4
# print(27/3)
# print(26//3)
# print(26 % 3)
# a>b a<b a>=b a<=b
# ===================================================
# height = int(input('Введите высоту треугольника'))
# base = int(input('Введите основание треугольника'))
#
# S = (height*base)/2
# print(S)
# print(type(S))
# ==================================================
""""""
"""Дано число n. С начала суток прошло n минут. 
Определите, сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
Учтите, что число n может быть больше, чем количество минут в сутках"""

"""How to solve:
нужно из количества введенных минут (n) вычесть число дней (в минутах), которое туда умещается и работать
с остальным числом минут, раскладывая его на часы (h) и минуты (m) и выводя их на экран """

n = int(input())            # input for some amount of minutes
d = n // 1440               # how much full 24-h_periods (days) in n minutes?
n_corr = n - (d * 1440)     # corrected "n"
hh = n_corr // 60           # Amount of hours
mm = n_corr % 60            # Amount of minutes
print(d, 'days')            # (We don't need) output days
print(hh, 'hours')          # output hours
print(mm, 'minutes')        # output minutes
