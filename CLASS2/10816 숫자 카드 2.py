# 10816번 숫자 카드 2
from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index

for i in range(len(b)):
    print(count_by_range(a, b[i], b[i]), end=' ')