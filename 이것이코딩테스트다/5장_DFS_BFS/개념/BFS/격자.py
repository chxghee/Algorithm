from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(sx, sy):

    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True

    while q:
        x,y = q.pop()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = True


   

def bfs(sx, sy):
    
    q = deque()
    q.appned((sx,sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = True


    




count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
