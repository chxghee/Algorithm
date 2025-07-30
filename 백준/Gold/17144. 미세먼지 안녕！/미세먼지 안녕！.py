# https://www.acmicpc.net/problem/17144
import copy
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

air = ((1,2))
def can_diffuse(x,y):
    return 0 <= x < r and 0 <= y < c and not (y == 0 and x in air)

def diffuse(position, new_room):
    x, y = position
    dirty = room[x][y] // 5
    diffused_cnt = 0

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        if can_diffuse(cx, cy):
            new_room[cx][cy] += dirty
            diffused_cnt += 1

    new_room[x][y] -= dirty * diffused_cnt

def working_clockwise():
    x, y = air[1], 0

    # 1. 
    for i in range(x+1, r-1):
        new_room[i][0] = new_room[i+1][0]
    
    # 2
    for i in range(c-1):
        new_room[r-1][i] = new_room[r-1][i+1]
    
    # 3
    for i in range(r-1, x, -1):
        new_room[i][c-1] = new_room[i-1][c-1]

    # 4
    for i in range(c-1, 1, -1):
        new_room[x][i] = new_room[x][i-1]
    new_room[x][1] = 0




def working_declockwise():
    x, y = air[0], 0

    for i in range(x-1, 0, -1):
        new_room[i][0] = new_room[i-1][0]
    
    # 2
    for i in range(c-1):
        new_room[0][i] = new_room[0][i+1]
    
    # 3 -> 
    for i in range(0, x):
        new_room[i][c-1] = new_room[i+1][c-1]

    # 4
    for i in range(c-1, 1, -1):
        new_room[x][i] = new_room[x][i-1]
    new_room[x][1] = 0


def working():
    working_declockwise()
    working_clockwise()



def get_total_dirty():
    result = 0
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                result += room[i][j]
    return result


r,c,t = map(int,input().split())

room = [list(map(int, input().split())) for _ in range(r)]

a = 0
for i in range(r):
    if room[i][0] == -1:
        a = i
        break

air = (a, a+1)

for i in range(t):
    new_room = copy.deepcopy(room)
    
    # 먼지 확산
    dirty_list = []
    for i in range(r):
        for j in range(c):
            if room[i][j] >= 5:
                dirty_list.append((i, j))

    for position in dirty_list:
        diffuse(position, new_room)
    
    # 공기 청정기 가동
    working()
    room = new_room
    

print(get_total_dirty())


