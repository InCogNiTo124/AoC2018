graph = dict()
line = input()
while line != '':
    steps = line.split(' ')
    if steps[7] not in graph:
        graph[steps[7]] = {steps[1]}
    else:
        graph[steps[7]] |= {steps[1]}
    line = input()

s = set()
for t in graph:
    print('O' in graph[t])
    s |= graph[t]

alphabet = set([chr(t) for t in range(ord('A'), ord('Z')+1)])
s = alphabet - set(graph.keys())
print(s)
order = list()
while len(s) > 0:
    t = min(s)
    if t not in order:
        order.append(t)
        for key in graph:
            if graph[key].issubset(set(order)):
                s |= {key}
    s -= {t}

print("".join(order))

