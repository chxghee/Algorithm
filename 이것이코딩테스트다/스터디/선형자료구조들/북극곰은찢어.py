# https://www.acmicpc.net/problem/25918
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

# 1. 가능한 짝꿍찾기 -> 같은게 연속으로 나오면 최소한 1일이 딜레이 됨
stack = []
max_continue_same = 1
same_count = 1

for c in s:

    if not stack: # empty
        stack.append(c)
        same_count = 1
        continue

    top = stack[-1]
    if top != c: 
        stack.pop()
        max_continue_same = max(max_continue_same, same_count)
        same_count = 1

    else:
        stack.append(c)
        same_count += 1
    
if stack:
    print(-1)
else:
    print(max_continue_same)
