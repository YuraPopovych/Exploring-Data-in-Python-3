romeo_txt = open('romeo.txt')
ar  = []
for line in romeo_txt:

     words = line.strip('\n')

     split_ar = words.split()

     for i in split_ar:
         if (i not in ar):
             ar.append(i)


ar.sort()
print(ar)