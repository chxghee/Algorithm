
# 서로소 집합의 연산 
# 1.find - 해당 수가 속한 집합을 찾는다.
# 2.unoin - 해당 수가 속한 집합을 합친다.



import sys
input = sys.stdin.readline

# 1. find 연산 - 특정 원소가 속한 집합을 찾기
# 여기서 집합을 찾는 방법은 자신이 속한 트리의 루트노드가 소속이 된다.
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