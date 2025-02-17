import sys

a =  sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

def edit_dist(a,b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(m+1): # 가로 초기화
        dp[0][i] = i
    for i in range(n+1): # 세로 초기화
        dp[i][n] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:    # 같다면 
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[n][m]

dp = edit_dist(a,b)
print(dp)

    