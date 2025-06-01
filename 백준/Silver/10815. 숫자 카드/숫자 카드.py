
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
