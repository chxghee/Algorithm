import sys
import heapq

INF = 1e9
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 로직 


# 1 -> X 로 가는 경로 중 k를 거쳐 최소로 가는 방법
for now in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][now] + graph[now][b])

result = graph[1][k] + graph[k][x]
if result >= INF:

    print(-1)
else:
    print(result)

