import sys
import heapq
# O(ElogV)

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 각 노드 정버를 담을 리스트  (해당 행의 리스트에는 튜플로(목적지,비용) 을 저장)
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블(리스트) 무한대 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    # a -> b 로 가는 비용이 w
    a, b, w = map(int, input().split())
    graph[a].append((b, w))


def dijkstra(start):
    q = []

    # 시작 노드 방문처리
    heapq.heappush(q, (0, start))   # 힙에 (거리비용, 노드) 형식으로 저장한디.
    distance[start] = 0
    
    while q:    # 이때 간선의 개수만큼 힙에 넣어다가 뺀다 -> O(E)

        # 방문하지 않은 노드 중 최단 거리인 노드 반환 -> 힙을 이용해서 O(logV)으로 시간을 단축한다.
        dist, now = heapq.heappop(q) 

        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))


    
dijkstra(start)

for i in range(1, n+1):

    if distance[i] == INF:
        print("도달 x")
    else:
        print(distance[i])

