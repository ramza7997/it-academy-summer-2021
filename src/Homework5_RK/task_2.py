"""
Создайте декоратор, который хранит результаты
вызовов функции (за все время вызовов, не только текущий запуск программы)

"""


def decorator(function_one):
    def wrapper(*args, **kwargs):
        results = function_one(*args, **kwargs)
        with open("results.txt", "a") as res:
            res.write(str(results) + "\n")
        return results

    return wrapper


@decorator
def function_sum(x, y):
    return x + y


print(function_sum('a', 'b'))
print(function_sum(1, 9))
print(function_sum(3, 3))


@decorator
def func_sub(x, y):
    return x - y


print(func_sub(9, 8))
print(func_sub(4, 9))
print(func_sub(3, 6))
