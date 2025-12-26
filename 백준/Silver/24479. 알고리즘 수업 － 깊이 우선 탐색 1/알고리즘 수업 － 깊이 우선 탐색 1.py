# https://www.acmicpc.net/problem/24479
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(n+1):
    graph[i].sort()

order = [0] * (n+1)
count = 1

def dfs(now):
    global count

    if visited[now]:
        return
    
    visited[now] = True    
    order[now] = count
    count += 1

    
    for adj in graph[now]:

        dfs(adj)

dfs(r)

for i in range(1, n+1):
    print(order[i])

