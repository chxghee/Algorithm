# https://www.acmicpc.net/problem/7576

# bfs에서 진행 깊이(레벨)을 계산하는 방법
# 1. data에 날짜를 더해간다                 -> 원본 데이터가 망가지지만, 빠르고 간단
# 2. 같은 레벨은 한번에 처리해서 날짜 세기      -> 원본 데이터는 유지, but 큐를 두번 순회해야함 


from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 방법 2 - 같은 레벨은 한번에 처리헤서 날짜 세기
def bfs2():
    q = deque()
    # 익은 토마토들 먼저 큐에 넣기
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                q.append((i, j))

    days = -1  # 시작은 -1 → 처음 익은 애들은 0일 차로 치지 않음

    while q:
        for _ in range(len(q)):  # 현재 큐에 있는 모든 노드(현재 날짜에 익은 토마토들)
            x, y = q.popleft()

            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]

                if 0 <= cx < n and 0 <= cy < m and data[cx][cy] == 0:
                    data[cx][cy] = 1
                    q.append((cx, cy))
        days += 1  # 하루 지남

    return days



m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

result = bfs2()

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result = -1

print(result)