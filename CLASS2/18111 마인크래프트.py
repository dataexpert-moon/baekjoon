# 18111번 마인크래프트
from sys import stdin
input = stdin.readline

def solve_height(h):
    time = 0
    for i in range(n):
        for j in range(m):
            if house[i][j] == h:
                continue
            elif house[i][j] > h:
                time += (house[i][j] - h) * 2
            else:
                time += (h - house[i][j])
    return [time, h]

n, m, b = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]
result = [float('inf'), 0]
# 최대 높이 설정을 위한 변수
sum = b
# 현재 땅의 높이 합 추가
for i in range(n):
    for j in range(m):
        sum += house[i][j]
# 최대 높이 길이 설정
max_h = min(257, sum//(n*m) + 1)

# 구현
for i in range(0, max_h):
    time, h = solve_height(i)
    if time <= result[0]:
        result[0] = time
        result[1] = h

print(*result)



