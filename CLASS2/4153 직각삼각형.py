# 4153번 직각삼각형

ans = []
while True:
    data = list(map(int, input().split()))
    data.sort()
    a, b, c = data[0], data[1], data[2]
    if a == 0 and b == 0 and c == 0:
        break
    if (a**2 + b**2) == c**2:
       ans.append('right')
    else:
        ans.append('wrong')

for i in ans:
    print(i)