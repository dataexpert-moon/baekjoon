# 2164번 카드2
from collections import deque

n = int(input())
cards = deque()
for i in range(1, n+1, 1):
    cards.append(i)

while True:
    # n이 1일 때 고려
    if len(cards) == 1:
        break
    # 제일 위에 있는 카드 버리기
    cards.popleft()
    if len(cards) == 1:
        break
    # 제일 위에 있는 카드를 제일 아래에 있는 카드로 옮기기
    card = cards.popleft()
    cards.append(card)

for i in cards:
    print(i)