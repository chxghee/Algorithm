# https://www.acmicpc.net/problem/2178
from collections  import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0))
    maze[0][0] = 2

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m and maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    
    return maze[n-1][m-1] - 1

print(bfs())
    