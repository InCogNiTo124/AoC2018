from collections import Counter
import copy

area = []
line = input()
while line != '':
    area.append(list(line))
    line = input()
i_min = 0
j_min = 0
i_max = len(area)
j_max = len(area[0])

def get_adjacent(a):
    x, y = a
    adj = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            adj |= {(x+i, y+j)}
    adj -= {a}
    return set([(i, j) for i, j in adj if i_min <= i < i_max and j_min <= j < j_max])

print('\n'.join([''.join(t) for t in area]))

k = 0
while k < 10:
    print(k)
    new_area = [['@' for y in range(j_max)] for x in range(i_max)]
    for i in range(len(area)):
        for j in range(len(area[i])):
            adj = get_adjacent((i, j))
            adj_counts = Counter([area[i][j] for i, j in adj])
            if area[i][j] == '.':
                if adj_counts['|'] >= 3:
                    new_area[i][j] = '|'
                else:
                    new_area[i][j] = '.'
            elif area[i][j] == '|':
                if adj_counts['#'] >= 3:
                    new_area[i][j] = '#'
                else:
                    new_area[i][j] = '|'
            elif area[i][j] == '#':
                if adj_counts['#'] >= 1 and adj_counts['|'] >= 1:
                    new_area[i][j] = '#'
                else:
                    new_area[i][j] = '.'
    area = new_area
    print('\n'.join([''.join(t) for t in area]))
    k += 1

final_counter = Counter()
for t in area:
    final_counter.update(t)

print("{}*{}={}".format(final_counter['|'],
                        final_counter['#'],
                        final_counter['|'] * final_counter['#']))
