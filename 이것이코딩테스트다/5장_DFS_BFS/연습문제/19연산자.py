# https://www.acmicpc.net/problem/14888
import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
add_cnt, sub_cnt, mul_cnt, div_cnt = map(int, sys.stdin.readline().split())

max_val = -float('inf')
min_val = float('inf')

def dfs(i, now):
    global max_val, min_val, add_cnt, sub_cnt, mul_cnt, div_cnt

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add_cnt > 0:
            add_cnt -= 1
            dfs(i+1, now + a[i])
            add_cnt += 1
        if sub_cnt > 0:
            sub_cnt -= 1
            dfs(i+1, now - a[i])
            sub_cnt += 1
        if mul_cnt > 0:
            mul_cnt -= 1
            dfs(i+1, now * a[i])
            mul_cnt += 1
        if div_cnt > 0:
            div_cnt -= 1
            dfs(i+1, int(now / a[i]))
            div_cnt += 1
            



dfs(1,a[0])
print(max_val)
print(min_val)