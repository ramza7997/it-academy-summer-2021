"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

student = int(input())
languag_list = []
for i in range(1, student + 1):
    languag_set = set()
    languag_n = int(input())
    for j in range(languag_n):
        languag = input()
        languag_set.add(languag)
    languag_list.append(languag_set)
know = set.intersection(*languag_list)
print(len(know))
for lang in know:
    print(lang)
a_know = set.union(*languag_list)
print(len(a_know))
for languag_a in a_know:
    print(languag_a)
