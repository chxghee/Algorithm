# https://www.acmicpc.net/problem/7569
from collections import deque
import sys
input = sys.stdin.readline

# 다 익을 떄 까지 며칠? -> level을 알아야 함 BFS?
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

def validate_position(k,x,y):
    return 0 <= k < h and 0 <= x < n and 0 <= y < m

def bfs():
    
    # 모든 익은 토마토는 BFS를 같이 시작 해야 함
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if box[k][i][j] == 1:
                    q.append((k,i,j))

    while q:
        k, x, y  = q.popleft()

        # 인접 토마토 
        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            ck = k + dk[i]

            # 안익은 토마토일 경우
            
            if validate_position(ck,cx,cy) and box[ck][cx][cy] == 0:
                box[ck][cx][cy] = box[k][x][y] + 1
                q.append((ck,cx,cy))

    # 걸린 시간 계산
    result = 0
    for k in range(h):
        for i in range(n):

            # 익지 않은 토마토 있으면 -1 리턴
            if 0 in box[k][i]:
                return 0

            row_max = max(box[k][i])
            result = max(row_max, result)

    return result



# input
m, n, h = map(int, input().split())

box = []
for k in range(h):
    tomato = [list(map(int, input().split())) for i in range(n)]
    box.append(tomato)


print(bfs()-1)

