"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма
Евклида (мы не знаем функции и рекурсию).
"""

first_natural_num = int(input("Первое натуральное число: "))
second_natural_num = int(input("Второе натуральное число: "))
while first_natural_num != 0 and second_natural_num != 0:
    if first_natural_num > second_natural_num:
        first_natural_num = first_natural_num % second_natural_num
    else:
        second_natural_num = second_natural_num % first_natural_num
print(f"Общий делитель {first_natural_num + second_natural_num}")
