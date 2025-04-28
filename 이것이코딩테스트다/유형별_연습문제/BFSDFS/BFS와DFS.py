# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline



def dfs(start):
    stack = []
    visited = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    
    for val in visited:
        print(val, end=' ')
        
def bfs(start):
    q = deque()
    visited = []

    q.append(start)
    visited.append(start)

    while q:
        node = q.popleft()
        

        for adj in graph[node]:

            if adj not in visited:
                visited.append(adj)
                q.append(adj)
    
    for val in visited:
        print(val, end=' ')




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