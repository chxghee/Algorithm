# https://www.acmicpc.net/problem/16235
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n


# 봄: 나이만큼 양분 먹고 나이 +1 (어린 나무 순으로) 못먹으면 즉시 사망
def spring():
    global trees
    
    survivors = deque()
    dead = deque()
    
    while trees:
        age, x, y = trees.popleft()
        food = ground[x][y]

        if food - age < 0:  # 양분 못먹으면 사망.
            dead.append((age, x, y))

        else:
            survivors.append((age+1, x, y))
            ground[x][y] -= age

    trees = survivors
    return dead



# 여름: 죽은 나무 나이 // 2 가 양분으로
def summer(dead):
    while dead:
        age, x, y = dead.pop()
        ground[x][y] += age // 2


# 가을: 나이 % 5 == 0.  이면 인접한 모든 칸에ㅔ 나이가 1인 나무 생김
def autumn():
    r = len(trees)
    for i in range(r-1, -1, -1):
        age, x, y = trees[i]
        if age % 5 == 0:
            for j in range(8):
                cx = x + dx[j]
                cy = y + dy[j]
                if is_valid(cx, cy):
                    trees.appendleft((1, cx, cy))
        if age < 5:
            break


# 겨울: 로봇이 양분 주입
def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += a[i][j]

def season():
    dead_trees = spring()
    summer(dead_trees)
    autumn()
    winter()


n,m,k = map(int, input().split())
ground = [[5] * n for _ in range(n)] 

a = [list(map(int, input().split())) for _ in range(n)]

trees_init = []
for i in range(m):
    x,y,z = map(int, input().split())
    trees_init.append((z, x-1, y -1))
trees_init.sort()
trees = deque(trees_init)


# k 년 지날때
for i in range(k):
    season()

print(len(trees))
