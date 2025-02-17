import sys
# O(v^2)

# 1. 각 노드에 대한 최단거리를 저장할 1차원 리스트 선언
# 2. 리스트를  순차탐색 하여 단계마다 방문x 노드 중 최단거리가 가장 짧은 노드 선택

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 각 노드 정버를 담을 리스트  (해당 행의 리스트에는 튜플로(목적지,비용) 을 저장)
graph = [[] for _ in range(n+1)]

# 방문한 노드 리스트 
visited =[False] * (n+1)

# 최단 거리 테이블(리스트) 무한대 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    # a -> b 로 가는 비용이 w
    a, b, w = map(int, input().split())
    graph[a].append((b, w))




# 방문하지 않은 노드 중 최단 거리인 노드 반환
def get_smallest_node():
    min_val = INF
    node = 0
    for i in range(1, n+1):
        
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            node = i
    return node

def dijkstra(start):

    # 시작 노드 방문처리
    distance[start] = 0
    visited[start] = True
    for adj in graph[start]:        # 시작 노드와 인접한 노드에 대해 거리를 저장 
        distance[adj[0]] = adj[1]

    for _ in range(n-1):        # 아직 방문 x 노드가 n-1개 니꺼 n-1번 반복
        # 가장 가까운 노드 방문처리
        now = get_smallest_node()
        visited[now] = True
        
        # 최단 경로 테이블 다시 계산  (이전 노드에서 방문 비용 | 현재 노드를 통한 방문 비용) 비교후 작은 값으로 설정
        for adj in graph[now]:
            distance[adj[0]] = min(distance[adj[0]], distance[now] + adj[1])

dijkstra(start)

for i in range(1, n+1):

    if distance[i] == INF:
        print("도달 x")
    else:
        print(distance[i])

