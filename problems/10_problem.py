"""
Your task is to find the multiplication of given numbers
Example
[In] 4 5 1 9 3 2 10 1
[Out] 10800
"""

i = [int(a) for a in input().split()]
m=1
for j in i:
    m *= j
print(m)
