# https://www.acmicpc.net/problem/2606
# 기본 중에 기본 문제 세가지 방법으로 풀 수 있다
# 1. BFS
# 2. DFS
# 3. union find



import sys
from collections import deque
input = sys.stdin.readline


# union find 로 풀기
def find_parent(parent, x):
    if parent[x] != x:  # 최상단 부모가 아닐 때
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b





def dfs(now, visited):
    global cnt
    
    visited[now] = True
    cnt += 1

    for adj in graph[now]:
        
        if not visited[adj]:    # 방문한적 없다면
            dfs(adj, visited)
            
def bfs(start, visited):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        visited[node] = True
        

        for adj in graph[node]:
            if not visited[adj]:
                q.append(adj)

    return visited.count(True)



n = int(input())
edge = int(input())
graph = [[] for _ in range(n+1)]



# 서로소 집합으로 풀기
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i


for i in range(edge):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
visited = [False] * (n+1)

# dfs(1, visited)
# print(cnt - 1)

# print(bfs(1, visited) - 1)


for i in range(1, n+1):
    parent[i] = find_parent(parent, i)

un = parent[1]
print(parent.count(un) - 1)
