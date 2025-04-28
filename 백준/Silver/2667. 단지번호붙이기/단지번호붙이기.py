# https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline



def dfs(apt, sx, sy):
    
    stack = []
    stack.append((sx,sy))
    cnt = 0

    while stack:
        nx, ny = stack.pop()

        if data[nx][ny] == 1:
            data[nx][ny] = apt
            cnt += 1

            for i in range(4):
                cx = nx + dx[i]
                cy = ny + dy[i]
                if 0 <= cx < n and 0 <= cy < n and data[cx][cy] == 1:
                    stack.append((cx, cy))

    return cnt





n = int(input())
data = [list(map(int,input().rstrip())) for _ in range(n)]

# 시계방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = []
apt = 2
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            cnt = dfs(apt, i, j)
            result.append(cnt)
            apt += 1

result.sort()
print(len(result))
for val in result:
    print(val)
