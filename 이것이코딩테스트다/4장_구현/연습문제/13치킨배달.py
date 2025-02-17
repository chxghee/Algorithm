# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations


# 입력 세팅
n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
home = []
chicken = []

for x in range(n):
    for y in range(n):
        if data[x][y] == 1:
            home.append([x,y])
        if data[x][y] == 2:
            chicken.append([x,y])


# 거리 계산 함수
def cal_distance(home, chicken):
    return abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])


# 치킨 거리 계산 함수
def get_chicken_distance(home, chicken):
    total_d = 0
    for h in home:
        min_d = float('inf')
        for c in chicken:
            min_d = min(min_d, cal_distance(h,c))

        total_d += min_d
    return total_d

min_distance = float('inf')
for comb in combinations(chicken, m):
    min_distance = min(min_distance, get_chicken_distance(home, comb))
    

print(min_distance)