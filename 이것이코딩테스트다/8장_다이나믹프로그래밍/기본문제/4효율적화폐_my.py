import sys

n,m = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

money.sort()

dp = [0] * (m+1)

for i in range(money[0], m+1):
    
    if i in money:
        dp[i] = 1
    
    else:
        min_cnt = float("inf")
        for j in range(1,i):
            if dp[j] != 0 and dp[i-j] != 0:
                min_cnt = min(dp[j] + dp[i-j], min_cnt)
        
        if min_cnt == float("inf"):
            dp[i] = 0
        else:
            dp[i] = min_cnt

if dp[m] == 0:
    print(-1)
else:
    print(dp[m])
            