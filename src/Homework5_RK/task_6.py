"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_sep(num, count):
    if num % 2 == 0:
        count += 1
        num = num / 2
        return max_sep(num, count)
    else:
        return 2 ** count


input_num = int(input('Введите число: '))
print(max_sep(input_num, 0))
