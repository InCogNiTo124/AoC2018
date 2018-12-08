import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

from collections import deque

x = deque([int(t) for t in input().split(' ')])

def f():
    global x
    child_nodes = x.popleft()
    metadata_no = x.popleft()
    if child_nodes == 0:
        return sum([x.popleft() for t in range(metadata_no)])
    else:
        partial = []
        for i in range(child_nodes):
            partial.append(f())
        s = 0
        for i in range(metadata_no):
            index = x.popleft()
            try:
                s += partial[index-1]
            except:
                continue
        return s

print(f())
