"""
Take values of length and breadth of a rectangle from the user and check if it is square or not.

Note: Input must be in one line

[In] 4 5
[Out] No

[In] 6 6
[Out] Yes
"""
a, b = map(int, input().split())
if a > 0 and b > 0:
    if a == b:
        print('Yes')

    else:
        print('No')


