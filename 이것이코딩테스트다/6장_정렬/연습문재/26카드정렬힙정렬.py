# https://www.acmicpc.net/problem/1715
import sys
import heapq

h = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    heapq.heappush(h, data)


result = 0

while len(h) != 1:

    a = heapq.heappop(h)
    b = heapq.heappop(h)

    x = a + b
    result += x
    heapq.heappush(h, x)


print(result)



