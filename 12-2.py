initial_state = list(input()[15:])
input()
line = input()
transitions = dict()
while line != '':
    parts = line.split(' => ')
    transitions[parts[0]] = parts[1]
    line = input()

prev = 0
curr = 0
state = initial_state[:]
for gen in range(1, 200):
    state = ['.', '.'] + state + ['.', '.']
    new_state = []
    for i in range(len(state)):
        sublist = "".join([state[(i+t) % len(state)] for t in range(-2, 3)])
        new_state.append(transitions[sublist] if sublist in transitions else '.')
    state = new_state[:]
    del new_state
    prev = curr
    curr = sum([i-2*gen for i in range(len(state)) if state[i] == '#'])
print(curr + (50000000000-199)*(curr-prev))
