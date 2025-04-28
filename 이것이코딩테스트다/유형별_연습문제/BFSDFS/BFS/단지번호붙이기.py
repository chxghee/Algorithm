# https://www.acmicpc.net/problem/2667
from collections import deque
import sys
input = sys.stdin.readline



def bfs(apt, sx, sy):
    q = deque((sx,sy))
    q.append((sx,sy))       # 중요!!! deque((x,y)) 하면 제대로 동작 안함 -> x, y가 각각 들어감 그래서 실수를 안하려면 그냥 선언과 동시에 하지 말고 나중에 append를 하도록 하자
    data[sx][sy] = apt  # 시작 노드 방문처리
    cnt = 1     # 같은 집합에 속한 노드 개수
    
    while q:
        nx, ny = q.popleft()       

        # 인접 노드 탐색
        for i in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 > cx or n <= cx or 0 > cy or n <= cy:
                continue 

            if data[cx][cy] == 1:
                data[cx][cy] = apt  # 방문처리
                q.append((cx,cy))
                cnt += 1
        
    return cnt



n = int(input())
data = [list(map(int,input().rstrip())) for _ in range(n)]

# 시계방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = []
apt = 2
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            cnt = bfs(apt, i, j)
            result.append(cnt)
            apt += 1

result.sort()
print(len(result))
for val in result:
    print(val)
