# https://www.acmicpc.net/problem/1300

import sys
input = sys.stdin.readline


def count(x):
    cnt = 0
    for i in range(1 , n+1):
        cnt += min(x// i, n)
    return cnt

n = int(input())
k = int(input())

start = 1
end  = k

result = 0
while start <= end:
    mid  = (start + end) // 2

    if count(mid) >= k:
        result = mid
        end = mid -1
    else:
        start = mid + 1

print(result)
