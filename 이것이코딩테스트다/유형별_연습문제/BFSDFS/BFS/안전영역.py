# https://www.acmicpc.net/problem/2468
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,d,h):
    q = deque()
    q.append((x,y))
    d[x][y] = h

    while q:
        nx, ny = q.popleft()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < n and d[cx][cy] > h:
                d[cx][cy] = h
                q.append((cx,cy))

def find_safe_count(h):
    d = copy.deepcopy(data)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if d[i][j] > h:
                bfs(i,j,d,h)
                cnt += 1

    return cnt


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

max_h = -1
for val in data:
    m = max(val)
    max_h = max(max_h, m)

result = 0
for i in range(max_h):
    result = max(result, find_safe_count(i))

print(result) 
