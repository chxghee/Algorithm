# https://www.acmicpc.net/problem/15684
import copy
import sys
input = sys.stdin.readline



def move_ladder(ladder, position):
    
    for i in range(1, h+1):    
        if position in ladder[i]:
            position += 1
        elif position - 1 in ladder[i]:
            position -= 1

    return position


def is_answer_ladder(ladder):

    for position in range(1, n + 1):
        r = move_ladder(ladder, position)
        if position != r:
            return False

    return True


def dfs(idx, depth):
    global result

    if depth >= result or depth > 3:
        return
    
    if is_answer_ladder(ladder):
        result = min(result, depth)
        
    
    for new_ladder_idx in range(idx, len(candidates)):
        new_line_row, new_line_col = candidates[new_ladder_idx]

        if new_line_col in ladder[new_line_row] or new_line_col - 1 in ladder[new_line_row] or new_line_col + 1 in ladder[new_line_row]:
            continue

        ladder[new_line_row].add(new_line_col)       # 사다리 추가
        dfs(new_ladder_idx + 1, depth+1)                   # 다음 사다리를 고르도록 인덱스 +1
        ladder[new_line_row].remove(new_line_col)       # 사다리 원복
    


 
# 입력
n,m,h = map(int, input().split())
ladder = [set() for _ in range(h + 1)]


for i in range(m):
    a, b = map(int, input().split())
    ladder[a].add(b)

# 사다리 후보들
candidates = []
for i in range(1, h + 1):
    for j in range(1, n):
        if j not in ladder[i] and j-1 not in ladder[i] and j+1 not in ladder[i]:
            candidates.append((i, j))



result = 4
dfs(0, 0)
print(result if result < 4 else -1)


