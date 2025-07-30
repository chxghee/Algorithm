# https://www.acmicpc.net/problem/1753
# O(ElogV)

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):

    # 1. init dp table and distance info
    dp[start] = 0
    q = []
    heapq.heappush(q, (0, start))       # 가중치와 노드를 튜플로 삽입

    while q:
        dist, now = heapq.heappop(q)       # 가장 짧은 노드 get

        for adj in graph[now]:
            end, weight = adj

            cost = dp[now] + weight
            if cost < dp[end]:
                dp[end] = cost
                heapq.heappush(q, (cost, end))



v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

dp = [INF] * (v+1)

for i in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

    
dijkstra(start)
    

for i in range(1, v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
