# 플로이드 워셜 알고리즘 
# -> 동적계획법을 이용한 모든 노드에서 모든 노드로 가는 최단거리를 구하는 알고리즘
# O(n^3)

import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

# 1. 각 최단거리를 저장할 그래프(DP테이블)을 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 1-1 주대각 0으로 초기화 (자기자신으로가는것)
for i in range(1, n+1):
    graph[i][i] = 0

# 1-2 간선 정보 입력
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w

# 2. 플로이드 워셜 알고리즘 점화식 Dab = min(Dab, Dak + Dkb) -> O(n^3)
for now in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][now] + graph[now][b])

# 3. 결과 출력
print("************ 실행결과 ************")

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("도달 불가", end=" ")
        else:
            print(graph[a][b], end=" ")

    print()

