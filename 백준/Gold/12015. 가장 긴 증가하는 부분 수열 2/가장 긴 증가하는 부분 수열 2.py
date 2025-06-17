import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

lis = []


for val in data:

    idx = bisect.bisect_left(lis, val)

    if len(lis) == idx:
        lis.append(val)
    else:
        lis[idx] = val

print(len(lis))

