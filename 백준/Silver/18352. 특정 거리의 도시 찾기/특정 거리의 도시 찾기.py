# https://www.acmicpc.net/problem/18352
import sys
from collections import deque


n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    distance = [-1] * (n+1)
    distance[start] = 0

    while q:
        node = q.popleft()
        
        for next_node in graph[node]:
            if distance[next_node] == -1:   # 방문 x
                distance[next_node] = distance[node] + 1    # 다음 노드 거리 = 현재 노드의 최단거리 + 1
                q.append(next_node)

    return distance

distance = bfs(x)

result = [i for i in range(len(distance)) if distance[i] == k]

if not result:
    print(-1)
else:
    result.sort()
    for value in result:
        print(value)



        
               