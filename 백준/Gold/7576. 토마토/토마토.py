# https://www.acmicpc.net/problem/7576
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()

    # 익은 토마토에서 동시에 같이 시작 해야함
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                q.append((i,j))

    while q:
        nx, ny = q.popleft()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < m and data[cx][cy] == 0:   # 익지 않은 토마토인 경우
                data[cx][cy] = data[nx][ny] +  1
                q.append((cx,cy))
    
    # 걸린 시간 계산
    day = -1
    for i in range(n):
        d = max(data[i])
        day = max(d, day)
    return day - 1


m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

result = bfs()

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result = -1

print(result)