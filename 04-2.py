from collections import deque, Counter

x = deque()
line = input()
while line != '':
    date = line[1:11]
    time = line[12:17]
    if '#' in line:
        i = line.index('#')
        j = line[i+1:].index(' ')
        value = int(line[i+1:i+1+j])
    elif 'wakes up' in line:
        value = -1
    elif 'falls asleep' in line:
        value = 0
    x.append(('{} {}'.format(date, time),
              int(time[3:5]),
              value))
    line = input()

x = sorted(x, key=lambda t: t[0])
guard_sleep_dict = dict()

time_start = -1
time_end = -1
guard_no = -1
for entry in x:
    if entry[2] == 0:
        time_start = entry[1]
    elif entry[2] == -1:
        time_end = entry[1]
        guard_sleep_dict[guard_no].extend([t for t in range(time_start, time_end)])
        time_start = -1
        time_end = -1
    else:
        guard_no = entry[2]
        if guard_no not in guard_sleep_dict:
            guard_sleep_dict[guard_no] = []

max_guard = 0
max_freq = 0
max_min = 0
for minute in range(0, 60):
    for guard in guard_sleep_dict:
        s = sum([t == minute for t in guard_sleep_dict[guard]])
        if s > max_freq:
            max_freq = s
            max_guard = guard
            max_min = minute

print(max_guard)
print(max_min)
print(max_guard * max_min)
