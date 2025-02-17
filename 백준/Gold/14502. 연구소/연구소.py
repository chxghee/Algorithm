# https://www.acmicpc.net/problem/14502
import sys
import copy
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# 빈 칸과 바이러스 위치 저장
coor = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 0]
virus_positions = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 2]

# 안전 영역 계산 함수
def check_safty(lab):
    return sum(row.count(0) for row in lab)

# 바이러스 전파 함수 (DFS 방식)
def spread_virus(lab, x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                stack.append((nx, ny))

# 벽 설치 후 안전 영역 계산
def find_safe(lab):
    temp_lab = copy.deepcopy(lab)
    for x, y in virus_positions:
        spread_virus(temp_lab, x, y)
    return check_safty(temp_lab)

# 벽 설치 모든 경우의 수
new_walls = combinations(coor, 3)

# 최대 안전 영역 찾기
safe = 0
for walls in new_walls:
    # 새로운 벽 설치
    for x, y in walls:
        data[x][y] = 1
    # 안전 영역 계산
    safe = max(safe, find_safe(data))
    # 설치한 벽 초기화
    for x, y in walls:
        data[x][y] = 0

print(safe)