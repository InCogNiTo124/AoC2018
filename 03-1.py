from collections import deque

def region_overlap(a, b):
    if a[1] < b[1] + b[3] and a[1] + a[3] > b[1]:
        start = max(a[1], b[1])
        end = min(a[1]+a[3], b[1] + b[3])
        x = set([i for i in range(start, end)])
    else:
        return set()

    if a[2] < b[2] + b[4] and a[2] + a[4] > b[2]:
        start = max(a[2], b[2])
        end = min(a[2] + a[4], b[2] + b[4])
        y = set([j for j in range(start, end)])
    else:
        return set()

    to_return = set()
    for i in x:
        for j in y:
            to_return |= {(i, j)}
    return to_return

already_overlapping = set()

x = deque()
line = input()
while line != '':
    parts = line.split(' ')
    id = int(parts[0][1:])
    topleft = parts[2][:-1].split(',')
    left = int(topleft[0])
    top = int(topleft[1])
    dims = parts[3].split('x')
    width = int(dims[0])
    height = int(dims[1])
    x.append((id, left, top, width, height))
    line = input()

for i in range(len(x)-1):
    a = x[i]
    for j in range(i+1, len(x)):
        b = x[j]
        intersection_set = region_overlap(a, b)
        already_overlapping |= intersection_set

print(len(already_overlapping))

if __name__ == "__main__":
    print(region_overlap((1, 1, 3, 4, 4), (1, 3, 1, 4, 4)))
