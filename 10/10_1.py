m_box_open = open('mbox-short.txt')

email_count = {}

for line in m_box_open:
    if (not line.startswith('From') ) or line.startswith('From:'): continue
    words = line.split()

    email = words[1]


    email_count[email] = email_count.get(email, 0) + 1

    ar_of_tuple = []

    email_count_items = email_count.items()

    for k, v in email_count_items:
        ar_of_tuple.append((v, k))

    ar_of_tuple.sort(reverse=True)

most_commits = ar_of_tuple[0]
print(most_commits)