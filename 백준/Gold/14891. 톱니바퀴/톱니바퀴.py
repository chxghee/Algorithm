import sys
from collections import deque
input = sys.stdin.readline

def turn_cog(turn_cog_num, dirt):
    turn_cog_num -= 1  # 입력이 1-based이므로 0-based로 변환

    turn = [0] * 4  # 각 톱니바퀴의 회전 방향 저장 (0: 회전 안 함, 1: 시계, -1: 반시계)
    turn[turn_cog_num] = dirt  # 현재 톱니바퀴 회전 방향 설정

    # 오른쪽으로 전파
    d = dirt  # 현재 회전 방향
    for i in range(turn_cog_num, 3):  # 현재 톱니부터 오른쪽 끝까지 검사
        right = i + 1  # 오른쪽 톱니
        if cog[i][2] != cog[right][6]:  # 맞닿은 부분(2,6) 비교
            d *= -1  # 반대 방향으로 회전
            turn[right] = d
        else:
            break  # 같으면 전파 멈춤

    # 왼쪽으로 전파
    d = dirt
    for i in range(turn_cog_num, 0, -1):  # 현재 톱니부터 왼쪽 끝까지 검사
        left = i - 1  # 왼쪽 톱니
        if cog[i][6] != cog[left][2]:  # 맞닿은 부분(6,2) 비교
            d *= -1  # 반대 방향으로 회전
            turn[left] = d
        else:
            break  # 같으면 전파 멈춤

    # 실제 회전 수행
    for i in range(4):
        if turn[i] == 1:    # 시계 방향 회전
            cog[i].appendleft(cog[i].pop())
        elif turn[i] == -1:  # 반시계 방향 회전
            cog[i].append(cog[i].popleft())

# 입력 받기
cog = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())

for _ in range(k):
    cog_num, dirt = map(int, input().split())
    turn_cog(cog_num, dirt)

# 결과 계산
result = 0
point = [1, 2, 4, 8]

for i in range(4):
    if cog[i][0] == 1:
        result += point[i]

print(result)
