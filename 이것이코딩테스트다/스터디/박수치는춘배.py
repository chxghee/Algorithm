# https://www.acmicpc.net/problem/30404
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
x = list(map(int, input().split()))

count = 1
end_time = x[0] + k

for i in range(1, n):
    now = x[i]

    if now > end_time:
        count += 1
        end_time = now + k

print(count)