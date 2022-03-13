# 2751번 수 정렬하기 2

n = int(input())

data = []
for _ in range(n):
    num = int(input())
    data.append(num)

for i in sorted(data):
    print(i)