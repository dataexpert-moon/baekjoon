# 1966번 프린터 큐

t = int(input())
ans = list()

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    check = [0 for _ in range(n)]
    # 문서위치 저장
    check[m] = 1
    cnt = 0
    while True:
        if data[0] == max(data):
            cnt += 1
            if check[0] != 1:
                del check[0]
                del data[0]
            else:
                ans.append(cnt)
                break
        else:
            data.append(data[0])
            check.append(check[0])
            del data[0]
            del check[0]

for i in ans:
    print(i)