import sys
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# 시작좌표, 기둥, 설치
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5

# 기듕 -> 1.바닥: data[x][y-1] == -1    2.기둥존재: data[x][y-1] == 0   3.왼쪽에 보 존재 data[x-1][y-1] == 1 

# 보 -> 1.기둥존재: data[x][y-1] == 0   2. 양옆에 보 존재: data[x-1][y] == 1 and data[x+1][y] == 0


# 기듕 -> 2.위에 기둥존재: data[x][y+1] == 0   3.왼쪽에 보 존재 data[x-1][y-1] == 1 

def solution(n, build_frame):
    answer = [[]]
    data = [[3] * n for _ in range(n)] # 인덱스 기준으로 1이면 보 0이면 기둥 아무것도 아ㄴ면 3

    for val in range(build_frame):

        x = val[0]
        y = val[1]
        obj = val[2]
        op = val[3]

        # 기둥이라면
        if obj == 0:
            if op == 1: # 설치
                if vertical(data, x, y) == True:
                    data[x][y] = 0
                    answer.append(list[x,y,0])

            else: # 철거
                if vertical_remove(data, x, y) == True:
                    data[x][y] = 3
                    data = [item for item in data if item != list[x,y,0]]

        # 보
        else:
            if op == 1: # 설치
                if vertical(data, x, y) == True:
                    data[x][y] = 0
                    answer.append(list[x,y,0])

            else: # 철거
                if vertical_remove(data, x, y) == True:
                    data[x][y] = 3
                    data = [item for item in data if item != list[x,y,0]]





    


    return answer


def vertical(data, x, y):
    
    if data[x][y] != 3:
        return False
    
    if data[x][y-1] == 0 or data[x-1][y-1] == 1 or y == 0:
        return True
    
    return False

def horizental(data, x, y):

    if data[x][y] != 3:
        return False
    
    if data[x][y-1] == 0 or data[x+1][y-1] == 0:
        return True
    
    if data[x-1][y] == 1 and data[x+1][y] == 1:
        return True
    
    return False


def vertical_remove(data, x, y):
    
    if data[x][y] != 0:
        return False

    # 기둥 오른편 보 존재 -> 아래 기둥이 있을때 + 다음보가 기둥에 지탱
    if (v_check1(data, x, y) == True) and (v_check2(data, x, y) == True):
        return True
    
    return False

def v_check1(data, x, y):

    if data[x][y+1] == 1:  
        if data[x+1][y] == 0:
            return True
        if data[x+1][y+1] == 1 and data[x+2][y] == 0:
            return True
    return False

def v_check2(data, x, y):
    if data[x-1][y+1] == 1: # 왼쪽에 보 존재
        if data[x-1][y] == 0:
            return True
        if data[x-1][y+1] == 1 and data[x-2][y] == 0:
            return True
    return False


def horizental_remove(data, x, y):

    if data[x][y] != 1:
        return False
    
    # 기중에 지턍되어 있고 오른쪽에 보가 존재 -> 근데 걔가 연결된 곳이 기둥

    if data[x][y-1] == 0:
        if data[x+1][y-1]:
            return True
        if data[x+1][y] == 1 and data[x+2][y-1] == 0:
            return True
    
    if data[x+1][y-1] == 0:
        if data[x][y-1] == 0:
            return True
        
            

    if data[x][y-1] == 0 or data[x+1][y-1] == 0:
        return True
    
    if data[x-1][y] == 1 and data[x+1][y] == 1:
        return True
    
    return False


solution(n,build_frame)
