# https://www.acmicpc.net/problem/15649
# 백트래킹으로 순열 구하기 - 재귀 (이런 조합 순열을 구할 때 혹은 이전 상황으로 돌아가야 할땐 백트래킹 재귀를 쓰면 좋음)

# 순열은 순서가 교려됨 -

import sys
input = sys.stdin.readline
n,m = map(int, input().split())


def back_tracking(depth):
    
    if depth == m:
        print(*result)   # 언패킹으로(*)  리스트에 있는 숫자들을 다 풀어서 프린트로 전달
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        
        # push
        result.append(i)
        visited[i] = True

        back_tracking(depth + 1)

        # 원복
        visited[i] = False
        result.pop()



visited = [False] * (n+1)
result = []
depth = 0

back_tracking(depth)
