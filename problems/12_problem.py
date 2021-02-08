"""
Your task is to reverse an integer number
Example
[In] 76542
[Out] 24567
"""
n = int(input())
reversed = 0

while (n != 0):
    r = int(n % 10)
    reversed = reversed * 10 + r
    n = int(n / 10)

print(reversed)