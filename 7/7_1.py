
try:
    user_input = input('Input file name here:')
    text_file = open(user_input)

except:
    print('There are no such file here. Please insert correct file name.')
    exit()


count = 0
number = 0
space_plus_number_indetation = 2


for line in text_file:
    if line.lstrip().startswith('X-DSPAM-Confidence'):
        start_index_of_a_number = line.find(':') + space_plus_number_indetation
        number += float(line[start_index_of_a_number:])
        count += 1
avg_number = number / count
print(avg_number)
