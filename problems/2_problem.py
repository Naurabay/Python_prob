"""
[!] Ввод в одну строку. Дается два числа. Нужно найти их сумму.

ПРИМЕР
-----------
>>> Ввод: 3 4
>>> Вывод: 7
"""
i = [int(a) for a in input().split()]
print(sum(i))