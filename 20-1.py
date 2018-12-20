from collections import deque

regex = input()[1:-1]
stack = deque([0])

max_d = 0

for t in regex:
    d = stack.pop()
    if max_d < d:
        max_d = d
    if t in ['S', 'W', 'N', 'E']:
        stack.append(d+1)
    elif t == '(':
        stack.append(d)
        stack.append(d)
    elif t == '|':
        stack.append(stack[-1])
    elif t == ')':
        continue

if max_d < stack[0]:
    max_d = stack.pop()
print(max_d)
