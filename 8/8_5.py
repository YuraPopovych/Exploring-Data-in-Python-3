

my_text_file = open('mbox-short.txt')

count = 0

for line in my_text_file:

    if ( (not line.startswith('From')) or line.startswith('From:')): continue

    word = line.split()

    count += 1

    print(word[1])

print(count)






