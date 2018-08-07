m_box_open = open('mbox-short.txt')

email_count = {}

for line in m_box_open:
    if (not line.startswith('From') ) or line.startswith('From:'): continue
    words = line.split()

    word = words[1]

    domain_index = word.find('@') + 1

    email_domain = word[domain_index:]

    #print(email_domain)

    email_count[email_domain] = email_count.get(email_domain, 0) + 1



print(email_count)