import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# n <= 30000 
# 워셜의 경우 o(n^3) ->
# 다익스트라 -> o(ElogV) 
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

distance = [INF] * (n+1)



def dijkstra(start):

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))

# 로직


dijkstra(c)

cnt = 0
max_d = 0
for val in distance:
    if val != INF:
        cnt += 1
        max_d = max(max_d, val)

print(cnt - 1, max_d)
