import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n)]
planet = [[] for _ in range(n)]

# 행성 정보 입력
for i in range(n):
    x,y,z = map(int, input().split())
    planet[i] = (x,y,z, i)

edges = []
for j in range(3):
    idx_sort = sorted(planet, key=lambda x: x[j])
    for i in range(n-1):
        cost = idx_sort[i+1][j] - idx_sort[i][j]
        edges.append((cost, idx_sort[i+1][3], idx_sort[i][3]))

edges.sort()

# # 가능한 간선 모두 구하기 -> 이렇게 하게 되면 n최대 100,000 이라 메모리 초과 및 시간 초과
# edges = []
# for i in range(n):
#     for j in range(i+1, n):        
#         cost = calulate_cost(planet[i], planet[j])
#         edges.append((cost, i, j))
# edges.sort()

result = 0
for edge in edges:
    cost , a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)
