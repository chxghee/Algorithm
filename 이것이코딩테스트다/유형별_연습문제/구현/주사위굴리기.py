# https://www.acmicpc.net/problem/14499
from collections import deque
import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
trial = list(map(int, input().split()))

# 이동 방향 (동, 서, 북, 남)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 주사위 상태 (전개도)
dice = [0] * 6  # 인덱스: [윗면, 북, 동, 서, 남, 바닥]

for val in trial:
    nx, ny = x + dx[val], y + dy[val]

    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 주사위 회전 처리
    if val == 1:  # 동쪽
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif val == 2:  # 서쪽
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif val == 3:  # 북쪽
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif val == 4:  # 남쪽
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    # 바닥 값 갱신
    if data[nx][ny] == 0:
        data[nx][ny] = dice[5]
    else:
        dice[5] = data[nx][ny]
        data[nx][ny] = 0

    x, y = nx, ny

    print(dice[0])
