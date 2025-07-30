# https://www.acmicpc.net/problem/2206
from collections import deque
import copy
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(data):
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,0,1))     # x, y, 벽 부순 횟수, 이동거리
    visited[0][0][0] = True


    while q:
        x, y, wall, dist = q.popleft()

        if x == n-1 and y == m-1:
            return dist 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and not visited[nx][ny][wall]:     # 다음 칸이 벽이 아니고, 아직 그 방문 안 했을 때
                    visited[nx][ny][wall] = True
                    q.append((nx, ny, wall, dist + 1))
                
                if data[nx][ny] == 1 and wall == 0 and not visited[nx][ny][1]:  # 벽이고 부순적 없고 부슨 벽을 방문하자 않았을떄
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, dist + 1))
        
    
    return -1


n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs(data))