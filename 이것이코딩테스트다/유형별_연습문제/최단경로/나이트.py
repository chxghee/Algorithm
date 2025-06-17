# https://www.acmicpc.net/problem/7562
from collections import deque
import sys
input = sys.stdin.readline

# 시계방향
dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

def calc_min_path(size, start, target):

    if start == target:
        return 0

    visited = [[False] * size for _ in range(size)]
    
    q = deque()
    q.append((start[0], start[1], 0))       # + 이동 횟수
    visited[start[0]][start[1]] = True

    while q:

        x, y, depth = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
                if [nx, ny] == target:
                    return depth + 1
                visited[nx][ny] = True
                q.append((nx, ny, depth + 1))



n = int(input())

for _ in range(n):
    l = int(input())
    start = list(map(int,input().split()))
    target = list(map(int,input().split()))
    print(calc_min_path(l,start, target))



