# https://www.acmicpc.net/problem/1238
# 다익스트라는 특정 출발지부터 다른 모든 노드의 최단 거리를 구할 수 있다.
# -> 그럼 어떤 목적지가 있을때 모든 노드에서 이 목적지로의 최단 거리를 구하려면?
# -> 그래프를 뒤집은뒤 최단 거리를 구하면 상당히 효율적으로 구할 수 있다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijckstra(start, graph):

    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))
    
    return distance

n, m, dst = map(int, input().split())

graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    reversed_graph[b].append((a, w))


result = [0] * (n+1)

go_party = dijckstra(dst, reversed_graph)
go_home = dijckstra(dst, graph)

print(max(map(sum, zip(go_party[1:], go_home[1:]))))
