# https://www.acmicpc.net/problem/14501

# 전략 -> 뒤에서 부터 하는 방법도 생각하기 (즉 확정할 수 있는 방향에서부터 차근차근 쌓아가는 것에 dp)

import sys

n = int(sys.stdin.readline().rstrip())
t=[]
p=[]
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

# dp는 i 부터 막날까지 낼수 있는 수익의 최대라고 하자
dp = [0] * (n+1)
max_val = 0

for i in range(n-1,-1,-1):
    time = i + t[i]

    if time <= n:   # 날짜 내에 할 수 있다면
        dp[i] = max(max_val, p[i] + dp[time])
        max_val = dp[i]

    else:       # 날짜를 초과 하면
        dp[i] = max_val

print(max_val)

