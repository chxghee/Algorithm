import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

home, chicken = [], []
for x in range(n):
    for y in range(n):
        if data[x][y] == 1:
            home.append([x,y])
        if data[x][y] == 2:
            chicken.append([x,y])


# 거리계산 함수
def cal_distance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])

# 치킨 거리 합 구하는 함수
def get_chicken_distance(home, chicken):
    total = 0
    for h in home:
        min_d = float('inf')
        for c in chicken:
            min_d = min(min_d, cal_distance(h, c))
    
        total += min_d
    return total

result = float('inf')
for comb in combinations(chicken, m):
    result = min(result, get_chicken_distance(home, comb))

print(result)
            
