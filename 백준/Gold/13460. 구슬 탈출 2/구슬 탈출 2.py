# https://www.acmicpc.net/problem/13460
import sys
from collections import deque
input = sys.stdin.readline

# 방향: 오 아 왼 위 = 0 1 2 3

def move(ball, dir):
    x = ball[0]
    y = ball[1]
    if dir == 0:
        for i in range(y, m):
            if data[x][i] == '#':
                return (x,i-1)
            if data[x][i] == 'O':
                return (-1, -1)
        
    elif dir == 1:
        for i in range(x, n):
            if data[i][y] == '#':
                return (i-1,y)
            if data[i][y] == 'O':
                return (-1, -1)
        
    elif dir == 2:
        for i in range(y, -1, -1):
            if data[x][i] == '#':
                return (x,i+1)
            if data[x][i] == 'O':
                return (-1, -1)
        
    else:
        for i in range(x, -1 ,-1):
            if data[i][y] == '#':
                return (i+1,y)
            if data[i][y] == 'O':
                return (-1, -1)
        


def bfs(red, blue):

    cnt = 0
    q = deque()
    q.append((red, blue, cnt))
    
    while q:
        r, b, c = q.popleft()
        
    
        
        if c >= 10:
            return -1

        for i in range(4):
            if i == 0:      # 오른쪽일때
                # 벽이 나올 때 까지 이동
                new_r = move(r, i)
                new_b = move(b, i)
                

                if new_r[0] == new_b[0] and new_r[1] == new_b[1]:
                    if new_r[0] == -1:
                        continue
                    if r[1] > b[1]:
                        new_b = (new_b[0], new_b[1] - 1)
                    else:
                        new_r = (new_r[0], new_r[1] - 1)
                else:
                    if new_r[0] == -1:
                        return c + 1
                    if new_b[0] == -1:
                        continue
                
                
                if new_r[0] == r[0] and new_r[1] == r[1] and new_b[0] == b[0] and new_b[1] == b[1]: # 움직이지 않은 경우
                    continue
                q.append((new_r, new_b, c + 1))
                    

            
            elif i == 1:    # 아래
                # 벽이 나올 때 까지 이동
                new_r = move(r, i)
                new_b = move(b, i)
                

                if new_r[0] == new_b[0] and new_r[1] == new_b[1]:   # 같은 위치에 있으면...
                    if new_r[0] == -1:
                        continue
                    if r[0] > b[0]:
                        new_b = (new_b[0] - 1, new_b[1])
                        
                    else:
                        new_r = (new_r[0] - 1, new_r[1])
                else:
                    if new_r[0] == -1:
                        return c + 1
                    if new_b[0] == -1:
                        continue

                        
                
                if new_r[0] == r[0] and new_r[1] == r[1] and new_b[0] == b[0] and new_b[1] == b[1]: # 움직이지 않은 경우
                    continue
                
                q.append((new_r, new_b, c + 1))
                    
            
            elif i == 2:    # 왼
                # 벽이 나올 때 까지 이동
                new_r = move(r, i)
                new_b = move(b, i)
                

                if new_r[0] == new_b[0] and new_r[1] == new_b[1]:
                    if new_r[0] == -1:
                        continue
                    if r[1] < b[1]:
                        new_b = (new_b[0], new_b[1] + 1)
                        
                    else:
                        new_r = (new_r[0], new_r[1]+1)
                else:
                    if new_r[0] == -1:
                        return c + 1
                    if new_b[0] == -1:
                        continue
                        
                if new_r[0] == r[0] and new_r[1] == r[1] and new_b[0] == b[0] and new_b[1] == b[1]: # 움직이지 않은 경우
                    continue
                
                q.append((new_r, new_b, c + 1))
                    
            
            else:           # 위
                # 벽이 나올 때 까지 이동
                new_r = move(r, i)
                new_b = move(b, i)
                

                if new_r[0] == new_b[0] and new_r[1] == new_b[1]:   # 같은 위치에 있으면...
                    if new_r[0] == -1:
                        continue
                    if r[0] < b[0]:
                        
                        new_b = (new_b[0] + 1, new_b[1])
                        
                    else:
                        
                        new_r = (new_r[0] + 1, new_r[1])
                else:
                    if new_r[0] == -1:
                        return c + 1
                    if new_b[0] == -1:
                        continue
                        
                
                if new_r[0] == r[0] and new_r[1] == r[1] and new_b[0] == b[0] and new_b[1] == b[1]: # 움직이지 않은 경우
                    continue
                
                q.append((new_r, new_b, c + 1))

    return -1



n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] == 'B':
            blue = (i,j)
        if data[i][j] == 'R':
            red = (i,j)
        if data[i][j] == 'O':
            goal = (i,j)



print(bfs(red, blue))