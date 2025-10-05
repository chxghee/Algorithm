# https://www.acmicpc.net/problem/16918

import sys
input = sys.stdin.readline

# 1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
# 2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
# 3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
# 4. 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
# 3과 4를 반복한다.

# 1 설치 -> 2 터짐 -> 2 설치 -> 1 터짐 -> 1 설치 -> 2 터짐 -> 2 설치 -> 1 터짐 -> 1 설치 -> 2 터짐 -> 2 설치 -> 1 터짐


def set_boom(kind):
    

    for i in range(r):
        for j in range(c):
            if boom[i][j] == 0:
                boom[i][j]= kind



def explosion(kind):
    
    to = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if boom[i][j] == kind:
                to[i][j] = True
                boom_adj(i,j,to)

    for i in range(r):
        for j in range(c):
            if to[i][j]:
                boom[i][j] = 0


def boom_adj(i,j, to):
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0<= nx < r and 0<= ny < c:
            to[nx][ny] = True



dx = [0,1,0,-1]
dy = [1,0,-1,0]



r, c, n = map(int, input().split())

data = [list(input().rstrip()) for _ in range(r)]


# 0: 없음 1: 첫번째 폭탄 그룹 2: 두번째 폭탄 그룹
boom = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 'O':
            boom[i][j] = 1


time = 1


while time < n:

    # 2 터짐
    if time % 4 == 0:
        explosion(2)

    elif time % 4 == 1: # 2 설치
        set_boom(2)

    elif time % 4 == 2: # 1 터짐
        explosion(1)

    else:   # 1 설치
        set_boom(1)


    
    time += 1
    


for i in range(r):
    for j in range(c):
        if boom[i][j] == 0:
            print(".",end='')
        else:
            print("O", end='')
    print()
        