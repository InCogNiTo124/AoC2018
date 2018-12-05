from collections import deque

def check_adjacent(a, b):
    return a.lower() == b.lower() and a.upper() == b.upper() and a != b

def reduce(queue):
    L = float("inf")
    while len(queue) < L:
        L = len(queue)
        i = 1
        while i < len(queue):
            if check_adjacent(queue[i-1], queue[i]):
                del(queue[i])
                del(queue[i-1])
                i -= 2
            i += 1
    return queue

queue = list(input())
min_length = float("inf")
min_char = -1
for t in range(ord('a'), ord('z') + 1):
    t = chr(t)
    queue_copy = queue[:]
    i = 0
    while i < len(queue_copy):
        if queue_copy[i].lower() == t:
            del(queue_copy[i])
            i -= 1
        i += 1
    L = len(reduce(queue_copy))
    if min_length > L:
        min_length = L
        min_char = t

print(min_length)
