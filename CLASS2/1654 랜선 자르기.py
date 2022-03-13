# 1654번 랜선 자르기

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
start, end = 1, max(data)

# start와 end가 같아질 때까지 반복
while start <= end:
    mid = (start + end) // 2 # 중간 위치
    cnt = 0
    for i in data:
        cnt += i // mid # 분할된 랜선 수
    # 목표값 이상이면
    if cnt >= n:
        # 시작점 조정
        start = mid + 1
    # 목표값 이하라면
    else:
        # 끝점 조정
        end = mid - 1
# 정답 출력
print(end)

