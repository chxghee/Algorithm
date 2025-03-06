
# 서로소 집합의 연산 
# 1.find - 해당 수가 속한 집합을 찾는다.  (그래프에서 "노드"를 의미)
# 2.unoin - 해당 수가 속한 집합을 합친다. (그래프에서 "간선"을 의미)


# 사용 예시 - 무방향 그래프의 사이클 판별 (방향그래프의 사이클은 DFS 이용)
# -> 1. 모든 간선을 탐색하며.. 루트노드가 다르면 -> union 연산
# -> 2. 모든 간선을 탐색하며.. 루트노드가 같으면 -> 사이클이 발생


import sys
input = sys.stdin.readline

# 1. find 연산 - 특정 원소가 속한 집합을 찾기
# 여기서 집합을 찾는 방법은 자신이 속한 트리의 루트노드가 소속이 된다.
# 이때 경로 압축법을 사용하여 같은 소속의 집합은 루트 노드를 부모로 갖은 것으로 최적화 -> 그러면 unoin이 O(V*연산개수) 에서 줄어들게 된다.
def find_parent(parent, x):
    
    if parent[x] != x:      # 루트 노드는 자기 자신이 부모인 경우이므로 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 2. union 연산 - 두 원소가 속한 집합을 합침
# 작은 노드가 부모가 되도록 (큰 값이 작은 값을 가르킴)
def union_parent(parent, a, b):
    a = find_parent(parent, a)      # 현재 내가 속한 집합을 찾는다 (루트노드를 찾는다)
    b = find_parent(parent, b)
    
    # 크기에 따라 루트 노드를 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i


for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print("********* 각 원소가 속한 집합 출력 *********")
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print("********* 부모 테이블 정보 출력 *********")
for i in range(1, v+1):
    print(parent[i], end=' ')


"""
6 4
1 4
2 3
2 4
5 6
"""