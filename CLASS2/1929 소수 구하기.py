# 1929번 소수 구하기

import math

m, n = map(int, input().split())

array = [True for i in range(n+1)]
# 1은 소수가 아니므로 빼기
array[1] = False
# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i]:
        print(i)