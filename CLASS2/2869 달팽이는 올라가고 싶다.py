# 2869번 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
# 달팽이가 올라가는데 걸리는 날
day = (v-b)/(a-b)
# 정답 출력
print(int(day) if day == int(day) else int(day)+1)