# https://www.acmicpc.net/problem/1753
# O(V^2)

import sys
input = sys.stdin.readline

INF = int(1e9)

# 방문하지 않은 노드 중 가장 거리가 짧은 노드 반환. -> 힙을 통해 알고리즘 시간 단축 가능
def get_smallest_node():
    min_dist = INF
    node = 0

    for i in range(1, v+1):
        if min_dist > dp[i] and visited[i] == False:
            node = i
            min_dist = dp[i]
    return node
        


def dijkstra(start):

    # 1. init dp table and distance info
    visited[start] = True
    dp[start] = 0

    for adj in graph[start]:
        dp[adj[0]] = adj[1]

    # 2. update dp table 
    for _ in range(v-1):
        now = get_smallest_node()

        for adj in graph[now]:
            end, weight = adj
            dp[end] = min(dp[end], dp[now] + weight)


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

dp = [INF] * (v+1)
visited = [False] * (v+1)

for i in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

    
dijkstra(start)
    

for i in range(1, v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
