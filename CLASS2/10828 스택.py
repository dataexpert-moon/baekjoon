# 10828번 스택
from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
stack = deque()

for _ in range(n):
    a = input().split()
    s = a[0]
    # pop
    if s == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # size
    elif s == 'size':
        print(len(stack))
    # empty
    elif s == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top
    elif s == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    # push
    else:
        b = a[1]
        stack.append(b)
