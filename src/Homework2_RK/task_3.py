"""
Вводится строка. Требуется удалить из нее
повторяющиеся символы и все пробелы.
"""

line = input("ВВедите предложение: ")
sym = "".join(list(dict.fromkeys(line)))
# Remove duplicate characters

no = sym.replace(' ', '')
# Remove spaces

print(no)
# We enter without spaces
