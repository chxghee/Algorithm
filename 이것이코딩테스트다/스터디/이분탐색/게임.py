# https://www.acmicpc.net/problem/1072
import sys
input = sys.stdin.readline

def binary_search(start, end):
    global result

    if start > end:
        return

    mid = (start + end) // 2
    new = (y + mid) * 100 // (x + mid) 

    if new > rating:
        result = mid
        end = mid -1
        binary_search(start, end)
    
    else:
        start = mid + 1
        binary_search(start, end)


x, y = map(int, input().split())
rating = y * 100 // x 

if rating >= 99:
    print(-1)
    exit(0)

start = 1
end = int(1e9)
result = 0


binary_search(start, end)
print(result)

