# https://www.acmicpc.net/problem/11404

import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = min(graph[a][b], w)


# 로직 구현 

# 플로이드 워셜 이용 모든 위치에서 모든 목적지로 가는 최소 비용 + 작은 n의 범위
# 점화식 : D = min(Dxy, Dxk + Dky)
# 최소값을 담을 자료구조 : 2차원 리스트 -> graph

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()