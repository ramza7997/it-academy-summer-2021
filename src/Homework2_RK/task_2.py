sent = input("Предложения: ")
words = dict()
for word in sent.split(" "):
    words[len(word)] = word

text = words[max(words)]
print(text)
