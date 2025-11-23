# https://www.acmicpc.net/problem/23029
import sys
input = sys.stdin.readline

n = int(input())
food = [0]
food += [int(input()) for _ in range(n)]
dp = [0] * (n+1)


if n == 1:
    print(food[1])
    exit(0)

if n == 2:
    print(max((food[1] + food[2] // 2), food[2]))
    exit(0)


dp[1] = food[1]
dp[2] = max((food[1] + food[2] // 2), food[2])
dp[3] = max(dp[2], (food[2] + food[3] // 2), food[3] + dp[1])



for i in range(3, n+1):
    eat_prev = dp[i-3] + food[i] // 2 + food[i-1]
    not_eat_prev = dp[i-2] + food[i]
    not_eat = dp[i-1]
    dp[i] = max(eat_prev, not_eat_prev, not_eat)

print(dp[n])






# DP: 해당 위치에서 최대 먹을수 있는 양
# i 단계에서..
# 1. i를 먹고, 이전을 먹지 않는 경우
# 2. i를 먹고, 이전을 먹는 경우
# 3. i를 먹지 않는 경우
# 1 2 4 3 2 2
