from collections import deque

def check_adjacent(a, b):
    return a.lower() == b.lower() and a.upper() == b.upper() and a != b

def reduce(input_string, ignore_char=''):
    q = deque()
    for t in input_string:
        if t.lower() != ignore_char:
            q.append(t)
            while len(q) >= 2 and check_adjacent(q[-1], q[-2]):
                q.pop()
                q.pop()
    return len(q)

min_len = float("inf")
input_string = input()
for char in range(ord('a'), ord('z')+1):
    char = chr(char)
    L = reduce(input_string, ignore_char=char)
    if min_len > L:
        min_len = L

print(min_len)
