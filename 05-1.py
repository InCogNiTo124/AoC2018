from collections import deque

def check_adjacent(a, b):
    return a.lower() == b.lower() and a.upper() == b.upper() and a != b

def reduce(input_string):
    q = deque()
    for t in input_string:
        q.append(t)
        while len(q) >= 2 and check_adjacent(q[-1], q[-2]):
            q.pop()
            q.pop()
    return len(q)

print(reduce(input()))
