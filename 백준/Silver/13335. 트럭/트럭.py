# https://www.acmicpc.net/problem/13335

from collections import deque
import sys
input = sys.stdin.readline

n,l,w = map(int, input().split())
cars = list(map(int, input().split()))

# 다리에 올라간 자동차의 정보를 저장 아무것도 안 올라가 있으면 0
bridge = deque([0] * l)
now_weight = 0
time = 0
for car in cars:

    while True:
        time += 1

        out_car = bridge.popleft()
        now_weight -= out_car

        if now_weight + car <= w:
            bridge.append(car)
            now_weight += car
            break
        else:
            bridge.append(0)

print(time + l)