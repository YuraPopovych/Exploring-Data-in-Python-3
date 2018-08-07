m_box_open = open('mbox-short.txt')


week_count = {}

for line in m_box_open:
    if (not line.startswith('From') ) or line.startswith('From:'): continue
    words = line.split()

    day_of_week = words[2]

    week_count[day_of_week] = week_count.get(day_of_week, 0) + 1



print(week_count)