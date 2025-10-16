# https://www.acmicpc.net/problem/11559
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]

ROW = 12
COL = 6


def bfs(x, y):
    global pop_list, visited

    groups = []    
    queue = deque()
    color = puyo[x][y]
    queue.append((x,y))
    groups.append((x,y))
    visited[x][y] = True

    while queue:
        nx, ny = queue.popleft()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if on_position(cx, cy) and puyo[cx][cy] == color and not visited[cx][cy]:
                visited[cx][cy] = True
                queue.append((cx,cy))
                groups.append((cx,cy))

    return groups


def on_position(x, y):
    return 0<= x < ROW and 0<= y < COL


def pop_puyo(pop_list):
    for x, y in pop_list:
        puyo[x][y] = "."


def sort_puyo():

    for c in range(COL):
        down_puyos = []
        for r in range(11, -1, -1):
            if puyo[r][c] != '.':
                down_puyos.append(puyo[r][c])
                puyo[r][c] = '.'    # 빈칸으로 칠하기
        
        r = 11
        for down_puyo in down_puyos:
            puyo[r][c] = down_puyo
            r -= 1
        

puyo = [list(input().rstrip()) for _ in range(ROW)]

result = 0
while True:
    
    pop_list = []
    visited = [[False] * COL for _ in range(ROW)]
    
    
    # BFS 로직
    for i in range(ROW):
        for j in range(COL):
            if puyo[i][j] != '.' and not visited[i][j]:
                groups = bfs(i,j)
                
                if len(groups) >= 4:
                    pop_list.extend(groups)

    
    # pop_list 없애기
    pop_puyo(pop_list)

    # 재정렬 -> 아래로 이동
    sort_puyo()


    if len(pop_list) == 0:
        break

    result += 1
    

print(result)
