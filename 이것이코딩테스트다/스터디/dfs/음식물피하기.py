# https://www.acmicpc.net/problem/1743

# stack에 넣는 순간 방문 처리를 해야 한다.
import sys
input = sys.stdin.readline

def check(x,y):
    return (0 <= x < n) and (0 <= y < m)

def dfs(now):
    
    if hotel[now[0]][now[1]] != 1:
        return 0

    
    stack = []
    stack.append(now)
    hotel[now[0]][now[1]] = 2
    r = 1
    
    while stack:
        x, y = stack.pop()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny) and hotel[nx][ny] == 1:
                stack.append((nx,ny))
                r += 1
                hotel[nx][ny] = 2

    return r


dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m,k = map(int, input().split())
hotel = [[0] * m for _ in range(n)]

food = []
for _ in range(k):
    x , y = map(int,input().split())
    hotel[x-1][y-1] = 1
    food.append((x-1,y-1))

result = 0

# 모든 음식물에서 dfs를 돌리고, 가장 큰 depth를 가진 것이 정답
for node in food:
    depth = dfs(node)
    result = max(result, depth)

print(result)


"""
2 2 4
1 1
1 2
2 1
2 2

"""
