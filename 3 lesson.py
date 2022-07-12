# ================================= dictionary exercises:    ===============================================
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# # my_dict = dict(zip(keys, values))
# # print(my_dict)
# my_dict = dict()
# for i in range(len(keys)):
#     my_dict.update({keys[i]: values[i]})
# print(my_dict)
# ==============================================================================================
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
import random

from numpy.core.defchararray import capitalize, title


# def num_translate(key):
#     a = {
#         'zero': 'ноль',
#         'one': 'один',
#         'two': 'два',
#         'three': 'три',
#         'four': 'четыре',
#         'five': 'пять',
#         'six': 'шесть',
#         'seven': 'семь',
#         'eight': 'восемь',
#         'nine': 'девять',
#         'ten': 'десять'
#     }
#     return a.get(key.lower())
#
#
#
# key = input('Input the word in engl: ')
#
#
# if key == key.capitalize():
#     print(num_translate(key).capitalize())
# elif key == key.upper():
#     print(num_translate(key).upper())
# else:
#     print(num_translate(key))


# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

# names = input('Введите имена сотрудников через запятую (можно с маленькой буквы и без пробелов)')
# names = 'tom,Todd,gAs, saM,fReak'
# def thesaurus(names):  # применяем ф-цию распаковки, которая позволит нашей ф-ии работать с неизвестным числом позиционных эл-ов
#     """функция в качестве аргументов принимает имена
#     сотрудников и возвращает словарь,
#     где ключи - это первые буквы имен, а значения - списки"""
#     names = names.replace(' ', '')  # убираем все лишние и случайные пробелы при вводе имен
#     names = names.title()  # Делаем каждый элемент с заглавной буквы, остальные буквы - строчные
#     list_names = names.split(',')  # Получаем список имен, разделив строку по запятой на массив эл-ов
#     dictnames = {}
#     for name in list_names:  #
#         first_letter = name[0: 1]  #
#         if first_letter in dictnames:
#             dictnames.get(first_letter).append(name)
#         else:
#             dictnames.setdefault(first_letter, [name])
#     return dictnames
#
#
# print('dictnames', thesaurus(names))
# ========Version 2=============================================
# def thesaurus(*names):
#     out_dict = dict()
#     for name in names:
#         out_dict.setdefault(name[0], [])
#         out_dict[name[0]].append(name)
#     return out_dict
#
#
# print(thesaurus("rjym", "rtfg", "fuck", "ShiT"))
# ===========================================================
# Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается
# с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {"П": ["Петр Алексеев"]},
#     "И": {"И": ["Илья Иванов"]},
#     "С": {"И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"]}
# }
# Как поступить, если потребуется сортировка по ключам?

# =========================================================================

# name_surname = input('введите имя и фамилию через запятую')
# name_surname = "Иван сергеев", "инНа Серова", "ПеТр Алексеев", "Илья Иванов" ,"Анна Савельева"

# def thesaurus_adv(*names_surnames):
#     out_dict = {}
#     for name_surname in names_surnames:
#         name, surname = name_surname.split()
#         out_dict.setdefault(surname[0], {})
#         out_dict[surname[0]].setdefault(name[0], [])
#         out_dict[surname[0]][name[0]].append(name_surname)
#
#     sorted_dict = {
#         x: out_dict[x]
#         for x in sorted(out_dict)
#     }
#
#     return out_dict

    #     if name[0] is capitalize:
    #         out_dict.setdefault(name[0], [])
    #     else:
    #         name = name.title()
    #         out_dict.setdefault(name[0], [])
    #     out_dict[name[0]].append(name)
    # return out_dict


# print(thesaurus_adv("Иван сергеев", "инНа Серова", "ПеТр Алексеев", "Илья Иванов", "Анна Савельева"))

# ====================================================================================================

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


# input = int(input('how many jokes do you need?'))
#
#
# def get_jokes(jokes_amount):
#     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#     for i in range(1, jokes_amount+1):
#         rndm_for_nouns = random.randrange(0, len(nouns))
#         rndm_for_adverbs = random.randrange(0, len(adverbs))
#         rndm_for_adjectives = random.randrange(0, len(adjectives))
#         joke = f"joke is " \
#                f"{nouns[rndm_for_nouns]}" \
#                f"{' '}" \
#                f"{adverbs[rndm_for_adverbs]}" \
#                f"{' '}" \
#                f"{adjectives[rndm_for_adjectives]}"
#         nouns.remove(nouns[rndm_for_nouns])
#         adverbs.remove(adverbs[rndm_for_adverbs])
#         adjectives.remove(adjectives[rndm_for_adjectives])
#
#         print(joke)
#     # return joke можно ничего и не возвращать
#
#
# get_jokes(input)
# =====================================================================================================================
#