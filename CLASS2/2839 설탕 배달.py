# 2839번 설탕 배달

n = int(input()) # 설탕
result= 0 # 봉지 수

while n>=0:
  if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
    result += n // 5 # 5로 나눈 몫 출력
    print(result)
    break
  n -= 3 # 설탕이 5의 배수가 될 때까지 반복
  result += 1 # 봉지 추가
else:
  print(-1)