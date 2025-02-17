# https://www.acmicpc.net/problem/1932
import sys

def find_adj_max(x,y):
    if i - 1 == -1:
        return 0
    if j - 1 == -1:
        return tri[i-1][j]
    if j == len(tri[i-1]):
        return tri[i-1][j-1]
    
    return max(tri[i-1][j], tri[i-1][j-1])


n = int(sys.stdin.readline().rstrip())
tri = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tri.append(row)

# 왼쪽 대각선 : i-1, j
# 오른쪽 대각선 : i-1, j-1 
dp = tri

for i in range(n):
    for j in range(i+1):
        dp[i][j] = dp[i][j] + find_adj_max(i,j)

print(dp)

print(max(dp[n-1]))
