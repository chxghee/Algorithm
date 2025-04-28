# https://www.acmicpc.net/problem/10026
import sys
import copy
input = sys.stdin.readline


def normal_visit_proc(x, y):
    if data[x][y] == 'R':
        return 'r'
    if data[x][y] == 'G':
        return 'g'
    if data[x][y] == 'B':
        return 'b'
    return data[x][y]

def normal_dfs(data, x,y):
    stack = []
    stack.append((x,y))
    target = data[x][y]
    data[x][y] = normal_visit_proc(x,y)
    

    while stack:
        nx, ny = stack.pop()

        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx < n and 0 <= cy < n and data[cx][cy] == target:
                data[cx][cy] = normal_visit_proc(cx,cy)
                stack.append((cx,cy))
                

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
data = [list(input().rstrip()) for _ in range(n)]

result = 0
data2 = copy.deepcopy(data)
for i in range(n):
    for j in range(n):
        if 'A' <= data2[i][j] <= 'Z':
            normal_dfs(data2,i,j)
            result += 1

for i in range(n):
    for j in range(n):
        if data[i][j] == 'G':
            data[i][j] = 'R'

r2 = 0
for i in range(n):
    for j in range(n):
        if 'A' <= data[i][j] <= 'Z':
            normal_dfs(data,i,j)
            r2 += 1


print(result, r2)
