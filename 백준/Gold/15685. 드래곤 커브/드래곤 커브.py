# https://www.acmicpc.net/problem/15685

import sys
input = sys.stdin.readline

nx = [1, 0, -1, 0]
ny = [0,-1, 0 , 1]

def rotate(dragon, criteria_coor, start_coor):
    
    rotated = []
    
    cx, cy = criteria_coor
    new_criteria = ()

    for coor in dragon:
        dx, dy = coor

        # 기준점을 원점으로 평행이동
        dx -= cx
        dy -= cy

        # 평행이동 후 다시 원점 이동
        rotated_x = cx - dy
        rotated_y = cy + dx

        rotated.append((rotated_x, rotated_y))

        if coor[0] == start_coor[0] and coor[1] == start_coor[1]: # 다음 기준점 구하기
            new_criteria = (rotated_x, rotated_y)

    return rotated, new_criteria


def count_square(result):
    cnt = 0
    for coor in result:
        coor1 = (coor[0] + 1, coor[1])
        coor2 = (coor[0] + 1, coor[1] + 1)
        coor3 = (coor[0], coor[1] + 1)

        if coor1 in result and coor2 in result and coor3 in result: 
            cnt += 1
    return cnt

n = int(input())
result = set()

for i in range(n):
    x, y, d, g = map(int, input().split())
    
    dragon = set()
    start = (x, y)
    criteria = (x + nx[d], y + ny[d])

    dragon.add(start)
    dragon.add(criteria)
    
    
    for val in range(g):
        
        
        rotated_dragon, criteria = rotate(dragon, criteria, start)
    
        dragon.update(rotated_dragon)
    
    
    result.update(dragon)

print(count_square(result))

