# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

def find_min(l, impossible_idx):
    mval = 1000000
    for i in range(3):
        if impossible_idx != i:
            mval = min(mval, l[i])
    return mval



n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [[0,0,0] for _ in range(n)]
dp[0] = data[0][:]

for i in range(1, n):

    for j in range(3):
        dp[i][j] = find_min(dp[i-1], j) + data[i][j]

    
print(min(dp[n-1]))