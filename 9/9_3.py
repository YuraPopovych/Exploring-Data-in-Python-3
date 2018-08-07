m_box_open = open('mbox-short.txt')

email_count = {}

for line in m_box_open:
    if (not line.startswith('From') ) or line.startswith('From:'): continue
    words = line.split()

    email = words[1]

    email_count[email] = email_count.get(email, 0) + 1


min_count = min(email_count)
max_count = max(email_count)


print('Prin min count: ', min_count, email_count[min_count])
print('Prin max count: ', max_count, email_count[max_count])