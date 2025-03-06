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

def is_same_team(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n):
    parent[i] = i

for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        union_parent(parent, a, b)
        
    else:
        is_same_team(parent, a, b)
    

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''