# https://www.acmicpc.net/problem/25706
import sys
input = sys.stdin.readline

def get_next_position(now, jump):
    if now + jump > n:
        return n+1
    return now + jump + 1


n = int(input())
h = list(map(int, input().split()))
dp = [0] * (n+2)
dp[n] = 1

for i in range(n-1,0,-1):
    
    if h[i-1] == 0: # 현재 칸이 점프대가 아니면
        dp[i] = dp[i+1] + 1

    else:
        next_position = get_next_position(i, h[i-1])
        dp[i] = dp[next_position] + 1


if n == 1:
    print(dp[1])
    exit(0)

for i in range(1, n+1):
    print(dp[i], end=' ')

