# 10845번 큐

from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    a = input().split()
    s = a[0]
    # pop
    if s == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    # size
    elif s == 'size':
        print(len(q))
    # empty
    elif s == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    # front
    elif s == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    # back
    elif s == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    # push
    else:
        b = a[1]
        q.append(b)
