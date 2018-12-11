import numpy as np


SERIAL = int(input())


def power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += SERIAL
    power *= rack_id
    power = (power // 100) % 10
    return power - 5

"""
SERIAL = 8
print(power(3, 5))
SERIAL = 57
print(power(122, 79))
SERIAL = 39
print(power(217, 196))
SERIAL = 71
print(power(101, 153))
"""
grid = np.empty((300, 300))
for i in range(1, 301):
    for j in range(1, 301):
        grid[i-1, j-1] = power(i, j)

max_sum = 0
max_top = 0
max_left = 0
max_square = 0
for square_size in range(1, 300):
    for left in range(300-square_size):
        for top in range(300-square_size):
            s = np.sum(grid[top:top+square_size, left:left+square_size])
            if max_sum < s:
                max_sum = s
                max_top = top
                max_left = left
                max_square = square_size
print(s, (max_top+1, max_left+1, max_square))
