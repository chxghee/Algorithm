# https://www.acmicpc.net/problem/14502
import sys
import copy
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0


def check_safty():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        result = max(result, check_safty())
        return 

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)



