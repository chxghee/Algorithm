# https://www.acmicpc.net/problem/14891

# 같으면 회전 x 다르면  반대 방향 회전  / N = 0, S = 1 / 1 시계, -1 반시계(앞에꺼 빼서 뒤에)

import sys
from collections import deque
input = sys.stdin.readline

# 2 - 6 


def turn_cog(turn_cog_num, dirt):
    turn_cog_num -= 1

    turn = [0] * 4
    turn[turn_cog_num] = dirt
   
   
    d = dirt
    for i in range(turn_cog_num, 3):
        right = 1 + i
        
        if cog[right][6] != cog[i][2]:
            d *= -1
            turn[right] = d
        else:
            break
        
               
    d = dirt 
    for i in range(turn_cog_num, 0, -1):
        left = i - 1
        
        if cog[left][2] != cog[i][6]:
            d *= -1
            turn[left] = d
        else:
            break
         

    for i in range(4):
        if turn[i] == -1:
            data = cog[i].popleft()
            cog[i].append(data)
        
        if turn[i] == 1:
            data = cog[i].pop()
            cog[i].appendleft(data)




cog = [deque(list(map(int, input().rstrip()))) for _ in range(4)]



k = int(input())

for _ in range(k):
    cog_num, dirt = map(int, input().split())
    turn_cog(cog_num, dirt)


result = 0
point = {
    0: 1,
    1: 2,
    2: 4,
    3: 8 
}


for i in range(4):
    if cog[i][0] == 1:
        result += point[i]

print(result)



