# https://www.acmicpc.net/problem/11000
import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []

for _ in range(n):
    start, end = map(int, input().split())
    classes.append((start, end))

classes.sort()

# 가장 빨리 시작하는 것
# 현재 고른거의 끝나는 시간 이후 가장 빨리 시작하는 것

ends = []
heapq.heappush(ends, classes[0][1])     # 끝나는 시간 저장
room = 1

for i in range(1, n):
    s, t = classes[i]

    if s < ends[0]: # 끝나는 시간보다 일찍 시작 하면
        room += 1
    else:
        heapq.heappop(ends) # 뒤에 연강 생성되어 추가하므로 이전거는 pop

    heapq.heappush(ends, t)

print(room)
