# https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:  # 부모가 아니면
        parent[x] =  find_parent(parent[x], parent)         # 경로 압축 -> 경로 압축을 쓰게 되면 모든 노드에 대해 find_parent()를 꼭 해야함
    return parent[x]

def union_parent(a,b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

n, e = map(int, input().split())


edge = []
parent = [i for i in range(n+1)]

for i in range(e):
    a ,b = map(int, input().split())
    union_parent(a, b, parent)
    
result = set()

# 경로 압축했기 때문에 find를 꼭 해줘야 함 (적용이 안된 노드가 있을 수 있기 때문에)
for i in range(1, n+1):
    result.add(find_parent(i,parent))

print(len(result))