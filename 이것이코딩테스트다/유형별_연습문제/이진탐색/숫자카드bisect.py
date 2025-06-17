# https://www.acmicpc.net/problem/10816

# "숫자 몇 개냐" = Counter 최고

# "인덱스 찾기", "범위 세기" = bisect 최고


import sys
import bisect
input = sys.stdin.readline


n = int(input())
has = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

has.sort()
for val in find:
    idx = bisect.bisect_left(has, val)
    if has[idx] == val:
        print(1, end=' ')
    else:
        print(0, end=' ')


