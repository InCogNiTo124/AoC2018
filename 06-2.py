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
for i in range(DIM_Y):
    for j in range(DIM_X):
        dist = 0
        for index, point in enumerate(points):
            dist += manhattan(point, (i, j))
        grid[i][j] = dist

linear_grid = []
for x in grid:
    linear_grid.extend(x)
print(sum(1 for t in linear_grid if t < 10000))
