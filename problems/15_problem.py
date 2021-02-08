"""
A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern.
The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ...,
where the pattern is: "add 3 to the previous term".
In this problem, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ...
This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3
Write a program that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above.
 When n < 0 return the sequence with negative terms.
"""
n=int(input())
output = [0]
sign = 1
if n < 0:
    sign = -1
for numb in range(1, abs(n) + 1):
    output.append(sign * (numb + abs(output[numb - 1])))
print(output)