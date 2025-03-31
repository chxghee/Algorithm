# https://www.acmicpc.net/problem/16236
from collections import deque
import sys
input = sys.stdin.readline

def bfs():

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    q = deque()
    q.append((shark[0], shark[1], 0))   # 상어 x,y,dist

    visited = [[False] * n for i in range(n)]
    visited[shark[0]][shark[1]] = True

    fish = []
    min_dist = float('inf')

    while q:
        nx, ny, dist = q.popleft()

        if dist > min_dist:
            break

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < n and not visited[cx][cy]:
                if data[cx][cy] <= shark[2]:    # 크기가 작거나 같아야 이동가능
                    q.append((cx,cy,dist+1))
                    visited[cx][cy] = True

                    # 먹을 수 있으면 리스트에 추가
                    if 0 < data[cx][cy] < shark[2]:
                        fish.append((dist+1,cx,cy))
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

q = bfs()       # 현재 가까운 물고기 반환

while q:
    dist, x, y = q
    time += dist    # 이동

    shark_x , shark_y, size, eat_cnt = shark

    data[shark_x][shark_y] = 0

    shark_x = x
    shark_y =  y
    eat_cnt += 1

    if eat_cnt == size:    # 내 크기만큼 먹었으면
        size += 1
        eat_cnt = 0
    
    shark = (shark_x , shark_y, size, eat_cnt)


    q = bfs()

print(time)



