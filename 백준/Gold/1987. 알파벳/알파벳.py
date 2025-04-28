# https://www.acmicpc.net/problem/1987
import sys
input = sys.stdin.readline

def dfs(x,y):
    stack = []
    stack.append((x,y, data[x][y]))

    max_len = 1
    

    while stack:
        nx, ny, visited = stack.pop()
        max_len = max(max_len, len(visited))

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]
        
            if 0 <= cx < n and 0 <= cy < m and data[cx][cy] not in visited:
                stack.append((cx,cy, visited + data[cx][cy]))
    
    return max_len



dx = [-1,0,1,0]
dy = [0,1,0,-1]

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]


print(dfs(0,0))
