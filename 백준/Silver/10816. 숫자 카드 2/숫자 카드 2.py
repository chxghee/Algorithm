# https://www.acmicpc.net/problem/10816

# "숫자 몇 개냐" = Counter 최고

# "인덱스 찾기", "범위 세기" = bisect 최고


import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
has = list(map(int, input().split()))

m = int(input())
data = list(map(int, input().split()))

find = [0] * m

has_cnt = Counter(has)

for i in range(m):
    find[i] = has_cnt[data[i]]

for val in find:
    print(val, end=" ")
