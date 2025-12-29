# https://www.acmicpc.net/problem/2239
import sys
input = sys.stdin.readline

# 종료조건 - 81 칸을 다 채웠는지.

def possibleRow(y,new_number):
    for i in range(9):
        if board[i][y] == new_number:
            return False
    return True

def possibleCol(x, new_number):
    return not new_number in board[x]



base = {
    0: 0,
    1:0,
    2:0,
    3:3,
    4:3,
    5:3,
    6:6,
    7:6,
    8:6,
}

# 012 345 678
def possible3x3(x,y,new_number):
    global board

    base_x = base[x]
    base_y = base[y]

    for i in range(base_x, base_x + 3):
        for j in range(base_y, base_y + 3):
            if board[i][j] == new_number:
                return False
    return True


board = [list(map(int, input().rstrip())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

# 0,0,1
def back_tracking(idx):

    if idx == len(blank):
        for row in board:
            print("".join(map(str, row)))   
        exit(0)
    
    x, y = blank[idx]

    # 들어갈 수 있다면
    for number in range(1, 10):
        if possibleRow(y, number) and possibleCol(x, number) and possible3x3(x, y, number):
            board[x][y] = number
            
            back_tracking(idx+1)
            
            # 없다면 원복
            board[x][y] = 0

back_tracking(0)



