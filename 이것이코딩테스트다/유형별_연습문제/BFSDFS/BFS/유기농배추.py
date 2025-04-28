# https://www.acmicpc.net/problemset?sort=ac_desc&algo=127

# DFS BFS에서 방문 처리 시점은 무조건 append시점에 하는 게 좋음 -> 왜냐면 중복된 노드가 자료구조에 들어갈 수 있기 때문 
# 탐색 순서를 확인하려면 자료구조에서 pop된 시점에 기록하면 된다.
from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x,y))
    data[x][y] = 2
    while q:
        nx, ny = q.popleft()
        

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < m and data[cx][cy] == 1:
                q.append((cx,cy))
                data[cx][cy] = 2
    


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
                bfs(i,j)
                result += 1

    print(result)
