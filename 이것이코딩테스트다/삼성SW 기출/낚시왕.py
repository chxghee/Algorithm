# https://www.acmicpc.net/problem/17143
import copy
import sys
input = sys.stdin.readline

INF = int(1e9)
# 위 아래 오 왼
dx = [0, -1,1,0,0]
dy = [0, 0,0,1,-1]


def catch(position, sharks):
    global result

    find = -1
    distance = INF
    size = INF
    for i in range(len(sharks)):
        r, c, s, d, z = sharks[i]
        if position == c:
            if distance > r:
                distance = r
                find = i
                size = z
    if distance != INF:
        sharks.pop(find)
        result += size
    

def move_sharks():
    after = {}
    for shark in sharks:
        r, c, s, d, z = shark
        
        nr, nc, nd = move(r,c,s,d)


        key = (nr, nc)
        if key not in after or after[key][4] < z:
            after[key] = (nr, nc, s, nd, z)

    
    return list(after.values())



def append_shark(new_shark, after):
    flag = 0

    for i in range(len(after)):
        shark = after[i]
        if new_shark[0] == shark[0] and new_shark[1] == shark[1]:# 같은 위치에 상어 
            flag = 1
            if new_shark[4] > shark[4]:   #.새로운 상어가 클떄
                after[i] = new_shark
            else:
                break

    # 아무것도 추가되지 않았을 떄
    if flag == 0:    
        after.append(new_shark)

    return after
def move(r, c, s, d):
    if d == 1 or d == 2:  # 상하 이동
        cycle = (R - 1) * 2
        s %= cycle
        
        if d == 1:  # 위로
            if s <= r:
                return r - s, c, d
            else:
                remaining = s - r
                cycles = remaining // (R - 1)
                pos = remaining % (R - 1)
                if cycles % 2 == 0:
                    return pos, c, 2  # 아래 방향
                else:
                    return R - 1 - pos, c, 1  # 위 방향
        else:  # d == 2, 아래로
            if s <= R - 1 - r:
                return r + s, c, d
            else:
                remaining = s - (R - 1 - r)
                cycles = remaining // (R - 1)
                pos = remaining % (R - 1)
                if cycles % 2 == 0:
                    return R - 1 - pos, c, 1  # 위 방향
                else:
                    return pos, c, 2  # 아래 방향
                    
    else:  # d == 3 or d == 4, 좌우 이동
        cycle = (C - 1) * 2
        s %= cycle
        
        if d == 3:  # 오른쪽으로
            if s <= C - 1 - c:
                return r, c + s, d
            else:
                remaining = s - (C - 1 - c)
                cycles = remaining // (C - 1)
                pos = remaining % (C - 1)
                if cycles % 2 == 0:
                    return r, C - 1 - pos, 4  # 왼쪽 방향
                else:
                    return r, pos, 3  # 오른쪽 방향
        else:  # d == 4, 왼쪽으로
            if s <= c:
                return r, c - s, d
            else:
                remaining = s - c
                cycles = remaining // (C - 1)
                pos = remaining % (C - 1)
                if cycles % 2 == 0:
                    return r, pos, 3  # 오른쪽 방향
                else:
                    return r, C - 1 - pos, 4  # 왼쪽 방향


# 입력
R,C,M = map(int, input().split())

sharks = []
for i in range(M):
    r, c, s,d,z = map(int, input().split())
    r -= 1
    c -= 1
    sharks.append((r, c, s, d, z))



result = 0
for position in range(C):
    catch(position, sharks)
    sharks = move_sharks()
    

print(result)