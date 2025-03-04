# 크루스칼 알고리즘 (그리디 알고리즘)

# 최소 신장 트리 - 최소한의 비용으로 신장트리를 찾는것
# 신장트리란? -모든 노드를 연결하지만 사이클이이 존재하지 않는 그래프.

# 1. 모든 간선을 가중치로 작은 순으로 오름차순 정렬
# 2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생하는지 확인
#    2-1 사이클이 없으면 해당 간선을 신장트리에 포함한다.
#    2-2 사이클이 있으면 해당 간선을 신장트리에 포함 X.
# 이때 사이클을 찾는 방법은 서로소 집합을 이용한다.

# 시간 복잡도 O(ElogE) <- 간선 정렬에 시간이 오래걸리기 때문

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


v, e = map(int, input().split())

# 부모 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


# 간선 정보를 담을 리스트, 비용을 담을 cost
edges = []
min_cost = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w,a,b))

# 1. 오름차순 정렬
edges.sort()

# 2. 간선 전체 탐색
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 최소신장트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost

print(min_cost)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''