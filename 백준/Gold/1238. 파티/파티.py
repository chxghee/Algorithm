# https://www.acmicpc.net/problem/1238
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, dst = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))


def dijckstra(start, end):

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
    
    return distance[end]

result = [0] * (n+1)

for i in range(1, n+1):
    result[i] = dijckstra(i, dst) + dijckstra(dst, i)

print(max(result))