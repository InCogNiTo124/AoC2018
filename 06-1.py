from collections import Counter

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])
points = []
t = input()
while t != '':
    points.append(tuple([int(x) for x in t.split(', ')]))
    t = input()

DIM_X = 500
DIM_Y = 500
grid = [[float("inf") for j in range(DIM_X)] for i in range(DIM_Y)]
to_ignore = set()
for i in range(500):
    for j in range(500):
        min_dist = float("inf")
        min_point = -1
        for index, point in enumerate(points):
            dist = manhattan(point, (i, j))
            if dist == min_dist:
                min_point = -1
            elif dist < min_dist:
                min_dist = dist
                min_point = index
        grid[i][j] = min_point
        if i == 0 or i == DIM_Y-1 or j == 0 or j == DIM_X-1:
            to_ignore |= {min_point}

linear_grid = []
for x in grid:
    linear_grid.extend(x)

for index, count in Counter(linear_grid).most_common():
    if index not in to_ignore:
        print(count)
        break
