import sys
from bisect import bisect_left, bisect_right

n,x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start = bisect_left(data, x)
end = bisect_right(data, x)
print(start, end)
result = end-start 

if  result <= 0:
    print(-1)
else:
    print(result)
