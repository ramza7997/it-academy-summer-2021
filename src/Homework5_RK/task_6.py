"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_sep(num, count):
    if num % 2 == 0:
        count += 1
        num = num / 2
        result = max_sep(num, count)
    else:
        result = 2 ** count
    return result


input_num = int(input('Введите число: '))
print(max_sep(input_num, 0))
