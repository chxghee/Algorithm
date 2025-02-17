import sys
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# 힌트 일단 연산을 하고 하고 유효성을 검사하는것도 좋다


# 시작좌표, 기둥, 설치
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5


def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: # 기둥일때
            if y == 0 or ([x-1, y, 1] in answer) or ([x, y, 1] in answer) or ([x, y-1,0] in answer):
                continue

            return False
        elif stuff == 1: 
            if ([x,y-1,0] in answer) or (([x-1, y, 1] in answer) and ([x+1, y, 1] in answer)) or ([x+1,y-1,0] in answer):
                continue
            return False
        
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        
        x, y, stuff, op = frame
        if op == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        
        if op == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    
    return sorted(answer)


re = solution(n,build_frame)
print(re)


            
