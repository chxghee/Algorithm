# https://www.acmicpc.net/problem/4883

import sys
input = sys.stdin.readline


# 연결 형태 반대가 되어야 연결 가능성 체크 가능
# 왼: 아래 오아 오른쪽 -> 위 오위 
# 가운데: 왼아 아래 오아 오른쪽 -> 왼위 위 오위 왼
# 오: 왼아 아래 -> 왼위 위 왼 

diraction = [
    [(-1, 0), (-1, 1)],
    [(-1, -1), (-1, 0), (-1, 1), (0, -1)],
    [(-1, -1), (-1, 0), (0, -1)]
]


# dp 정의 - 이전 까지의 모든 경우를 고려해서 현재 내 위치에 올떄 까지의 최소 경로 비용.

def possible(x, y):
    return 0 <= x < n and 0<= y < 3


def calc_count():
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * 3 for _ in range(n)]

    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2] 

    # 첫줄은 가운데에서만 시작 가능하니 패스
    for i in range(1, n):
        for j in range(0,3):
            x, y = i, j

            reachable_nodes = []
            for dx, dy in diraction[j]:
                nx = x + dx
                ny = y + dy


                if not possible(nx ,ny) or dp[nx][ny] == -1: # 범위 밖이면 
                    continue
                
                reachable_nodes.append(dp[nx][ny])
            
            if not reachable_nodes:
                continue

            dp[x][y] = min(reachable_nodes) + graph[x][y]
    
    return dp[n-1][1]
                

t = 0
while True:

    n = int(input())
    if n == 0:
       exit(0)
    t += 1

    result = calc_count()

    print(f"{t}. {result}")

    