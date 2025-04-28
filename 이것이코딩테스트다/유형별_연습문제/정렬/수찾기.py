# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

def has_number(val, start, end):

    if start > end:
        return 0
    
    mid = (start + end) // 2

    if data[mid] > val:
        return has_number(val, start, mid - 1)
    elif data[mid] < val:
        return has_number(val, mid + 1, end)
    else:
        return 1



n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
find = list(map(int, input().split()))

for val in find:
    result = has_number(val, 0, n-1)
    print(result)