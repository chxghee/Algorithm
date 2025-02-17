import sys
# https://school.programmers.co.kr/learn/courses/30/lessons/60059


def solution(key, lock):
    
    klen = len(key)
    llen = len(lock)

    newlock = [[0] * (llen*3) for _ in range(llen*3)]
    for i in range(llen):
        for j in range(llen):
            newlock[llen + i][llen + j] = lock[i][j]

    for r in range(4):
        key = rotation(key)
        for x in range(llen * 2):
            for y in range(llen * 2):

                for i in range(klen):   # 열쇠 넣기
                    for j in range(klen):
                        newlock[x+i][y+j] += key[i][j]
                
                if checklock(newlock) == True:
                    return True
                
                for i in range(klen):   # 열쇠 빼기
                    for j in range(klen):
                        newlock[x+i][y+j] -= key[i][j]
                
    return False

def checklock(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True
            

def rotation(key):
    
    klen = len(key)
    result = [[] for _ in range(klen)]
    
    for i in range(klen):
        for j in range(klen):
            result[i].append(key[klen - j - 1][i])
    
    return result


# n,m  = map(int, sys.stdin.readline().split())
# lock = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# key = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# 1. 4방향 회전 후 이동으로 풀기
