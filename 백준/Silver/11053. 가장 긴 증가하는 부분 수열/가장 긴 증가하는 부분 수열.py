# https://www.acmicpc.net/problem/11053
import sys
import bisect
input = sys.stdin.readline

n = int(input())

data = map(int, input().split())


long = []
for val in data:
    idx = bisect.bisect_left(long, val)

    if len(long) == idx:
        long.append(val)
    else:
        long[idx] = val

print(len(long))
