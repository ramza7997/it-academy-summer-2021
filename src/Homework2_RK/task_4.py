"""
Посчитать количество строчных (маленьких) и
прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

text = input()
text_s = 0
text_b = 0
# We assign 0 to count

for i in text:
    if i.isupper():
        text_s += 1
    else:
        text_b += 1
        # Count uppercase and lowercase letters
        # and increment the counter by 1

print(text_s)
print(text_b)
