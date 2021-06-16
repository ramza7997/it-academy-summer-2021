# S = √ p * (p − a) * (p − b) * (p − c),
# где a, b, c — стороны, p — полупериметр,
# который можно найти по формуле: p = (a + b + c) : 2

a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))
if a > 0 and b > 0 and c > 0:
    s = (a + b + c) / 2
    i = s * (s - a) * (s - b) * (s - c)
    num = i ** 0.5
    print(num)
else:
    print("Не правильные стороны")
