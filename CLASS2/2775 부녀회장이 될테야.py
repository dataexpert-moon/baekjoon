# 2775번 부녀회장이 될테야

T = int(input())
ans = []
for _ in range(T):
    k = int(input())
    n = int(input())
    # 0층 리스트
    zeros = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            zeros[j] += zeros[j-1]
    ans.append(zeros[-1])

for i in ans:
    print(i)

