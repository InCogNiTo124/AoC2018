import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

from collections import deque

x = deque([int(t) for t in input().split(' ')])

def f():
    global x
    child_nodes = x.popleft()
    metadata_no = x.popleft()
    print(child_nodes)
    print(metadata_no)
    s = 0
    for i in range(child_nodes):
        s += f()
    return s + sum([x.popleft() for t in range(metadata_no)])

print(f())
