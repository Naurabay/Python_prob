"""
[!] Ввод в одну строку. Дается три целых числа. 
Необходимо найти площадь прямоугольного параллелепипеда и вывести результат в терминал.

ПРИМЕР
-----------
>>> Ввод: 3 4 5
>>> Вывод: 94
"""

a, b, c = map(int, input().split())
print( 2*(a*b + b*c + a*c))