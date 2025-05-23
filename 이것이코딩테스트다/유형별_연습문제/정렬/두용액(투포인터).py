# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

data.sort()

left = 0
right = n-1
min_sum = int(1e9)
result = ()


while left < right:
    s = data[left] + data[right]

    if abs(s) <= min_sum:
        min_sum = abs(s)
        result = (data[left], data[right])
    
    if s < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])





