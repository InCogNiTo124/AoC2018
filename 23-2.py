import re

class Nanobot:
    def __init__(self, pos, r):
        assert isinstance(pos, list)
        assert len(pos) == 3
        assert isinstance(r, int)
        self.pos = pos
        self.r = r
        return

    def __repr__(self):
        return "{} {}".format(repr(tuple(self.pos)), self.r)

    def distance(self, b):
        return abs(self.pos[0] - b.pos[0]) +\
               abs(self.pos[1] - b.pos[1]) +\
               abs(self.pos[2] - b.pos[2])

p = re.compile('[+-]?\d+(?:\.\d+)?')

line = input()
nanobots = list()
min_x = float("inf")
max_x = -float("inf")
min_y = float("inf")
max_y = -float("inf")
min_z = float("inf")
max_z = -float("inf")
while line != '':
    parts = p.findall(line)
    bot = Nanobot([int(t) for t in parts[:-1]], int(parts[-1]))
    nanobots.append(bot)
    line = input()

min_x = 17000000
max_x = 19500000
min_y = 10000000
max_y = 12000000
min_z = 14500000
max_z = 16000000
print("{} <= x <= {}".format(min_x, max_x))
print("{} <= y <= {}".format(min_y, max_y))
print("{} <= z <= {}".format(min_z, max_z))
from random import randint, sample
POP_COUNT = 2000
BEST = 120
population = [Nanobot([randint(min_x, max_x),
                       randint(min_y, max_y),
                       randint(min_z, max_z)], 1) for t in range(POP_COUNT)]


for epoch_count in range(100):
    print('\nEPOCH', epoch_count, '\n')
    evaluations = [sum(1 for x in nanobots if x.distance(t) < x.r) for t in population]
    population = sorted(population, key=lambda t: evaluations[population.index(t)], reverse=True)
    evaluations.sort(reverse=True)

    print(population[0], '\t', evaluations[0])
#    if 0 in evaluations:
#        population = [t for i, t in enumerate(population) if evaluations[i] > 0]
#    else:
    for i in range(0, BEST//3):
        del(population[-i-1])
#    for i in range(BEST//10):
#        population.append(
#            Nanobot([randint(min_x, max_x),
#                     randint(min_y, max_y),
#                     randint(min_z, max_z)], 1))
#    del(evaluations)
    best = population[:BEST]
    while len(population) < POP_COUNT:
        a, b = tuple(sample(best, 2))
        pos = [0, 0, 0]
        for c in range(3):
            p = randint(0, 11000) / 10000
            pos[c] = p * a.pos[c] + (1-p) * b.pos[c]
        kid = Nanobot(pos, 1)
        if randint(0, 1000) < 70:
            x = sample([0, 1, 2], randint(1, 3))
#            print("Mutation:")
#            print("Before:", kid.pos)
            for c in x:
                kid.pos[c] += randint(-1500000, 1500000)
#            print("After:", kid.pos)
        population.append(kid)

#for x, y in zip(population, evaluations):
#    print(x, '\t', y)

for i in range(0, 2):
    print(population[-i], evaluations[-i])
#print("\n".join([repr(t) for t in population]))
