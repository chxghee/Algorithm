# https://www.acmicpc.net/problem/15649
# 백트래킹으로 순열 구하기

import sys
input = sys.stdin.readline
n,m = map(int, input().split())


def back_tracking(depth):
    
    if depth == m:
        print(*result)
        return


    for i in range(1, n+1):
        if visited[i]:
            continue
        
        result.append(i)
        visited[i] = True
        back_tracking(depth + 1)
        visited[i] = False
        result.pop()


    

visited = [False] * (n+1)
result = []
depth = 0

back_tracking(depth)
