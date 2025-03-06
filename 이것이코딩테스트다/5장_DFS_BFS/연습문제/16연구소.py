# https://www.acmicpc.net/problem/14502
import sys
import copy
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

coor = []
virus_positions = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            coor.append((i,j))
        if data[i][j] == 2:
            virus_positions.append((i,j))


def check_safty(lab):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                cnt += 1

    return cnt

def find_safe(lab):
    temp_lab = copy.deepcopy(lab)
    
    for x, y in virus_positions:
        dfs(temp_lab,x,y)

    return check_safty(temp_lab)


def dfs(lab, x,y):
    stack = [(x,y)]

    while stack:
        cx, cy = stack.pop()

        for dx, dy in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                stack.append((nx,ny))
    

# 1. 전체 좌표중 3개 벽을 치기 
new_walls = list(combinations(coor, 3))


# 2. 이 벽에 대해 바이러스 조사
safe = -1
for walls in new_walls:
    
    for x, y in walls:
        data[x][y] = 1
    safe = max(safe, find_safe(data))
    for x, y in walls:
        data[x][y] = 0

print(safe)



