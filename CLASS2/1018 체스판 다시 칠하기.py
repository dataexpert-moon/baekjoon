# 1018번 체스판 다시 칠하기
# N과 M이 최대 50, 시간 제한 2초 고려 -> O(N^4) 시간복잡도 사용 가능
# 4중 반복문을 이용해 해결

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board, count = [list(input()) for _ in range(n)], set()

# 모든 경우의 수에 대하여
for i in range(n-7):
    for j in range(m-7):
        # 가능한 2가지(시작 위치가 흰색 or 검은색) 변수 생성
        first_white = 0
        first_black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열 인덱스 합이 짝수일 때
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_white += 1
                    if board[k][l] != 'B':
                        first_black += 1
                # 행과 열 인덱스 합이 홀수일 때
                else:
                    if board[k][l] != 'B':
                        first_white += 1
                    if board[k][l] != 'W':
                        first_black += 1
        # 개수를 count에 추가
        count.add(first_white)
        count.add(first_black)
# 칠해야 하는 개수 최솟값 출력
print(min(count))

