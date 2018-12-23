import re
import numpy as np

def manhattan(a, b):
    #assert isinstance(a, np.ndarray)
    #assert isinstance(b, np.ndarray)
    #assert a.shape == b.shape
    return np.abs(a-b).sum()

p = re.compile('[+-]?\d+(?:\.\d+)?')

line = input()
nanobot_pos = []
nanobot_r = []
while line != '':
    parts = p.findall(line)
    nanobot_pos.append([int(t) for t in parts[:-1]])
    nanobot_r.append(int(parts[-1]))
    line = input()
nanobot_pos = np.array(nanobot_pos, dtype=np.float64)
nanobot_r = np.array(nanobot_r, dtype=np.float64)

min_x = 17000000
max_x = 19500000
min_y = 10000000
max_y = 12000000
min_z = 14500000
max_z = 16000000
print("{} <= x <= {}".format(min_x, max_x))
print("{} <= y <= {}".format(min_y, max_y))
print("{} <= z <= {}".format(min_z, max_z))
POP_COUNT = 1000
BEST = 120
population = np.array([[np.random.uniform(min_x, max_x),
                        np.random.uniform(min_y, max_y),
                        np.random.uniform(min_z, max_z)] for t in range(POP_COUNT)], dtype=np.float64)

for epoch_count in range(100):
    print('\nEPOCH', epoch_count)
    #evaluations1 = np.array([np.sum(1 for pos, r in zip(nanobot_pos, nanobot_r) if manhattan(pos, t) <= r) for t in population], dtype=np.float64)
    evaluations = (np.abs(population[:,None] - nanobot_pos).sum(-1) < nanobot_r).sum(axis=1)
    arg_evals = np.argsort(-evaluations)
    population = population[arg_evals]
    evaluations = evaluations[arg_evals]
    print(population[0], '\t', evaluations[0])
    to_add = []
    best = population[:BEST, :]
    while len(to_add) < BEST // 2:
        a, b = tuple(best[np.random.randint(best.shape[0], size=2)])
        p = np.random.uniform(-0.1, 1.1)
        kid = (p * a + (1-p) * b).astype(np.float64)
        if np.random.uniform() < 0.07:
            pos = 1000000 * np.random.uniform(-1, 1, (3,))
            pos = pos.astype(np.float64)
            idx = np.random.choice([0, 1, 2], np.random.randint(1, 4), replace=False)
            kid[idx] += pos[idx]
        to_add.append(kid)
    to_add = np.array(to_add, dtype=np.float64)
    population[-BEST//2:] = to_add
#for x, y in zip(population, evaluations):
#    print(x, '\t', y)

for i in range(0, 2):
    print(population[-i], evaluations[-i])
#print("\n".join([repr(t) for t in population]))
