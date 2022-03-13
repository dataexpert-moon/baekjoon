# 1436번 영화감독 숌

n = int(input())
cnt, sum, ans = 0, 1, list()

while True:
    # 주어진 수를 찾았으면
    if cnt == n:
        # 반복문 종료
        break
    # 666이 포함되어 있는 수라면
    if '666' in str(sum):
        # 개수 추가
        cnt += 1
        # 정답 리스트에 추가
        ans.append(sum)
    # 수 1씩 증가
    sum += 1
# 정답 출력
print(ans[n-1])