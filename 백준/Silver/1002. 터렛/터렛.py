import sys
import math
input = sys.stdin.readline

def count_positions(x1, y1, r1, x2, y2, r2):
    dist = math.hypot(x2 - x1, y2 - y1)

    # 같은 중심
    if dist == 0:
        if r1 == r2:
            return -1  #같은 원일 떄
        else:
            return 0

    # 서로 다른 중심
    if dist == r1 + r2 or dist == abs(r1 - r2):
        return 1
    elif abs(r1 - r2) < dist < r1 + r2:
        return 2
    else:
        return 0

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(count_positions(x1, y1, r1, x2, y2, r2))
