"""
!Medium!

Task
You are given a positive integer N.
Your task is to print a palindromic
triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

You can't take more than two lines. The first line
(a for-statement) is already written for you.
You have to complete the code using exactly
one print statement.
"""

num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(int((10 ** i - 1) / 9) ** 2)
