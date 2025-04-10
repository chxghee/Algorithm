# https://www.acmicpc.net/problemset?sort=ac_desc&algo=127

# DFS BFS에서 방문 처리 시점은 중요하지 않다. 
# 탐색 순서를 확인하려면 자료구조에서 pop된 시점에 기록하면 된다.

import sys
input = sys.stdin.readline


def dfs(x, y):
    stack = []
    stack.append((x,y))
    data[x][y] = 2  # 방문처리 2

    while stack:
        nx, ny = stack.pop()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < m and data[cx][cy] == 1:
                data[cx][cy] = 2
                stack.append((cx, cy))



dx = [-1,0,1,0]
dy = [0,1,0,-1]

t = int(input())

for i in range(t):

    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    for i in range(k):
        y, x = map(int, input().split())
        data[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                dfs(i,j)
                result += 1

    print(result)


    

