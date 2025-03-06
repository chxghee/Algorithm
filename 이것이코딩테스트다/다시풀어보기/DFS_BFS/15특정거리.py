# https://www.acmicpc.net/problem/18352
import sys
from collections import deque

input = sys.stdin.readline

n,m,k,start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)

def bfs(start, end):
    result = []
    q = deque()
    q.append((start, 0))
    visited[start] = True
    
    while q:
        now, dist = q.popleft()
        
        for adj in graph[now]:
            if not visited[adj]:
                q.append((adj, dist + 1))
                visited[adj] = True
                
                if dist+1 == end:
                    result.append(adj)
    return result

result =  bfs(start, k)

if not result:
    print(-1)
else:
    result.sort()
    for val in result:
        print(val)


# 이 문제는 최단 거리 및 도달할수 있는 노드를 묻는 문제
# -> 때문에 최단거리 알고리즘으로 풀지 BFS로 풀지 고민
# 모든 노드의 거리가 1이므로 BFS로 선택