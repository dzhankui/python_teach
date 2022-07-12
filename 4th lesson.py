# todo
# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать
# результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


from requests import get, utils
import xml.etree.ElementTree as ET


def currency_rates(CharCode):
    name = input('Please gimme a currency code')
    #  getting the html-like page (almost html-code) as string with all tags and so on
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)  # decoding xml-file for a headers
    content = response.content.decode(encoding=encodings)
    xml = ET.fromstring(content)  # xml-string -> to structured doc
    children = xml.findall('Valute')  # finding all 'Valute' in the document
    CharCode = xml.findall('CharCode')  # finding all 'CharCode'
    for child in children:
        name = child.find('Name')  # возвращает элемент-тег с вложенной структурой, то есть, 'name' и все
        if name.text == CharCode:
            return child.find('CharCode').text
    return None


print((currency_rates('CharCode')))

# =================================================================
# todo
# (вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
# ================================================================
# todo
# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
# ================================================================
# todo
# (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
