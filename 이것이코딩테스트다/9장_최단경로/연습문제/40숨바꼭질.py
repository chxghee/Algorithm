import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:

    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for adj in graph[now]:
        cost = dist + adj[1]
        if cost < distance[adj[0]]:
            distance[adj[0]] = cost
            heapq.heappush(q, (cost, adj[0]))









print(distance)

node_info = []

m = 0
for val in distance:
    if val != INF:
        m = max(m, val)

cnt = 0
for i in range(1, n + 1):
    if distance[i] == val:
        node_info.append(i)
        cnt += 1


print(min(node_info), m, cnt-1)


    



