# https://www.acmicpc.net/problem/12100
import sys
import copy
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


def find_max_num(board):
    return max(map(max, board))

# 1. 전치 행렬 만듬 -> zip(*board)
# 2. 각 행을 뒤집어 줘야 최종적으로 시계방향으로 회전한 결과 얻음
def rotate(board):
    return [list(reversed(col)) for col in zip(*board)]


def move(data, dirc):

    # dirc: 0 = 오른쪽, 1 = 아래, 2 = 왼쪽, 3 = 위
    d = copy.deepcopy(data)

    # 방향에 따라 시계 방향 회전 -> 오른쪽으로 이동한 로직만 구현해 결과 얻기
    for _ in range(dirc):
        d = rotate(d)

    for i in range(n):
        pivot = d[i][n-1]
        p_idx = n-1
        for j in range(n-2, -1, -1):        

            if pivot != 0:      # 기준점 0 아니고
                if d[i][j] != 0:    # 비교값이 0 아니면
                    if pivot == d[i][j]: # 같은 값이라면 합치기
                        d[i][j] = 0
                        pivot *= 2
                    
                        d[i][p_idx] = pivot     # 값 반영 및 피봇 이동
                        p_idx -= 1
                        pivot = 0

                    else:                # 다른 값이면 pivot 한 칸 이동 
                        d[i][p_idx] = pivot
                        p_idx -= 1
                        pivot = d[i][j]
                        d[i][j] = 0
                        
            else:       # 현재 pivot 이 0 이면 값을 당겨와야 한다는 것
                if d[i][j] != 0:
                    pivot = d[i][j]
                    d[i][j] = 0
            
        d[i][p_idx] = pivot         # 최종 pivot 값 반영

    return d

# 브루트포스
def dfs(data, depth):
    
    if depth == 5:
        return find_max_num(data)

    return max(dfs(move(data, dir), depth+1) for dir in range(4))


print(dfs(data, 0))
        

"""
5
0 0 128 0 8
64 0 0 2 2
2 8 0 0 64
2 32 4 8 8
0 0 0 16 0

256

4
32 64 0 0
4 128 256 0
128 4 16 2
4 128 32 32

256


4
2 2 4 16
0 0 0 0
0 2 0 2
0 0 0 0


3
2 2 2
0 0 0
0 0 0

"""