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

# 재귀함수를 이용한 DFS구현 (그래프, 시작 노드, 방문정보 리스트)
def dfs(graph, v, visited):
    
    visited[v] = True   # 현재 노드 방문 처리
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
        
        


# 탐색 종료 base 케이스 1. 현재 노드와 인접한 노드 모두 방문 했을 때

dfs(graph, 1, visited)