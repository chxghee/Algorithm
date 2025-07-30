# https://www.acmicpc.net/problem/1916
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b ,w = map(int, input().split())
    graph[a].append((b, w))

start ,end = map(int, input().split())

def find_smallest_node():

    min_w = INF
    node = 0
    for i in range(1,n+1):
        if distance[i] < min_w and visited[i] == False:
            min_w = distance[i]
            node = i
    
    return node

def dijkstra_simple(start,end):
    visited[start] = True
    distance[start] = 0

    for adj in graph[start]:
        distance[adj[0]] = adj[1]
    
    for _ in range(n-1):
        node = find_smallest_node()
        visited[node] = True

        
        for adj in graph[node]:
            e, w = adj
            distance[e] = min(distance[node] + w, distance[e])
    
    return distance[end]


def dijkstra_heap(start, end):
    
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:

        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for adj in graph[now]:
            adj_node, w = adj

            cost = w + dist
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                heapq.heappush(heap, (cost, adj[0]))

    return distance[end]

print(dijkstra_heap(start, end))
    


