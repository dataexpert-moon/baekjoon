# 10250 ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = 0
    house = 0
    if n % h == 0:
        floor = h * 100
        house = n//h
    else:
        floor = (n % h) * 100
        house = 1 + n // h
    print(floor + house)
