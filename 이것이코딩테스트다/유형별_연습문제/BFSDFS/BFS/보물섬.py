# https://www.acmicpc.net/problem/2589
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    distance = [[-1] * m for _ in range(n)]
    distance[x][y] = 0
    max_dist = 0

    while q:
        nx, ny = q.popleft()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < m and data[cx][cy] == 'L' and distance[cx][cy] == -1:
                distance[cx][cy] = distance[nx][ny] + 1
                max_dist =  distance[cx][cy]
                q.append((cx,cy))

    return max_dist


n, m = map(int,input().split())
data = [list(input().rstrip()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            dist = bfs(i,j)
            result = max(result, dist)

print(result)