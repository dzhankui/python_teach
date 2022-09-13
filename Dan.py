"""Есть корзина с яблоками (basket). К нам в гости пришло несколько человек (people).
Требуется определить, сколько целых яблок достанется каждому (count), ведь ножа-то у нас нет.
А сколько яблок останется после гостей лежать в корзине? Обновить count"""
basket = int(input())
people = int(input())
count = basket // people
print(count)
count = basket % people
print(count)