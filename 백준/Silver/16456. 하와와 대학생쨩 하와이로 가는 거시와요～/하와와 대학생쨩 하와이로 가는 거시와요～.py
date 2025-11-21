# https://www.acmicpc.net/problem/16456

n = int(input())

# 현재 위치의 경우의 수를 구하려면...
# 바로 다음 위치로 이동
# 2칸 전에서 바로 이동하는 경우의 수 =   2칸 뛰고 -1 의 과 2 1 하는 경우
# 1칸 전에서
# 2 -> 1
# 3 -> 1 1 / 2 -1
# 4 -> 1 2 -1 / 111 / 2 -1 2 -1
# 5 -> 112-1 / 2 -1 2 1 // 1 2 -1 2 / 1111
# 6 ->


if n == 1:
    print(1)
    exit()
if n == 2:
    print(1)
    exit()
if n == 3:
    print(2)
    exit()
    
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2


for i in range(4, n+1):
    dp[i] = (dp[i-1] + dp[i-3]) % 1_000_000_009


print(dp[n])