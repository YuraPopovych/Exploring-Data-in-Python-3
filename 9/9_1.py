text_word = open('word.txt')

as_ar = {}


for line in text_word:
    words  = line.split()
    for word in words:
        as_ar[word] = 'No matter'


print('is' in as_ar)
