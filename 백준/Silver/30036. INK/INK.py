# https://www.acmicpc.net/problem/30036
import sys
input = sys.stdin.readline



class Square:
    coor: tuple
    color: str
    color_idx: int
    ink_amount: int

    def __init__(self, coor=(), color=None, color_idx=0, ink_amount=0):
        self.coor = coor
        self.color = color
        self.color_idx = 0
        self.ink_amount = ink_amount
    
    def next_color(self, color_set):
        self.color_idx = (self.color_idx + 1) % len(color_set)
        self.color = color_set[self.color_idx]







# U D L R 상하좌우
# 잉크 충저ㄴ: j
# 점프: J
def charge_ink(square):
    square.ink_amount += 1


def jump(square):
    paintable_wall = has_paintable_wall(square)

    for p in paintable_wall:
        x, y = p
        data[x][y] = square.color

    square.next_color(color_set)
    square.ink_amount = 0



def has_paintable_wall(square):
    x, y = square.coor

    paintable_wall = []
    for w in wall:
        wx, wy = w
        if abs(x-wx) + abs(y-wy) <= square.ink_amount:
            paintable_wall.append((wx, wy))
    
    return paintable_wall


def move(square, dirc):
    x,y = square.coor
    

    if dirc == 'U':
        x -= 1
        if not can_move(x,y):
            return  
        data[x+1][y] = '.'
    
    elif dirc == 'D':
        x += 1
        if not can_move(x,y):
            return 
        data[x-1][y] = '.'
    
    elif dirc == 'L':
        y -= 1
        if not can_move(x,y):
            return 
        data[x][y+1] = '.'
    
    else:
        y += 1
        if not can_move(x,y):
            return
        data[x][y-1] = '.'
    
    data[x][y] = '@'
    square.coor = (x, y)

def can_move(x,y):
    return 0 <= x < n and 0 <= y < n and (x, y) not in wall


wall = set()

i,n,k = map(int, input().split())
color_set = list(input().rstrip())

data = [list(input().rstrip()) for _ in range(n)]
command = list(input().rstrip())

for i in range(n):
    for j in range(n):
        if data[i][j] == '#':
            wall.add((i,j))
        if data[i][j] == '@':
            square = Square((i, j), color_set[0], 0)


for cmd in command:

    if cmd == 'j':
        charge_ink(square)
    elif cmd == 'J':
        jump(square)
    else:
        move(square, cmd)


for i in range(n):
    for j in range(n):
        print(data[i][j],end='')
    print()
