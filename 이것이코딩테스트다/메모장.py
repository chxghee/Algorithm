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

def bfs(start):
    visit = []
    q = deque([start])
    visit.append(start)

    while q:
        now = q.popleft()
        
        for adj in graph[now]:
            if adj not in visit:
                q.append(adj)
                visit.append(adj)
    return visit

print(bfs(1))