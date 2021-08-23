from inspect import getmembers
from inspect import isfunction

import task1_1

functions_list = getmembers(task1_1, isfunction)


def runner(*args):
    if not args:
        for element in functions_list:
            func = element[1]
            func()
    else:
        for func_name in args:
            for element in functions_list:
                if func_name == element[0]:
                    func = element[1]
                    func()


runner()
runner('total_price')
runner('total_price', 'longest_word', 'languages')