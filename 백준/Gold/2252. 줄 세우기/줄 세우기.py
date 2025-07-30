# https://www.acmicpc.net/problem/2252
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 앞에 있는 녀석이 화살표를 받음
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)


def topology_sort():

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for adj in graph[node]:
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    return result

for val in topology_sort():
    print(val, end=' ')
            



