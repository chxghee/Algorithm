# https://www.acmicpc.net/problem/14500
import sys
input = sys.stdin.readline

def in_range(x,y):
    return 0<= x <n and 0<=y<m
    
    

def tet1(x,y):
    r1 = 0
    r2 = 0

    if y + 4 <= m:  # 가로
        r1 = sum(data[x][y:y+4])
    if x + 4 <= n:  # 세로
        r2 = sum(data[i][y] for i in range(x, x+4))
    
    return max(r1, r2)

def tet2(x,y):

    if x + 1 < n and y + 1 < m:
        return data[x][y] + data[x][y+1] + data[x+1][y] + data[x+1][y+1]
    
    return 0

def tet3(x,y):
    t3 = [[(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (0,2), (-1,2)], [(0,0), (-1,0), (-2,0), (-2,-1)], [(0,0), (0,-1), (0,-2), (1,-2)],
          [(0,0), (1,0), (2,0), (2,-1)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (-1,0), (-2,0), (-2,1)], [(0,0), (0,-1), (0,-2), (-1,-2)]]
    
    return find_sum(x,y,t3)

def tet4(x,y):
    t4 = [[(0,0),(1,0),(1,1),(2,1)],       # S자 아래로 기울기
            [(0,0),(0,1),(-1,1),(-1,2)],     # S자 오른쪽 기울기
            [(0,0),(-1,0),(-1,-1),(-2,-1)],  # Z자 위로 기울기
            [(0,0),(0,-1),(1,-1),(1,-2)]    # Z자 왼쪽 기울기
        ]
    
    return find_sum(x,y,t4)



def tet5(x,y):
    t5 = [
        [(0,0), (0,1), (0,2), (1,1)],     # ㅗ
        [(0,0), (1,0), (2,0), (1,1)],     # ㅏ
        [(0,0), (0,1), (0,2), (-1,1)],    # ㅜ
        [(0,0), (1,0), (2,0), (1,-1)]     # ㅓ
    ]  
    
    return find_sum(x,y,t5)


def find_sum(x,y,t):
    result = 0
    for val in t:
        s = 0
        for i in range(4):
            dx, dy = val[i]
            cx = x + dx
            cy = y + dy
            if in_range(cx,cy):
                s += data[cx][cy]
            else:
                s=0
                break
        result = max(result, s)
    
    return result



n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]


result = 0
for i in range(n):
    for j in range(m):
        res = max(tet1(i,j), tet2(i,j), tet3(i,j), tet4(i,j), tet5(i,j))
        result = max(result, res)

print(result)