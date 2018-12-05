from collections import deque

def check_adjacent(a, b):
    return a.lower() == b.lower() and a.upper() == b.upper() and a != b

queue = list(input()) #deque(input())
print(len(queue))
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

print(len(queue))

if __name__ == "__main__":
    print(check_adjacent('a', 'A'))
