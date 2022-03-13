# 10814번 나이순 정렬

n = int(input())
data = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    data.append([a, b])

data.sort(key = lambda x: (x[0]))

for a, b in data:
    print(a, b, sep=' ')