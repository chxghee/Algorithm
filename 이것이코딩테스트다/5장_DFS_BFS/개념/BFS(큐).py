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

def bfs(graph, start):

    queue = deque()
    visited = []

    queue.append(start)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

print(bfs(graph, 1))
