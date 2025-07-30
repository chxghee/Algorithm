# https://www.acmicpc.net/problem/11403
# 워셜 -> O(n^3)

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


# 경유지
for i in range(n):
    for start in range(n):
        for end in range(n):
            if matrix[start][i] and matrix[i][end]:
                matrix[start][end] = 1
    


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


