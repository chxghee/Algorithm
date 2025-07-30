# https://www.acmicpc.net/problem/15684

import sys
input = sys.stdin.readline

# 틀린 세로선 개수 리턴
def check():
    cnt = 0
    for j in range(n):
        now = j
        for i in range(h):  # move
            now += ladders[i][now]
        if now != j:
            cnt += 1
    return cnt


def dfs(depth):
    global best
    c = check()

    if c > (result - 1 - depth) * 2:  # 틀린 세로 선 개수 > 남은 설치 가능 사다리 개수 * 2 이면 설치 x
        return
    
    if c == 0:  # 0 이면 사다리 조작 완료
        result = min(result, depth)
        return
    
    if result == depth + 1:
        return
    
    for i in range(h):
        ladder = ladders[i]
        for j in range(n - 1):
            if ladder[j] or ladder[j + 1]:
                continue
            ladder[j] = 1
            ladder[j + 1] = -1
            dfs(depth + 1)
            ladder[j] = 0
            ladder[j + 1] = 0
    

n, m, h = map(int, input().split())
ladders = [[0] * (n + 1) for _ in range(h)] # 사다리 수평 라인 1: 오른쪽 이동 가능 -1: 왼쪽이동 가능 0: 아무것도 x
for i in range(m):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = 1
    ladders[a - 1][b] = -1

result = 4
dfs(0)
if result == 4:
    result = -1
print(result)
