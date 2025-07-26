import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def rotate_90_clockwise(x, y, cx, cy):
    # 기준점 (cx, cy) 기준으로 시계방향 90도 회전
    return cx - (y - cy), cy + (x - cx)

n = int(input())
visited = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    # 0세대 커브 시작
    curve = [(x, y)]
    x2 = x + dx[d]
    y2 = y + dy[d]
    curve.append((x2, y2))

    # 세대 확장
    for _ in range(g):
        end_x, end_y = curve[-1]
        new_points = []
        for i in range(len(curve) - 2, -1, -1):  # 끝에서부터 회전
            px, py = curve[i]
            rx, ry = rotate_90_clockwise(px, py, end_x, end_y)
            new_points.append((rx, ry))
        curve.extend(new_points)

    # 전체 좌표 기록
    for x, y in curve:
        if 0 <= x <= 100 and 0 <= y <= 100:
            visited[y][x] = True

# 정사각형 카운트
ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
            ans += 1

print(ans)
