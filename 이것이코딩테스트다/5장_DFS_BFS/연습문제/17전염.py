# https://www.acmicpc.net/problem/18405

# bfs에서 시간 혹은 깊이를 큐에 같이 넣으면서 조절할 수 있다.

import sys
from collections import deque

# 입력
n, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())



queue = deque()
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            queue.append((data[i][j], i, j, 0))

queue = deque(sorted(queue))

dx = [-1,0,1,0]
dy = [0,-1,0,1]


while queue:
    virus, nx, ny, time = queue.popleft()

    if time == s:
        break

    for i in range(4):
        cx = dx[i] + nx
        cy = dy[i] + ny
    
    if 0 <= cx < n and 0 <= cy < n and data[cx][cy] ==0:
        data[cx][cy] = virus
        queue.append((virus, cx, cy, time + 1))

print(data[x-1][y-1])