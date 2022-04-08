print(type(15*3))
print(type(15/3))
print(type(15//3))
print(type(15**2))

#todo split '5' and '+' done
#todo add zero to 5 and 5 to get 05
#todo add '+' to the second 05 => +05
#todo add " before and after numbers

my_list = ['в ', '5', ' часов ', '17', ' минут ', 'температура ', 'воздуха ', 'была ', '+5', ' градусов']
print(my_list.index('+5'))
cut_list = my_list[8]
cut_list = my_list[8].split('+', 1)
print(cut_list)
plus = '+'
quotes = '"'
plus5 = plus + cut_list[1]
# print(plus5)
quotes = '"'

information = f'в {quotes}{my_list[1]:0>2}{quotes} часов {quotes}{my_list[3]}{quotes} минут температура воздуха была {quotes}{plus}{cut_list[1]:0>2}{quotes} градусов'
print(information)
#тупое обособление кавычками
# my_list.insert(1, '"')
# my_list.insert(3, '"')
# my_list.insert(5, '"')
# my_list.insert(7, '"')
# my_list.insert(12, '"')
# my_list.insert(14, '"')

# не менее тупо, но с привязкой к индексу элемента
# my_list.insert(my_list.index('+5'), '"')
# my_list.insert(my_list.index('+5') + 1, '"')
# my_list.insert(my_list.index('5'), '"')
# my_list.insert(my_list.index('5') + 1, '"')
# my_list.insert(my_list.index('17'), '"')
# my_list.insert(my_list.index('17') + 1, '"')
# print(my_list)

# print(''.join(my_list))



