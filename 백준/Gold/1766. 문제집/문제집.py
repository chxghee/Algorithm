# https://www.acmicpc.net/problem/1766
import heapq
import sys
input = sys.stdin.readline

# 우선순위가 있는 위상정렬은 어떻게 풀것인가?
# 힙을 이용해서 풀수 있는 이유
# 진입 차수가 0인 문제들을 힙에 넣어두면 번호가 가장 작은 문제부터 자동으로 나옴

n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():

    heap = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)    
    
    result = []
    
    while heap:

        node = heapq.heappop(heap)
        result.append(node)

        for adj in graph[node]:
            indegree[adj] -= 1

            if indegree[adj] == 0:
                heapq.heappush(heap, adj)

    return result

for val in topology_sort():
    print(val, end=' ')


