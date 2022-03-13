# 10866번 덱

from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    a = input().split()
    s = a[0]
    # pop_front
    if s == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    # pop_back
    if s == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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
    # push_front
    elif s == 'push_front':
        b = a[1]
        q.appendleft(b)
    # push_back
    elif s == 'push_back':
        b = a[1]
        q.append(b)
