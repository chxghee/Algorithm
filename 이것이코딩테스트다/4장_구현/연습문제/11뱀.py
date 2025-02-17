import sys
# https://www.acmicpc.net/problem/3190


def change_direction(direction, d):
    if d == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 보드 크기 n
n = int(sys.stdin.readline().rstrip())
# 맵 정보 (뱀 2 사과 1 아무것도 없으면 0)
data = [[0]*(n + 1) for _ in range(n+1)] 

# 사과 개수 k
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    a,b = map(int, sys.stdin.readline().split())
    data[a][b] = 1

# 방향 변환 l
l = int(sys.stdin.readline().rstrip())
s = [sys.stdin.readline().split() for _ in range(l)]
di = [(int(x[0]), x[1]) for x in s]

# 동 남 서 북 기준
dy = [1,0,-1,0]
dx = [0,1,0,-1]

x, y = 1, 1
data[x][y] = 2
time = 0
idx = 0
next_change, d = di[idx][0], di[idx][1]

# 동 0 남 1 서 2 북 3
direction = 0

q = [(x, y)]

while True:
    # 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not (1 <= nx <= n and 1<= ny <= n) or data[nx][ny] == 2:
        time += 1
        break

    if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        popx, popy = q.pop(0)
        data[popx][popy] = 0    # 꼬리 공간 풀기
    else:   # 사과 존재
        data[nx][ny] = 2
        q.append((nx, ny))

    x, y = nx, ny    
    # 시간 증가
    time += 1
    # 방향 바꾸기
    if idx < len(di) and time == int(di[idx][0]):
        direction = change_direction(direction, di[idx][1])
        idx += 1

print(time)