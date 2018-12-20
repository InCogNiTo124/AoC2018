from collections import deque

regex = input()[1:-1]
farthest = 0
stack = deque([((0, 0), 0)])
visited = set()
for t in regex:
    (x, y), d = stack.pop()
    if (x, y) not in visited and d >= 1000:
        farthest += 1
    visited |= {(x, y)}
    if t == 'S':
        stack.append(((x, y-1), d+1))
    elif t == 'N':
        stack.append(((x, y+1), d+1))
    elif t == 'W':
        stack.append(((x-1, y), d+1))
    elif t == 'E':
        stack.append(((x+1, y), d+1))
    elif t == '(':
        stack.append(((x, y), d))
        stack.append(((x, y), d))
    elif t == '|':
        stack.append(stack[-1])
    elif t == '(':
        continue

print(farthest)
