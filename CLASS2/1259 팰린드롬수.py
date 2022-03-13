# 1259번 팰린드롬수

answer = []
while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        answer.append('yes')
    else:
        answer.append('no')

for ans in answer:
    print(ans)
