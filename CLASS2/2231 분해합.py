# 2231번 분해합

n = int(input())
def constructor(n):
    num = 1
    while True:
        ans = num
        # 생성자가 없을 시
        if num == n:
            # 0을 반환
            return 0
        # 분해합 계산
        str_num = str(num)
        for i in range(len(str_num)):
            ans += int(str_num[i])
        # 생성자이면 return
        if ans == n:
            return num
        # 1 증가
        num += 1

print(constructor(n))


