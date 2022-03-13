# 11050번 이항 계수 1

n, k = map(int, input().split())

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)

ans = factorial(n) // (factorial(k) * factorial(n-k))
print(ans)