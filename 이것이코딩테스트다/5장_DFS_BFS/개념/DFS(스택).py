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
    
    # 방문할   방문한
    stack, visited = [], []

    stack.append(start)
    

    # 스택이 비어있게 되면 탐색이 종료된다.
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.append(node)

            # 현재 노드와 연결된 노드 중 방문하지 않은 노드를 스택에 추가
            # (뒤에 추가된 노드가 먼저 탐색되도록 역순으로 추가)
            # extend()는 괄호 안의 리스트를 스택에 한번에 추가
            stack.extend(reversed(graph[node])) 

    return visited

print(dfs(graph, 1))

