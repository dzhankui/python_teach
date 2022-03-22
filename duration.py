print('Введите период в секундах, а я все сделаю красиво!')
mins = 0
hrs = 0
d = 0
sec = 0
duration = int(input())

if duration >= 60:
    mins = duration // 60
    sec += duration % 60
    hrs = mins // 60
    mins = mins % 60
    d = hrs // 24
    hrs = hrs % 24
    print(d, 'дн', hrs, 'ч', mins, 'мин', 'и', sec, 'сек')

else:
    print('вы веели лишь', duration, 'сек')

# if duration >= 60:
#     mins = duration // 60 #sec
#     sec += duration%60
#     hrs = mins // 60 #min
#     a = 3 % 5
#     d = hrs // 24 #hrs
#     sec = a
# elif duration < 60:
#     print('вы ввели', duration, 'секунд')
# print('duration = ', duration, 'сек')
# print(d, 'дн', hrs, 'ч', mins, 'мин', 'и', sec, 'сек')
