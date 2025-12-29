# https://www.acmicpc.net/contest/problem/1585/2
import heapq
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
wait = list(map(int, input().split()))

# 현재는 대기 0 시간
game = [0] * m
heapq.heapify(game)

for t in wait:
    cur_min = heapq.heappop(game)
    heapq.heappush(game, cur_min + t)

min_time = heapq.heappop(game)

if min_time <= k:
    print("WAIT")
else:
    print("GO")

