# 1920번 수 찾기

n = int(input())
data = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
ans = []

for num in nums:
    if num in data:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i)