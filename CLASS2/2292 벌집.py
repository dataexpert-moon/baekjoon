# 2292 벌집

# 6 12 18 24씩 증가
#a_n = a_(n-1) + 6n

n = int(input())

def solve(n):
    now, cnt = 1, 1
    if n == 1:
        return cnt
    for i in range(1, 1000000001):
        last = now
        now += 6 * i
        cnt += 1
        # 주어진 범위 내에 존재한다면
        if last < n <= now:
            return cnt

print(solve(n))