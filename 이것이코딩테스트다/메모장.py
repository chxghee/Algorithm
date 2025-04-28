# https://www.acmicpc.net/problem/16236
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [-1,0,1,0]     # 북에서 부터 반시계이기 때문에
    dy = [0,-1,0,1]

    q = deque()
    q.append((shark[0],shark[1], 0))        # 상어 위치, 거리
    
    fish = []
    min_dist = float('inf')
    
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True

    while q:
        x, y, dist = q.popleft()

        if dist > min_dist:
            break

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:

                if data[nx][ny] <= shark[2]:

                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = True

                    if 0 < data[nx][ny] < shark[2]: # 먹을 수 있으면
                        fish.append((dist+1, nx, ny))
                        min_dist = dist + 1
    
    if fish:
        fish.sort()
        return fish[0]
    
    return None
     

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark = (i,j,2, 0)      # 위치 크기 먹은 애들 개수

time = 0

f = bfs()

while f:

    dist, x, y = f

    shark_x,shark_y, size, eat_cnt  = shark

    # move
    data[shark_x][shark_y] = 0
    shark_x, shark_y = x, y
    time += dist
    eat_cnt += 1
  

    if size == eat_cnt:
        size += 1
        eat_cnt = 0
    shark = (shark_x,shark_y, size, eat_cnt)

    f = bfs()

print(time)
