# 1874번 스택 수열
n = int(input())
stack, ans, find = [], [], True
# 숫자 1부터 시작
now = 1
for _ in range(n):
    num = int(input())
    # 스택 쌓기 Push
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    # 스택 꺼내기 Pop
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    # 불가능한 경우
    else:
        find = False

# 정답 출력
if not find: # 불가능하다면
    print('NO')
else:
    for i in ans: # 가능하다면
        print(i)

