import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a >= b:
        parent[a] = b
    else:
        parent[b] = a


G = int(input())
p = int(input())

parent = [i for i in range(G+1)]

result = 0

# 서로소 집합을 이용해 집합을 합쳐나가는데 이때 부모가 0 이 되면 모든 탑승구가 찼다는 얘기
for _ in range(p):
    g = int(input())
    f  = find_parent(parent, g)
    if f == 0:
        break
    union_parent(parent, g, f-1)
    result += 1

print(result)