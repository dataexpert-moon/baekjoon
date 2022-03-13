# 2108번 통계학
import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

#오름차순 정렬
data.sort()

# 평균 구하기
mean = int(sum(data))
if mean >= 0:
    print(int(sum(data) / n + 0.5))
elif mean < 0:
    print(int(sum(data) / n - 0.5))

# 중앙값 구하기
print(data[int(n/2)])

# 최빈값 구하기
mode_data = [data[0]]
cnt = 1
cnt_max = 0
last = data[0]

for i in data[1:]:
    if i != last:
        # 특정 수의 개수가 현재 최빈값 개수보다 많다면
        if cnt > cnt_max:
            # 최빈값 리스트 초기화
            mode_data = []
            # 최빈값 리스트에 추가
            mode_data.append(last)
            cnt_max = cnt
        # 특정 수의 개수가 현재 최빈값 개수와 같다면 최빈값 추가
        elif cnt == cnt_max and last not in mode_data:
            mode_data.append(last)
        cnt = 1
    # 중복된 수가 있다면
    else:
        cnt += 1
    last = i

# 마지막 수 계산
if cnt > cnt_max:
    mode_data = [last]
elif cnt == cnt_max and last not in mode_data:
    mode_data.append(last)

# 최빈값이 1개라면 단일값 출력
if len(mode_data) == 1:
    print(mode_data[0])
# 최빈값이 여러개라면 두 번째로 작은 값 출력
else:
    print(mode_data[1])

# 범위 구하기
print(abs(data[-1] - data[0]))