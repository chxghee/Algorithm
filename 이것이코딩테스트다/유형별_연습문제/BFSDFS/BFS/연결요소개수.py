# https://www.acmicpc.net/problem/11724
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    
    if visited[start]:
        return 0
    
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True

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
    if bfs(i):
        result += 1
    

print(result)