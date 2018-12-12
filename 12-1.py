initial_state = list(input()[15:])
input()
line = input()
transitions = dict()
while line != '':
    parts = line.split(' => ')
    transitions[parts[0]] = parts[1]
    line = input()

state = initial_state[:]
for gen in range(1, 2):
    state = ['.', '.'] + state + ['.', '.']
    new_state = []
    for i in range(len(state)):
        sublist = "".join([state[(i+t) % len(state)] for t in range(-2, 3)])
        new_state.append(transitions[sublist] if sublist in transitions else '.')
    state = new_state[:]
    del new_state
print(sum([i-2*gen for i in range(len(state)) if state[i] == '#']))
