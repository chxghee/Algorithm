from collections import deque
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

graph = [[] for _ in range(n)]
edges = []
parent = [i for i in range(n)]

full_cost = 0
# 입력
for i in range(m):
    x, y, z = map(int, input().split())
    edges.append((z,x,y))
    full_cost += z



edges.sort()
result = 0
for edge in edges:
    cost, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        result += cost
        union_parent(parent, x, y)

print(full_cost - result)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''