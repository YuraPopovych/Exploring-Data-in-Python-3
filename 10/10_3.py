""" count words in decreasing order of frequency """
import string

mbox_open = open('mbox-short.txt')

letters = {}
ar_letters = []

for line in mbox_open:
    translation = str.maketrans('', '', string.punctuation)
    line = line.translate(translation)
    line = line.lower()

    for i in line:
        if not i.isalpha(): continue
        letters[i] = letters.get(i, 0) + 1

letters_items = letters.items()

for letter, count in letters_items:
    ar_letters.append((count, letter))

ar_letters_sorted = sorted(ar_letters, reverse=True)

for count, word in ar_letters_sorted:
    print(word, count)

