text = input()
text_s = 0
text_b = 0
"""We assign 0 to count"""
for boo in text:
    if 'a' <= boo <= 'z':
        text_s += 1
    elif 'A' <= boo <= 'Z':
        text_b += 1
        """Count uppercase and lowercase letters
         and increment the counter by 1
         """

print(text_s)
print(text_b)
