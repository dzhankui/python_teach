# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой
# для каждого из чисел в интервале от 1 до 100:
# 1 - нт -
# 2 - нта -
# 23 - нта -
# 24 - нта -
# 5,6,7,8,9,10,10+, - ов -

# процент 1 21 31 41 51 61 71 81 91
# процента 2 3 4 23 33 43 44 53 54 63 64 73 74 83 84 93 94
# процентов 1 2 3 4 5 6 7 8 9 x10 10+
# починить все
# num = []
# word = ''
# for i in range(1, 101):
#     num.append(i)
#     if (i % 2 == 0) and (i % 5 == 0) and (4 <= i >= 10):
#         word = 'процентов'
#     if (i % 3 == 0) and (i % 4 == 0) and (i % 5 == 0):
#         word = 'процент'
#     elif  #create a condition, that check last digit of a num
#
#     print(i, word)
percent = int(input('Введите количество процентов'))
word = '' # процент процента процентов
if percent <= 100:
    if percent == 1:
        word = 'процент'
        print(percent, word)
    elif percent <= 4:
        word = 'процента'
        print(percent, word)
    else:
        word = 'процентов'
        print(percent, word)