# 무방향 그래프의 사이클 판별 (방향그래프의 사이클은 DFS 이용)
# 1. 모든 간선을 탐색하며.. 루트노드가 다르면 -> union 연산
# 2. 모든 간선을 탐색하며.. 루트노드가 같으면 -> 사이클이 발생


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

# 부모 리스트 초기화
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split()) # 간선 입력 (연결된 그래프 입력)

    # 간선에 연결된 두 노드의 소속 집합이 같다면 사이클이 발생한 것이다.
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    
    # 간선에 연결된 두 노드의 집합이 다르면 같은 집합으로 union해 준다.
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 X")