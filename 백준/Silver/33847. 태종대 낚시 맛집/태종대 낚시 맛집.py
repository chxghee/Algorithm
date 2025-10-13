# https://www.acmicpc.net/problem/33847
import sys
input = sys.stdin.readline

class fish:
    eat: int
    size: int
    cost: int

    def __init__(self, eat,size,cost):
        self.eat = eat
        self.size = size
        self.cost = cost

# input
n = int(input())
c=  int(input())
max_t = 0

fishes = []
for _ in range(n):
    x,size,cost = map(int, input().split())
    fishes.append(fish(x,size,cost))
    max_t += x

fishes.sort(key= lambda f: (-f.size))

# logic
# 최소 떡밥 / 최대 이익
result = 0
for t in range(max_t + 1):
    left_t = t
    t_cost = t * c
    profit = 0
    
    for fish in fishes:
        if fish.eat > left_t:
            continue

        left_t -= fish.eat
        profit += fish.cost
    
    net_profit = profit - t_cost        
    result = max(result, net_profit)

print(result)
