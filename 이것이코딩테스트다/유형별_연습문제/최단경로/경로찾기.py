# https://www.acmicpc.net/problem/11403
# 내 풀이 bfs -> O(n^3)

from collections import deque
import sys
input = sys.stdin.readline

def find_adj(q, node):
    
    if not q:
        return
    
    adj_list = set(q)
    
    while q:
        adj = q.popleft()
        for k in range(n):
            if matrix[adj][k] == 1:
                if k not in adj_list:
                    adj_list.add(k)
                    q.append(k)

    for val in adj_list:
        matrix[node][val] = 1


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    q = deque()
    for j in range(n):    
        if matrix[i][j] == 1:
            q.append(j)
    find_adj(q, i)


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()



