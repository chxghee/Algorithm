# https://www.acmicpc.net/problem/1753
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 가장 짧은 거리를 가지고 있는 노드의 인접 노드
        for adj in graph[now]:
            end, weight = adj
            cost = distance[now] + weight

            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(q, (cost, end))




v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

distance = [INF] * (v+1)

for i in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

    
dijkstra(start)
    

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
