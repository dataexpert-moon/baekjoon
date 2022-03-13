# 2805 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, sum(trees)

# start와 end가 같아질 때까지 반복
while start <= end:
    mid = (start + end) // 2 # 중간 위치
    cnt = 0
    # 나무 자르기
    for tree in trees:
        # 나무의 높이가 절단기 높이보다 크다면
        if tree > mid:
            # 자르기
            cnt += tree - mid
    # 자른 나무들의 길이가 목표값 이상이라면
    if cnt >= m:
        # 시작점 조정
        start = mid + 1
    # 목표값 이하라면
    else:
        # 끝점 조정
        end = mid - 1
print(end)

