"""
Your task is to find the factorial of a given number
Example
[In] 4
[Out] 24
[In] 3
[Out] 6
"""
n = int(input())

res = 1

for i in range(2, n + 1):
    res *= i
print(res)


