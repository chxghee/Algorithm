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




n , m = map(int, input().split())

parent = [0] * (1+n)

for i in range(1,1+n):
    parent[i] = i


graph = [[] for _ in range(n)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(0, len(data)):
        if data[j] == 1:
            union_parent(parent, i, j + 1)


plan = list(map(int, input().split()))

flag = 0
p = find_parent(parent, plan[0])
for val in plan[1:]:
    if p != find_parent(parent, val):
        flag =1
        break

if flag == 1:
    print("NO")
else:
    print("YES")

print(parent)

'''
5 4
1 0 1 1 0
0 1 0 1 1
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''