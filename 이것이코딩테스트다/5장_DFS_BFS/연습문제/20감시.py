from itertools import combinations
import sys

n = int(sys.stdin.readline().rstrip())
teacher = []
space = []

data = [list(sys.stdin.readline().split()) for _ in range(n)]

def check_horizental_safe(x,y,w):
    # 가로
    flag1 = 0
    flag2 = 0
    for i in range(n):
        if i < y:   # 왼쪽에서
            if data[x][i] == 'S':
                flag1 = 1
            if (x,i) in w:
                flag1 = 0

        if i > y:   # 왼쪽에서
            if (x,i) in w:
                flag2 = 0
                break
            if data[x][i] == 'S':
                flag2 = 1
                break
    if flag1 == 0 and flag2 == 0:
        return True
    return False

def check_vertical_safe(x,y,w):
    # 세로
    flag1 = 0
    flag2 = 0
    for i in range(n):
        if i < x:   # 위에서
            if data[i][y] == 'S':
                flag1 = 1
            if (i,y) in w:
                flag1 = 0

        if i > x:   # 아래서
            if (i,y) in w:
                flag2 = 0
                break
            if data[i][y] == 'S':
                flag2 = 1
                break
    if flag1 == 0 and flag2 == 0:
        return True
    return False


for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            space.append((i,j))
        if data[i][j] == 'T':
            teacher.append((i,j))


walls = list(combinations(space, 3))

def check():
    for w in walls:
        flag = 0
        for t in teacher:
            x, y = t
            if check_horizental_safe(x,y,w) and check_vertical_safe(x,y,w):
                flag += 1
            else:
                break
        
        if flag == len(teacher):
            return True
    return False

if check():
    print("YES")
else:
    print("NO")
    