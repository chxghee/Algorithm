import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for adj in data[1:-1]:
        indegree[i] += 1
        graph[adj].append(i)


def topology_sort():
    q = deque()
    result = copy.deepcopy(time)
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for adj in graph[node]:
            result[adj] = max(result[adj], result[node] + time[adj])
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    for i in range(1, n+1):
        print(result[i])

topology_sort()