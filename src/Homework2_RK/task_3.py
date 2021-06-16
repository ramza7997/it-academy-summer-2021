line = input("ВВедите предложение: ")
sym = "".join(list(dict.fromkeys(line)))
"""Remove duplicate characters"""
nosp = sym.replace(' ', '')
"""Remove spaces"""
print(nosp)
"""We enter without spaces"""
