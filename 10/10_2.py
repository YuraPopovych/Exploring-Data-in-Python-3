m_box_open = open('mbox-short.txt')

hours_count = {}

hours_items = []

for line in m_box_open:
    if (not line.startswith('From') ) or line.startswith('From:'): continue
    words = line.split()

    hr_min_sec = words[-2]

    hours = hr_min_sec[:2]

    hours_count[hours] = hours_count.get(hours, 0) + 1

    hours_count_items = hours_count.items()

for k, v in hours_count_items:
    hours_items.append((k, v))


hours_items_sorted = sorted(hours_items)

for hour, freq in hours_items_sorted:
    print(hour, freq)
