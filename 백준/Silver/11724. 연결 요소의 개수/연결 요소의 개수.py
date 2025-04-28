# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline


def dfs(start):
    
    if visited[start]:
        return 0

    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        node = stack.pop()
        
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    
    return 1

    


n, e = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(e):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, n+1):
    if dfs(i):
        result += 1
    

print(result)