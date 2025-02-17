from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5,],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

# 스택를 이용한 DFS구현 (그래프, 시작 노드)
def dfs(graph, start):
    
    stack = deque()
    visited = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            stack.extend(reversed(graph[node]))

    return visited




print(dfs(graph, 1))

