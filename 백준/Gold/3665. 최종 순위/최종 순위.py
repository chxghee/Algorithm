from collections import deque
import sys
input = sys.stdin.readline

def make_graph(t, change):

    graph = [[False] *(n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[t[i]][t[j]] = True
            indegree[t[j]] += 1
    
    for val in change:
        x, y = val
        if graph[x][y]:
            graph[x][y] = False
            graph[y][x] = True
            indegree[x] += 1
            indegree[y] -= 1
        else:
            graph[x][y] = True
            graph[y][x] = False
            indegree[x] -= 1
            indegree[y] += 1
            
    return graph, indegree


def topology_sort(graph, indegree):
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
        
    cycle = False
    ambi = False

    for _ in range(1, n+1):
     
        if len(q) == 0: # 사이클
            cycle = True
            break
        if len(q) >= 2: # 순서 모호
            ambi = True
            break
        
        node = q.popleft()
        result.append(node)

        for i in range(1, n+1):
            if graph[node][i]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif ambi:
        print("?")
    else:
        for val in result:
            print(val, end=" ")
        print()
        
a = int(input())

for _ in range(a):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    change = []
    for _ in range(m):
        x, y = map(int, input().split())
        change.append((x, y))
    graph, indegree = make_graph(t, change)
    topology_sort(graph, indegree)
    

