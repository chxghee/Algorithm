# https://www.acmicpc.net/problem/14888
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
add_cnt, sub_cnt, mul_cnt, div_cnt = map(int, sys.stdin.readline().split())

max_val = -float('inf')
min_val = float('inf')

q = deque([(a[0],1, add_cnt, sub_cnt, mul_cnt, div_cnt)])

while q:
    now, idx, add, sub, mul, div = q.popleft()

    if n == idx:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        continue

    next_num = a[idx]

    if add>0:
        q.append((now + next_num, idx + 1, add-1, sub, mul, div))
    if sub>0:
        q.append((now - next_num, idx + 1, add, sub-1, mul, div))
    if mul>0:
        q.append((now * next_num, idx + 1, add, sub, mul-1, div))
    if div>0:
        q.append((int(now / next_num), idx + 1, add, sub, mul, div - 1))





print(max_val)
print(min_val)