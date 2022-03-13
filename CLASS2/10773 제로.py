# 10773번 제로

k = int(input())
# 장부 리스트 생성
num_list = [0]
ans = 0

# 정수를 차례대로 입력받기
for _ in range(k):
  num = int(input())
  # 정수가 0이 아니면 장부에 추가
  if num != 0:
    num_list.append(num)
  # 정수가 0이면 장부에서 최근 값 삭제
  else:
    num_list.pop(-1)

# 장부에 있는 숫자 모두 더하기
for i in range(len(num_list)):
  ans += num_list[i]

# 정답 출력
print(ans)