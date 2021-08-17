"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def nearest_degree(num_work):
    final_num = 0
    num = num_work
    while num / 2 > 1:
        num = num / 2
        final_num += 1
    if (num_work - 2 ** final_num) / 2 ** final_num >= 0.5:
        result = '{}'.format(2 ** (final_num + 1))
    else:
        result = '{}'.format(2 ** final_num)
    return result


input_num = int(input())
print(nearest_degree(input_num))
