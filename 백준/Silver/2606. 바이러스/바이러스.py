# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline


def dfs(start):
    stack = []
    visited = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    
    return visited


n = int(input())
edge = int(input())
graph = [[] for _ in range(n+1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(1)
print(len(result) - 1)