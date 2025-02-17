# https://www.acmicpc.net/problem/2110
import sys
from bisect import bisect_left, bisect_right

n, c = map(int, sys.stdin.readline().split())

data = []
for _ in range(n):
    x = int(sys.stdin.readline().split())
    data.append(x)

data.sort()

# 공유기 사이의 최대 거리를 이분탐색으로 줄이면서 해를 찾는 문제 
start = 1
end = data[-1] - data[0]
result = 0

while (start <= end):
    mid = (start + end) // 2        # gap
    val = data[0]                   # 시작 위치에 공유기 설치
    count = 1

    for i in range(1,n):
        if data[i] >= val + mid:
            val = data[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid -1
