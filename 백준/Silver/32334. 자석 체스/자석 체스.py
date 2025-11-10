# https://www.acmicpc.net/problem/32334
import sys
input = sys.stdin.readline

# x,y 에서 a,b 네모칸 사이에 존재하는 자석수 구하기
def get_attachs(x,y, a,b):
    
    x = max(1, x)
    y = max(1, y)
    a = min(n, a)
    b = min(n, b)

    return count[a][b] - count[x-1][b] - count[a][y-1] + count[x-1][y-1]





n, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
count = [[0]*(n+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, n+ 1):
        count[i][j] = board[i-1][j-1] + count[i-1][j] + count[i][j-1] - count[i-1][j-1]


min_attach = int(1e9)


for i in range(1, n+1):
    for j in range(1, n+1):
        
        if board[i-1][j-1] == 1:    # 자석이 있으면
            continue

        # 해당 위치에서 붙는 자석 개수 구하기 
        attach_cnt = get_attachs(i - d, j - d, i + d, j + d)


        # 0이 되는 위치가 나오면 출력 후. 종료하기
        if attach_cnt == 0:
            print(i, j)
            exit(0)
            

        if attach_cnt < min_attach:
            min_attach = attach_cnt
            x = i
            y = j



print(x, y)
print(min_attach)


"""
5 1
1 0 0 0 0
0 0 1 0 1
1 0 0 0 0
0 0 1 0 0
1 0 0 0 0
"""