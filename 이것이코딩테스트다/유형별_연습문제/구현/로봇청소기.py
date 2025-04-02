# https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline



n, m = map(int, input().split())
robot = list(map(int, input().split()))
data = [ list(map(int, input().split())) for i in range(n)]

# 0 북 / 1 동 / 2 남 / 3 서 
# 동 북 서 남 순서로 변함 (반 시계)
dy = [-1,0,1,0]
dx = [0,1,0,-1]
result = 0

def check_clean(y,x):
    
    for i in range(4):
        cx = dx[i] + x
        cy = dy[i] + y
        if data[cy][cx] == 0:
            return True
    return False

def turn(d):
    return (d - 1 + 4) % 4

def back(d):
    return (d + 2) % 4

while True:

    y, x, d = robot

    # 1.현재칸 청소 x
    if data[y][x] == 0:
        result += 1
        data[y][x] = 2
        continue

    # 2. 현재칸 주변의 4방향이 아직 청소되지 않은게 있는 경우
    if check_clean(y,x):
        # 90회전 (반시계)
        
        for i in range(4):
            d = turn(d) # 회전
            cx = x + dx[d]
            cy = y + dy[d]
            if data[cy][cx] == 0:
                robot[0] = cy
                robot[1] = cx
                robot[2] = d
                break

    else:
        d = back(d)
        cx = x + dx[d]
        cy = y + dy[d]
        if data[cy][cx] == 1:
            break
        else:
            robot[0] = cy
            robot[1] = cx

print(result)
        