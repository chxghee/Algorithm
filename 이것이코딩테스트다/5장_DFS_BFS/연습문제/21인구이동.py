import sys

n, l, r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dx = [-1, 0,1,0]
dy = [0,-1,0,1]

# 연합 가능 여부 체크
def check_union(a,b):
    if l <= abs(a-b) <= r:
        return True
    return False

# 인구이동
def move(un, total_pop):
    avg_population = total_pop // len(un)
    for x, y in un:
        data[x][y] = avg_population
    

def dfs(x,y, visited):
    stack = [(x, y)]
    union = [(x, y)]
    total_pop = data[x][y]
    visited[x][y] = True


    while stack:
        nx, ny = stack.pop()
        now_country = data[nx][ny]
        

        for i in range(4):
            cx, cy = nx + dx[i] , ny + dy[i]

            if 0 <= cx < n and 0 <= cy < n: 
                next_country = data[cx][cy]
                if check_union(now_country, next_country):  # 이동가능하다면
                    
                    if not visited[cx][cy]:             # 아직 방문하지 않았다면
                        visited[cx][cy] = True
                        stack.append((cx, cy))
                        union.append((cx, cy))
                        total_pop += next_country

    return union, total_pop


days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False

    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                union, total_pop = dfs(x, y, visited)

                if len(union) != 1:       
                    move(union, total_pop)
                    is_moved = True

    if not is_moved:
        break
    
    days += 1

print(days)