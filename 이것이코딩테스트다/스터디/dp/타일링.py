# https://www.acmicpc.net/problem/11726

n = int(input())


# 2 -> a a / s
# 3 -> a s / s a / aaa
# 4 -> aaaa / ss /asa / saa / aas
# 5 -> aaaa / 

# s 를 추가하는 방법 / a를 추가하는 방법

if n == 1:
    print(1)
    exit()

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2


for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)