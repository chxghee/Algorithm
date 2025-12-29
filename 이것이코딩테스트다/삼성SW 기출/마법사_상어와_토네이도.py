import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
result = 0


# (dx, dy, ratio) : 현재 위치 (x,y) 기준 상대좌표와 비율(%)
ratios = [
    # 0: 왼쪽
    [(-1, 1, 1), (1, 1, 1), (-2, 0, 2), (2, 0, 2), (-1, 0, 7), (1, 0, 7), (-1, -1, 10), (1, -1, 10), (0, -2, 5)],
    # 1: 아래쪽
    [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, 2, 2), (0, -1, 7), (0, 1, 7), (1, -1, 10), (1, 1, 10), (2, 0, 5)],
    # 2: 오른쪽
    [(-1, -1, 1), (1, -1, 1), (-2, 0, 2), (2, 0, 2), (-1, 0, 7), (1, 0, 7), (-1, 1, 10), (1, 1, 10), (0, 2, 5)],
    # 3: 위쪽
    [(1, -1, 1), (1, 1, 1), (0, -2, 2), (0, 2, 2), (0, -1, 7), (0, 1, 7), (-1, -1, 10), (-1, 1, 10), (-2, 0, 5)]
]

alpha_pos = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def spread_sand(x, y, direction):
    
    global result
    
    sand = a[x][y]
    a[x][y] = 0
    total_spread = 0

    # 비율이 정해진 모래 이동
    for dx, dy, r in ratios[direction]:
        nx, ny = x + dx, y + dy
        spread_amount = (sand * r) // 100
        total_spread += spread_amount

        if 0 <= nx < n and 0 <= ny < n:
            a[nx][ny] += spread_amount
        else:
            result += spread_amount
    
    # 알파(α) 위치로 남은 모래 이동
    remaining_sand = sand - total_spread
    ax, ay = alpha_pos[direction]
    nx, ny = x + ax, y + ay

    if 0 <= nx < n and 0 <= ny < n:
        a[nx][ny] += remaining_sand
    else:
        result += remaining_sand


x = y = n // 2

# 왼(0), 아래(1), 오른(2), 위(3)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 0
move_count = 0
move_len = 1
change_dir = 0

# (0,0)에 도달할 때까지 루프 실행
while not (x == 0 and y == 0):
    
    x += dx[direction]
    y += dy[direction]
    move_count += 1
    
    spread_sand(x, y, direction)

    # 이동 거리를 다 채우면 방향 전환
    if move_count == move_len:
        move_count = 0
        direction = (direction + 1) % 4
        change_dir += 1

        # 방향을 2번 바꿀 때마다 이동 거리 1 증가
        if change_dir == 2:
            change_dir = 0
            move_len += 1

print(result)