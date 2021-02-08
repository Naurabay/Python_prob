"""
Given a positive integer n, calculate the following sum:
n + n/2 + n/4 + n/8 + ...
All elements of the sum are the results of integer division.
Example
[In] 25
[Out] 47
"""
import math

n = int(input())
summa = 0
while n > 0:
    summa += n
    n = math.floor(n / 2)
print(summa)
