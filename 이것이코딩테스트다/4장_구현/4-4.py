# 게임 개발
n,m = map(int,input().split())
x,y,d = map(int,input().split())

# 방문 
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1


# 북 동 남 서 이동방행
dx = [-1,0,1,0]
dy = [0,1,0,-1]

maps=[]
for i in range(n):
    data = list(map(int, input().split()))
    maps.append(data)

count = 1
trun = 0

while True:
    # 왼 쪽 회전
    d = (d+3)%4 
    nx = x + dx[d]
    ny = y + dy[d]

    # 육지이고, 가본적 없다면
    if maps[nx][ny] == 0 and visit[nx][ny] == 0:
        x, y = nx, ny
        count += 1
        visit[nx][ny] = 1
        trun = 0
        continue

    # 육지지만, 가본적 있다면 / 바다라면 -> 회전만
    else:
        trun += 1

    # 네번 돌았다면 -> 갈곳이 없다 
    if trun == 4:
        
        # 뒤로 한칸
        a = (d+2)%4
        nx = x + dx[a]
        ny = y + dy[a]

        # 만약 뒤에가 바다라면 -> end
        if maps[nx][ny] == 1:
            break
        x, y = nx, ny
        trun = 0

print(count)
