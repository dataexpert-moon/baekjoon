# 11886번 요세푸스 문제 0

from collections import deque
n, k = map(int, input().split())
s = deque([])
# 데이터 추가
for i in range(1, n+1):
    s.append(i)
print('<', end ='')

while s:
    for _ in range(k-1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')


