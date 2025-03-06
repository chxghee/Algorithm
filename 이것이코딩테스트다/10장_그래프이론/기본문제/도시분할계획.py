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


n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
min_cost = 0
cost_list = []

for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        cost_list.append(cost)


result = sum(cost_list) - max(cost_list)
print(result)


        

    