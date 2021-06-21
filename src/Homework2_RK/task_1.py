"""
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек
цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L
товаров.
"""

rub = 3
cen = 20
prod = 3
total = prod * (100 * rub + cen)
# We translate into kopecks and
# multiply by the number of goods

print(total // 100, total % 100, sep=',')
# Break into rubles and kopecks
