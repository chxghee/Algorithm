import sys
from bisect import bisect_left, bisect_right  # bisect -> 정렬된 배열에서 두번째 인자가 들어갈 수 있는 위치를 반환

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
