# 상하좌우
n = int(input())
move = input().split()

result = [1,1]

for m in move:
    if m == 'L' and result[1] > 1:
        result[1] -= 1
    elif m == 'R' and result[1] < n:
        result[1] += 1
    elif m == 'U' and result[0] > 1:
        result[0] -= 1
        print("###")
    elif m== 'D' and result[0] < n:
        result[0] += 1
    else:
        continue

print(result[0], result[1])



## 책 방법
x ,y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_type = ["L", "R", "U", "D"]

for m in move:
    for i in range(len(move_type)):
        if move_type[i] == m:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx > n or nx < 1 or ny > n or ny < 1:
        continue

    x, y = nx, ny

print(x,y)