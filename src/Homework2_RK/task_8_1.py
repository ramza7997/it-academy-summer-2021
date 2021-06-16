"""
!Easy!

Task
Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

num = int(input("Введите число:"))
if num > 0:
    if num % 2 == 1:
        print("Weird")
    elif num % 2 == 0 and 2 <= num <= 5:
        print("not Weird")
    elif num % 2 == 0 and 6 <= num <= 20:
        print("Weird")
    elif num > 20:
        print("not Weird")
else:
    print("Error")
