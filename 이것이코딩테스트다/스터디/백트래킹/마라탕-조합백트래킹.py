# https://www.acmicpc.net/problem/28447 
# 조합 백트래킹을 이용한 풀이
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

picked = []
result = -int(1e9)


def dfs(start, depth):
    global result

    if depth == k:      # 완성이 되었을때 계산을 해 본다.
        local = 0
        for i in range(k):
            for j in range(i+1,k):
                local += data[picked[i]][picked[j]]

        result = max(result, local)
        return
    
    for i in range(start, n):
        picked.append(i)
        dfs(i + 1, depth + 1)
        picked.pop()
        
dfs(0,0)
print(result)


