"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.

Example
[]
"""
a=int(input())
b= a*100
if b>100:
    print(b-(b*.1))
else:
    print(b)