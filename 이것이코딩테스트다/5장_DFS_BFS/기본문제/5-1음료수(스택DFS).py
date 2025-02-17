import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def dfs_stack(x, y):
    stack = [(x, y)]  # 시작 지점을 스택에 넣습니다.
    is_new_area = False

    while stack:
        cx, cy = stack.pop()

        # 범위를 벗어나거나 이미 방문한 경우
        if cx < 0 or cx >= n or cy < 0 or cy >= m or graph[cx][cy] != 0:
            continue

        # 방문 처리
        graph[cx][cy] = 1
        is_new_area = True

        # 상하좌우 인접한 노드를 스택에 추가
        stack.append((cx, cy + 1))  # 오른쪽
        stack.append((cx, cy - 1))  # 왼쪽
        stack.append((cx + 1, cy))  # 아래쪽
        stack.append((cx - 1, cy))  # 위쪽

    return is_new_area


result = 0
for i in range(n):
    for j in range(m):
        if dfs_stack(i, j):
            result += 1

print(result)