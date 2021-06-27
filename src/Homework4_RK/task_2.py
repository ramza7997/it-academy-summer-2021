"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""

ans = int(input())
dct_country_city = {}
for _ in range(ans):
    s = input().split()
    country, cities = s[0], s[1:]
    for city_raw in cities:
        dct_country_city[city_raw] = country
ans_1 = int(input())
country = ""
for i in range(ans_1):
    city = input()
    country += dct_country_city[city] + "\n"
print(country)
