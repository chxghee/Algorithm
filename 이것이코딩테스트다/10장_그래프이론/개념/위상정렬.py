# 위상정렬 - 순서가 정해진 일련의 작업을 차례대로 수행해야 할 때 사용한다.
# 1. 진입차수가 0 인 노드를 큐에 삽입
# 2. 큐가 빌 때까지...
    # 2-1 큐에서 원소를 꺼내고 해당 노드에서 출발하는 간선을 그래프에서 제거
    # 2-2 새롭게 진입차수를 계산하여 0이 된 노드를 큐에 삽입

# 이때 모든 노드를 방문하기 전에 큐가 비게 된다면 사이클이 있는 것이다.

# 시간 복잡도 O(V+E) - 모든 간선과 노드를 탐색하므로

import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[] for _ in range(v+1)]

# 그래프 작성
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 큐에 진입 차수 0 인 노드 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)

        for adj in graph[node]:
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''