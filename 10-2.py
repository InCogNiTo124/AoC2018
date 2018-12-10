## This file is exact copy of the 10-1.py
## minus the previous line
## minus the previous line
## ...
## RecursionError: maximum depth exceeded

import re
from matplotlib import pyplot as plt
import numpy as np

p = re.compile('[+-]?\d+(?:\.\d+)?')

class Light:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        return

    def __repr__():
        return "#"

    def move(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def __eq__(self, b):
        return b == self.position

    def __hash__(self):
        return hash(self.position)

line = input()
lights = set()
points = []
velocities = []
while line != '':
    parts = p.findall(line)
    points.append([int(t) for t in parts[:2]])
    velocities.append([int(t) for t in parts[2:]])
    line = input()
points = np.array(points)
velocities = np.array(velocities)
x_max = -float("inf")
y_max = -float("inf")
x_min = float("inf")
y_min = float("inf")
i = 10450
fig = plt.figure()
for d in range(i):
    points += velocities
"""
for t in lights:
    if x_min > t.position[0]:
        x_min = t.position[0]
    elif x_max < t.position[0]:
        x_max = t.position[0]

    if y_min > t.position[1]:
        y_min = t.position[1]
    elif y_max < t.position[1]:
        y_max = t.position[1]
"""
while True:
    print(i)
    plt.plot(points[:, 0], points[:, 1], 'ro', markersize=0.5)
    plt.show()
    points += velocities
    i += 1
