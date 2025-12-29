# https://www.acmicpc.net/problem/1182
import sys
input = sys.stdin.readline

# 부분집합 DFS 를 써야 함 (순서가 없어도 됨)


def dfs(idx, sum1, picked):
    global count

    if idx == n:
        if sum1 == s and picked:    # 한번이라도 숫자를 뽑은 경우에만 개수를 더함
            count += 1
        return
    

    dfs(idx+1, sum1 + d[idx], True)       # 현재 번호를 선택하는 경우
    dfs(idx+1, sum1, picked)                # 현재 번호를 선택하지 않는 경우
        
    

n, s = map(int, input().split())
d = list(map(int, input().split()))

visited = [False] * n
count = 0
dfs(0, 0, False)

print(count)