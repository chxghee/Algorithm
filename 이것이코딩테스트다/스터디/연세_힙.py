import sys
input = sys.stdin.readline

n = int(input())
c = int(input())

total_profit = 0

for _ in range(n):
    x, s, w = map(int, input().split())
    net_profit_per_fish = w - c * x
    
    if net_profit_per_fish > 0:
        total_profit += net_profit_per_fish

print(total_profit)