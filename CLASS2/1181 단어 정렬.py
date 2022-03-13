# 1181번 단어 정렬

n = int(input())
data = [input() for _ in range(n)]
# 중복 제거
set_data = list(set(data))

sort_data = []
for i in set_data:
    sort_data.append((len(i), i))

sort_data = sorted(sort_data)

for len_i, word in sort_data:
    print(word)
