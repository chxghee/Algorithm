# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    stack, visited = [], []
    stack.append(start)
    

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            stack.extend(reversed(graph[node]))

        

def bfs(start):
    q = deque()
    visited = [False] * (n + 1)

    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        print(node, end=' ')
        
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj]  = True
                q.append(adj)


n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)] 
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


dfs(v)
print()
bfs(v)