"""
Выведите n-ое число Фибоначчи, используя только
временные переменные,
циклические операторы и условные операторы.
n - вводится
"""

fib1 = 0
fib2 = 1

n = input("Номер Фибоначчи: ")
n = int(n)
# Fibonacci number input

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
# We calculate the number that is located by this number

print("Значение:", fib2)
# Displaying the number
