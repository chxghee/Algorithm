# https://www.acmicpc.net/problem/15683
import copy
import sys
input = sys.stdin.readline

# 방향: 우 하 좌 상
cctv_type = [1,2,3,4,5]

def check_right(x, y, d):
    for i in range(y, m):   # 우
        if d[x][i] == 6:
            break
        if d[x][i] in cctv_type:
            continue
        d[x][i] = -1

def check_bottom(x, y, d):
    for i in range(x, n):   # 하
        if d[i][y] == 6:
            break
        if d[i][y] in cctv_type:
            continue
        d[i][y] = -1


def check_left(x, y, d):
    for i in range(y, -1, -1):  # 좌
        if d[x][i] == 6:
            break
        if d[x][i] in cctv_type:
            continue
        d[x][i] = -1

def check_top(x, y, d):
    for i in range(x, -1, -1):  # 상
        if d[i][y] == 6:
            break
        if d[i][y] in cctv_type:
            continue
        d[i][y] = -1

# 칠하기
def check_zone(d, cctv, dirc):
    
    x, y, type = cctv

    if type == 1:
        if dirc == 1:
            check_right(x, y, d)

        elif dirc == 2:
            check_bottom(x, y, d)

        elif dirc == 3:
            check_left(x, y, d)

        else:
            check_top(x, y, d)

    elif type == 2:
        if dirc == 1 or dirc == 3:
            check_right(x, y, d)
            check_left(x, y, d)

        else:
            check_bottom(x, y, d)
            check_top(x, y, d)

    
    elif type == 3:
        if dirc == 1:
            check_top(x, y, d)
            check_right(x, y, d)
        
        elif dirc == 2:
            check_right(x, y, d)
            check_bottom(x, y, d)
        
        elif dirc == 3:
            check_bottom(x, y, d)
            check_left(x, y, d)
        
        else:
            check_left(x, y, d)
            check_top(x, y, d)
    
    elif type == 4:
        if dirc == 1:
            check_left(x, y, d)
            check_top(x, y, d)
            check_right(x, y, d)
        
        elif dirc == 2:
            check_top(x, y, d)
            check_right(x, y, d)
            check_bottom(x, y, d)
        
        elif dirc == 3:
            check_right(x, y, d)
            check_bottom(x, y, d)
            check_left(x, y, d)
        
        else:
            check_bottom(x, y, d)
            check_left(x, y, d)
            check_top(x, y, d)
    
    else:
        check_right(x, y, d)
        check_bottom(x, y, d)
        check_left(x, y, d)
        check_top(x, y, d)
        
    
def count_zone(data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                cnt += 1
    return cnt


def dfs(data, cctv_position, idx):
    global result

    if idx == len(cctv_position):  # 모든 cctv를 확인했다면
        result = min(result, count_zone(data))
        return
    
    cctv = cctv_position[idx]
    
    # CCTV 5번은 회전할 필요가 없음 (모든 방향을 감시)
    max_direction = 1 if cctv[2] == 5 else 4
    
    for direction in range(max_direction):
        d = copy.deepcopy(data)
        check_zone(d, cctv, direction + 1)  # direction은 1부터 시작
        
        dfs(d, cctv_position, idx + 1)


n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

cctv_position = []
for i in range(n):
    for j in range(m):
        if data[i][j] != 0 and data[i][j] != 6:
            cctv_position.append((i, j, data[i][j]))


result = int(1e9)

dfs(data, cctv_position, 0)

print(result)