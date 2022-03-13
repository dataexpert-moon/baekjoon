# 1978번 소수 찾기

import math

n = int(input())
data = list(map(int, input().split()))
cnt = 0
array = [True for i in range(1001)]
# 1은 소수가 아니므로 빼기
array[1] = False

# 에라토스테네스 체 알고리즘
for i in range(2, int(math.sqrt(1000)) + 1):
    if array[i] == True: # i가 소수인 경우
        j = 2
        while i * j <= 1000:
            array[i*j] = False
            j += 1

for i in range(len(data)):
    if array[data[i]]:
        cnt += 1

print(cnt)