# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline



def can_place(x,y):
    return not col[y] and not diag1[x+y] and not diag2[x-y+n-1]
   
        

# 종료 조건 - 각 퀸은 행에 한 개 씩만 위치 가능 = 각 행에 퀸이 놓아진 경우
# 행을 기준으로 DFS
def dfs(row):
    global answer

    if row == n:
        answer += 1
        return
    
    for i in range(n):
        if can_place(row, i):   # 놓을 수 있다면
            col[i] = True
            diag1[row + i] = True
            diag2[row-i+n-1] = True
            
            
            dfs(row+1)
            
            col[i] = False
            diag1[row + i] = False
            diag2[row-i+n-1] = False
            



n = int(input())

col = [False] * n
diag1 = [False] * 2* n
diag2 = [False] * 2* n


answer = 0
dfs(0)

print(answer)


