# https://www.acmicpc.net/problem/28447 
from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
food = [i for i in range(n)]
data = [list(map(int, input().split())) for _ in range(n)]


result = - int(1e9)

for comb in combinations(food,k):
    local = 0
    for i in range(k):
        cri  = comb[i]
        for j in range(i+1,k):
            add = comb[j]
            local += data[cri][add]
    
    result = max(local, result)

print(result)
