import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def dfs(x, y):

    if x >= n or x <= -1 or y >= m or y <= -1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)


# 재귀함수를 이용한 DFS구현 (그래프, 시작 노드, 방문정보 리스트)
def dfs1(graph, v, visited):
    
    visited[v] = True   # 현재 노드 방문 처리
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
        
        